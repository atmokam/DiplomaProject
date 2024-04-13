import os
import pickle
from GeneticAlgo import GeneticAlgo


class Application:

    def run_genetic_algo(self, population_size, generations):
        gen_algo = GeneticAlgo(self._sim_folder, self._scales, self._netlist, self._spec, self._parameter_constraints)
        return gen_algo.genetic_algorithm(population_size, generations, 0.6)
 

    def run(self):
        path = os.path.join(self._sim_folder, "result.pkl")
        with open(path, 'wb') as f:
            result = self.run_genetic_algo(200, 30)
            pickle.dump(result, f)
            print(result)
            


    # Getters and setters

    @property
    def generations(self):
        return self._generations
    
    @generations.setter
    def generations(self, generations):
        self._generations = generations
        print(self._generations)

    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, population):
        self._population = population

    @property
    def sim_folder(self):
        return self._sim_folder
    
    @sim_folder.setter
    def sim_folder(self, path):
        self._sim_folder = path


    @property
    def parameter_constraints(self):
        return self._parameter_constraints
    
    @parameter_constraints.setter
    def parameter_constraints(self, constraints):
        self._parameter_constraints = constraints

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

    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, path):
        self._spec = path

    