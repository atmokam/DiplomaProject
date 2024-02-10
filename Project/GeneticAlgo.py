import random
from typing import List, Tuple
from Individual import Individual


class GeneticAlgo:    

    def fitness_function(self, measured_val, lower_bound, upper_bound):
        return (measured_val - lower_bound) / (upper_bound - lower_bound) 


    def generate_population(self, netlist, population_size, parameter_constraints) -> List[Individual]:
        population = []

        for _ in range(population_size):
            for key in netlist.keys():
                netlist[key] = {k: random.uniform(parameter_constraints[k][0], parameter_constraints[k][1]) 
                                for k in parameter_constraints.keys()}
            population.append(Individual(netlist.copy()))

        return population


    def select_parents(self, population) -> Tuple[Individual, Individual]:
        pass


    def crossover(self, parent1, parent2) -> Individual:
        pass


    def mutate(self, individual) -> Individual:
        pass


    def genetic_algorithm(self, netlist, spec, population_size, generations, param_constraints):

        population = self.generate_population(netlist, population_size, param_constraints) 
        # write to netlist
        
        # run hspice simulation -> measures file
        # parse measured values
        # calculate fitness on measured values

        for individual in population:
           pass
                #individual.fitness += self.fitness_function(measured_val, spec[key][0], spec[key][1])

        for _ in range(generations):
            parent1, parent2 = self.select_parents(population) 
            child = self.crossover(parent1, parent2)
            # simulate
            child = self.mutate(child) * rate
            population.append(child)

        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        return population[0].params
    
           
        
