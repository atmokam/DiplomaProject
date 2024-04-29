import os
import pickle
from GeneticAlgorithm import GeneticAlgorithm
from Simulator import Simulator
from Constraints import Constraints
from NetlistParser import NetlistParser
from SpecParser import SpecParser


class Application:
    def __init__(self):
        self._generations = 0
        self._population = 0
        self._constraints = Constraints()
        self._scales = {}
        self._simulator = Simulator()

    def _run_genetic_algorithm(self, population_size, generations):

        parameter_constraints = self._constraints.netlist_constraints
        parser = NetlistParser(self._netlist, parameter_constraints.keys())
        netlist = parser.parse()
        specs = SpecParser(self._spec).parse()
        self._simulator.measure_names = parser.parse_measure_names()

        gen_algo = GeneticAlgorithm(self._simulator, self._scales, netlist, 
                               specs, parameter_constraints)
        
        return gen_algo.genetic_algorithm(population_size, generations, 0.6)
 

    def run(self):
        path = os.path.join(self.sim_folder, "result.pkl")
        result = self._run_genetic_algorithm(self.generations, self.population)
        with open(path, 'wb') as f:
            pickle.dump(result, f)
        print(result)
            

    @property
    def generations(self):
        return self._generations
    
    @generations.setter
    def generations(self, generations):
        self._generations = generations

    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, population):
        self._population = population

    @property
    def sim_folder(self):
        return os.path.dirname(self._simulator.path)


    @property
    def constraints(self):
        return self._constraints
    
    @constraints.setter
    def constraints(self, constraints):
        self._constraints = constraints
        self._simulator.constraints = constraints


    @property
    def scales(self):
        return self._scales
    
    @scales.setter
    def scales(self, scales):
        self._scales = scales

    @property
    def netlist(self):
        return self._netlist
    
    @netlist.setter
    def netlist(self, path):
        self._netlist = path
        name = os.path.splitext(os.path.basename(path))[0] + '.keras'
        self._simulator.path = os.path.join(os.path.dirname(path), name)

    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, path):
        self._spec = path

    