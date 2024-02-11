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


    def _write_netlist(self, individual, param_constraints, out):
        ntl_parser = NetlistParser(self._netlist_path)
        ntl_parser.parameter_names = param_constraints.keys()
        ntl_parser.modify_transistor_params(individual.netlist, out, param_constraints)

    def _generate_num(self, sample_num, start, until):
        return random.randint(start, until) if isinstance(sample_num, int) else random.uniform(start, until)
    



    def _generate_population(self, netlist, population_size, param_constraints) -> List[Individual]:
        population = []
       
        for _ in range(population_size):
            for key in netlist.keys():
                netlist[key] = {k: self._generate_num(netlist[key][k], param_constraints[k][0], param_constraints[k][1]) 
                                for k in param_constraints.keys()}
            population.append(Individual(netlist.copy()))

        return population


    def _fitness_function(self, measured_val, lower_bound, upper_bound):
        return (measured_val - lower_bound) / (upper_bound - lower_bound) 


    def _select_parents(self, population) -> Tuple[Individual, Individual]:
        pass


    def _crossover(self, parent1, parent2) -> Individual:
        pass


    def _mutate(self, individual) -> Individual:
        pass



    def genetic_algorithm(self, netlist, spec, population_size, generations, param_constraints):

        population = self._generate_population(netlist, population_size, param_constraints) 
        deck_file = self._path_to_sim_folder + "deck.sp"

        for individual in population:
            self._write_netlist(individual, param_constraints, deck_file)
            # run hspice simulation -> measures file
            meas_file = self._path_to_sim_folder + "meas.txt" # path will be returned from simulator (.m*#)
            meas_ps = MeasureParser(meas_file)
            measured_vals = meas_ps.parse() # parse measured values <--- just parse from file for now
            
            for key, meas_val in measured_vals.items():
                low = spec.get(key, {}).get("SpecLo")
                high = spec.get(key, {}).get("SpecHi")
                if low and high:
                    individual.fitness += self._fitness_function(meas_val, low, high)
   

        # for _ in range(generations):
        #     parent1, parent2 = self._select_parents(population) 
        #     child = self._crossover(parent1, parent2)
        #     # simulate
        #     child = self._mutate(child) * rate
        #     population.append(child)

        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        return population[0].netlist
    
           
        
