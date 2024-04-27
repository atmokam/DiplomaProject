import os
import pickle
from GeneticAlgo import GeneticAlgo
from Simulator import Simulator
from Constraints import Constraints


class Application:
    def __init__(self):
        self._generations = 0
        self._population = 0
        self._constraints = Constraints()
        self._scales = {}
        self._netlist = ""
        self._spec = ""
        self._simulator = Simulator()

    def _run_genetic_algo(self, population_size, generations):
        gen_algo = GeneticAlgo(self._simulator, self._scales, self._netlist, 
                               self._spec, self._constraints.netlist_constraints)
        return gen_algo.genetic_algorithm(population_size, generations, 0.6)
 

    def run(self):
        path = os.path.join(self._sim_folder, "result.pkl")
        result = self._run_genetic_algo(self.generations, self.population)
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
        return self._simulator.path

    @sim_folder.setter
    def sim_folder(self, path):
        self._simulator.path = path


    @property
    def parameter_constraints(self):
        return self._constraints.netlist_constraints
    
    @parameter_constraints.setter
    def parameter_constraints(self, constraints):
        self._constraints.netlist_constraints = constraints
        self._simulator.constraints = Constraints()
        self._simulator.constraints.netlist_constraints = constraints

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
        name = os.path.splitext(os.path.basename(path))[0]
        self._simulator.path = os.path.join(os.path.dirname(path), name)

    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, path):
        self._spec = path

    