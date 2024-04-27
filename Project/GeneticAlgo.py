import random, os
from CsvWriter import CsvWriter
from typing import List
from Individual import Individual
from NetlistModifier import NetlistModifier
from MeasureParser import MeasureParser
from NetlistParser import NetlistParser
from SpecParser import SpecParser
from Simulator import Simulator
from Model import Model


class GeneticAlgo:

    def __init__(self, simulator, scales, netlist, spec, parameter_constraints):
        self._scales = scales
        self._parameter_constraints = parameter_constraints
        parser = NetlistParser(netlist, parameter_constraints.keys())
        self._netlist = parser.parse()
        
        self._ntl_path = netlist
        self._spec_path = spec
        self._spec = SpecParser(spec).parse()

        self._sim = simulator
        self._sim.measure_names = parser.parse_measure_names()

       


    def _write_netlist(self, individual, out): 
        ntl_mod = NetlistModifier(self._ntl_path)
        ntl_mod.modify_transistor_params(individual.netlist, out, self._parameter_constraints)
    # shouldve been part of simulator, doesnt belong here

    def _generate_num(self, sample_num, start, until):
        if isinstance(sample_num, int):
            return random.randint(start, until)
        return random.uniform(start, until)

    def _calculate_fintess(self, meas):
        fitness = 0.0
        for key, meas_val in meas.items():
            low = self._spec.get(key, {}).get('SpecLo')
            high = self._spec.get(key, {}).get('SpecHi')

            if low and high:
                spec_key = self._spec.get(key, {}).get('Scale')
                scale = self._scales.get(spec_key)
                
                fitness += self._fitness_function(meas_val, low * scale, high * scale)

        return fitness


    def _fitness_function(self, measured_val, lower_bound, upper_bound):
        if lower_bound <= measured_val <= upper_bound:
            return 1
        else:
            mid = (lower_bound + upper_bound) / 2
            return -abs(measured_val - mid) / mid

    def _generate_population(self, netlist, population_size) -> List[Individual]:
        population = []
        for _ in range(population_size):
            new_net = netlist.copy()
            for key in netlist.keys():
                new_net[key] = {param: self._generate_num(new_net[key][param], 
                                                          self._parameter_constraints[param][0], self._parameter_constraints[param][1]) 
                                                          for param in self._parameter_constraints.keys()}

            population.append(Individual(new_net.copy()))

        return population

    def _select_parents(self, population, size):
        if len(population) > size: #tournament selection
            sample_length = random.randint(size, len(population))
            p1 = random.sample(population, sample_length)
            p2 = random.sample(population, sample_length)
        
            p1.sort(key=(lambda x: x.fitness), reverse=True)
            p2.sort(key=(lambda x: x.fitness), reverse=True)
            result1 = p1[:size]
            result2 = p1[:size]

            random.shuffle(result1)
            random.shuffle(result2)
        else:
            result1 = random.sample(population, size)
            result2 = random.sample(population, size)
        return result1, result2

    def _crossover(self, parent_pop1, parent_pop2):
        result = []
        for par1, par2 in zip(parent_pop1, parent_pop2):
            net1, net2 = par1.netlist.copy(), par2.netlist.copy()
            size = random.randint(1, len(net1) - 1)
            rand_pop = random.sample(list(net1.keys()), size)
            for key in rand_pop:
                net1[key] = net2[key]

            par1.netlist = net1
            result.append(par1)
        return result

    def _mutate(self, pop, rate):
        for individual in pop:
            rand = random.random()
            if rand < rate:
                key = random.sample(individual.netlist.keys(), 1)
                param = random.sample(individual.netlist[key[0]].keys(), 1)[0]
                individual.netlist[key] = {param: self._generate_num(individual.netlist[key][param],
                                                                        self._parameter_constraints[param][0], self._parameter_constraints[param][1])}

        return pop

    def _get_measures(self, individual, out_file):
        #self._write_netlist(individual, out_file)
        #meas_file_path = self._sim.run_script(self._script_path)
        return self._sim.run_model(individual.netlist)


    def _initialize_individuals(self, population, best_fitness=float('-inf'), best_individual=None):
        for individual in population:
            individual.measures = self._get_measures(individual, self._deck_file)
            individual.fitness = self._calculate_fintess(individual.measures)

            if individual.fitness > best_fitness:
                best_fitness = individual.fitness
                best_individual = individual

        return best_fitness, best_individual


    def genetic_algorithm(self, population_size, generations, mutation_rate):
        population = self._generate_population(self._netlist.copy(), population_size)

        best_fitness, best_individual = self._initialize_individuals(population)
        fitness_data = [best_fitness]

        for _ in range(generations):
            parent1, parent2 = self._select_parents(population, population_size)
            child = self._crossover(parent1.copy(), parent2.copy())
            child = self._mutate(child, mutation_rate)

            best_fitness, best_individual = self._initialize_individuals(child, best_fitness, best_individual)
            
            fitness_data.append(best_fitness)
            population.extend(child)

        print(best_fitness)
        return best_individual.netlist