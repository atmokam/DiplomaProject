import random
from typing import List, Tuple
from Individual import Individual
from NetlistParser import NetlistParser
from MeasureParser import MeasureParser


class GeneticAlgo: 
    def __init__(self, path_to_sim_folder, spec_path, netlist_path):
        self._path_to_sim_folder = path_to_sim_folder
        self._spec_path = spec_path
        self._netlist_path = netlist_path
        self._scale = {"pic": 10**-12, "pico": 10**-12, "nan": 10**-9, "nano": 10**-9, "0": 1, "kil": 10**3 , "kilo": 10**3, "meg": 10**6, "mega":  10**6}


    def _write_netlist(self, individual, param_constraints, out):
        ntl_parser = NetlistParser(self._netlist_path)
        ntl_parser.parameter_names = param_constraints.keys()
        ntl_parser.modify_transistor_params(individual.netlist, out, param_constraints)

    def _generate_num(self, sample_num, start, until):
        return random.randint(start, until) if isinstance(sample_num, int) else random.uniform(start, until)
    


    def _calculate_fintess(self, individual, spec, meas):
        for key, meas_val in meas.items(): 
            low = spec.get(key, {}).get("SpecLo")
            high = spec.get(key, {}).get("SpecHi")
            if low and high:
                individual.fitness += self._fitness_function(meas_val, low * self._scale[spec[key]["Scale"]], high * self._scale[spec[key]["Scale"]])


    def _fitness_function(self, measured_val, lower_bound, upper_bound):
        return (measured_val - lower_bound) / (upper_bound - lower_bound) 


    def _generate_population(self, netlist, population_size, param_constraints) -> List[Individual]:
        population = []
       
        for _ in range(population_size):
            for key in netlist.keys():
                netlist[key] = {k: self._generate_num(netlist[key][k], param_constraints[k][0], param_constraints[k][1]) 
                                for k in param_constraints.keys()}
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



    def genetic_algorithm(self, netlist, spec, population_size, generations, param_constraints, mutation_rate):

        population = self._generate_population(netlist, population_size, param_constraints) 
        deck_file = self._path_to_sim_folder + "deck.sp"

        for individual in population:
            self._write_netlist(individual, param_constraints, deck_file)
            # run hspice simulation -> measures file
            meas_file = self._path_to_sim_folder + "meas.txt" # path will be returned from simulator (.m*#), i.e. Simulator(self._path_to_sim_folder).run()
            meas_ps = MeasureParser(meas_file)
            measured_vals = meas_ps.parse() 
            self._calculate_fintess(individual, spec, measured_vals)
           
            
        for _ in range(generations):
            parent1, parent2 = self._select_parents(population) 
            child = self._crossover(parent1.netlist.copy(), parent2.netlist.copy())
            child = Individual(self._mutate(child, mutation_rate))
            # simulate, calc fitness
            population.append(child)

        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        return population[0].netlist
    
           
        
