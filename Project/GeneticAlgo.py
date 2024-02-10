import random
from typing import List, Tuple
import NetlistParser

class Individual:
    def __init__(self, params: dict[str, str]):
       pass



class GeneticAlgo:    

    def fitness_function(self, measured_val, lower_bound, upper_bound):
        return (measured_val - lower_bound) / (upper_bound - lower_bound) 


    def generate_population(population_size, parameter_constraints) -> List[Individual]:
        population = []
        for _ in range(population_size):
            param_dict = {}
            for name in parameter_constraints.keys():
                param_dict[f"{name}"] = random.uniform(parameter_constraints[name][0], parameter_constraints[name][1])
            individual = Individual(param_dict)
            population.append(individual)

        return population


    def select_parents(self, population) -> Tuple[Individual, Individual]:
        pass


    def crossover(self, parent1, parent2) -> Individual:
        # impl crossover
        result = Individual() # change this
        return result


    def mutate(self, individual) -> Individual:
        pass


    def genetic_algorithm(self, generations, population_size, generate_from, param_constraints):

        population = self.generate_population(population_size) 
        # write to netlist
        # wrong: population_dict = {f"xm{i}": population[i].params for i in range(len(population))}
        # move these:
        netlist_parser = NetlistParser("path", param_constraints.keys())
        netlist_parser.modify_transistor_params()
        # run hspice simulation -> measures file
        # parse measured values
        # calculate fitness on measured values

        # for individual in population:
        #     for key in individual.params.keys():
        #         pass
                #individual.fitness += self.fitness_function(key, param_constraints[key][0], param_constraints[key][1])

        for _ in range(generations):
            parent1, parent2 = self.select_parents(population) 
            child = self.crossover(parent1, parent2)
            # simulate
            child = self.mutate(child) * rate
            population.append(child)

        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        return population[0].params
    
           
        
