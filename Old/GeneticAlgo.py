import random
import os
import csv
from CsvWriter import CsvWriter
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
        self._netlist = NetlistParser(netlist, parameter_constraints.keys()).parse() # dict
        self._spec_path = spec
        self._spec = SpecParser(spec).parse() # dict
        self._parameter_constraints = parameter_constraints
        self._sim = Simulator(self._path_to_sim_folder)

        self._csv_file = os.path.join(self._path_to_sim_folder, "output.csv")
        self._script_path = os.path.join(self._path_to_sim_folder, "run_sim.sh")
        self._deck_file = os.path.join(self._path_to_sim_folder, "deck_file.sp")



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
        #population.remove(rand_inds[1])
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
        meas_file_path = self._sim.run_script(self._script_path)
        return MeasureParser(meas_file_path).parse()



    def genetic_algorithm(self, population_size, generations, mutation_rate):

        population = self._generate_population(self._netlist, population_size)
        writer = CsvWriter(self._csv_file, population[0])
        
        for individual in population:
            measured_vals = self._get_measures(individual, self._deck_file)
            self._calculate_fintess(individual, measured_vals)
            writer.write_csv(individual)
           
        for _ in range(generations):
            parent1, parent2 = self._select_parents(population) 
            child = self._crossover(parent1.netlist.copy(), parent2.netlist.copy())
            child = Individual(self._mutate(child, mutation_rate))

            measured_vals = self._get_measures(child, self._deck_file)
            self._calculate_fintess(child, measured_vals)
            writer.write_csv(child)

            population.append(child)

        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        return population[0].netlist
    
           
        
