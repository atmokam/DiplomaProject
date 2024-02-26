import random
import os
from typing import List, Tuple
from Individual import Individual
from NetlistModifier import NetlistModifier
from MeasureParser import MeasureParser
from NetlistParser import NetlistParser
from SpecParser import SpecParser
from Simulator import Simulator


class GeneticAlgo: 
    def __init__(self, path_to_sim_folder, scales, netlist, spec, parameter_constraints):
        self._path_to_sim_folder = path_to_sim_folder
        self._scales = scales
        self._ntl_path = netlist
        ntl = NetlistParser(netlist, parameter_constraints.keys()) # dict
        self._netlist = ntl.parse()
        self._spec_path = spec
        sp = SpecParser(spec) # dict
        self._spec = sp.parse()
        self._parameter_constraints = parameter_constraints
        self._sim = Simulator(self._path_to_sim_folder)



    def _write_netlist(self, individual, out):
        ntl_mod = NetlistModifier(self._ntl_path) # read from ntl path
        ntl_mod.modify_transistor_params(individual.netlist, out, self._parameter_constraints)

    def _generate_num(self, sample_num, start, until):
        return random.randint(start, until) if isinstance(sample_num, int) else random.uniform(start, until)
    


    def _calculate_fintess(self, individual, meas: dict):
        for key, meas_val in meas.items(): 
            low = self._spec.get(key, {}).get("SpecLo")
            high = self._spec.get(key, {}).get("SpecHi")
            if low and high:
                individual.fitness += self._fitness_function(meas_val, low * self._scales[self._spec[key]["Scale"]], high * self._scales[self._spec[key]["Scale"]])


    def _fitness_function(self, measured_val, lower_bound, upper_bound):
        return (measured_val - lower_bound) / (upper_bound - lower_bound) 


    def _generate_population(self, netlist, population_size) -> List[Individual]:
        population = []
        
        for _ in range(population_size):
            for key in netlist.keys():
                netlist[key] = {k: self._generate_num(netlist[key][k], self._parameter_constraints[k][0], self._parameter_constraints[k][1]) 
                                for k in self._parameter_constraints.keys()}
            population.append(Individual(netlist.copy()))

        return population


    def _select_parents(self, population) -> Tuple[Individual, Individual]:
        rand_inds = random.sample(population, 3)
        rand_inds = sorted(rand_inds, key=lambda x: x.fitness)
        p1, p2 = rand_inds[0], rand_inds[1]
        population.remove(rand_inds[1])
        return (p1, p2)


    def _crossover(self, parent1, parent2) -> Individual:
        size = len(parent1) - random.randint(1, len(parent1)-1)
        rand_pop = random.sample(list(parent1.keys()), size)
        
        for key in rand_pop:
            parent1[key] = parent2[key]

        return parent1



    def _mutate(self, individual, rate) -> Individual:
        rand = random.random()
        if rand < rate:
            key1, key2 = random.sample(individual.keys(), 2)
            individual[key1], individual[key2] = individual[key2], individual[key1]
        return individual

    def _get_measures(self, individual, out_file):
        self._write_netlist(individual, out_file)
        script_path = os.path.join(self._path_to_sim_folder, "run_sim.sh")
        meas_file_path = self._sim.run_script(script_path)
        meas_ps = MeasureParser(meas_file_path)
        return meas_ps.parse()




    def genetic_algorithm(self, population_size, generations, mutation_rate):

        population = self._generate_population(self._netlist, population_size) 
        deck_file = self._path_to_sim_folder + "deck.sp"

        for individual in population:
            measured_vals = self._get_measures(individual, deck_file)
            self._calculate_fintess(individual, measured_vals)
           
            
        for _ in range(generations):
            parent1, parent2 = self._select_parents(population) 
            child = self._crossover(parent1.netlist.copy(), parent2.netlist.copy())
            child = Individual(self._mutate(child, mutation_rate))

            measured_vals = self._get_measures(child, deck_file)
            self._calculate_fintess(child, measured_vals)
        
            population.append(child)


        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        return population[0].netlist
    
           
        
