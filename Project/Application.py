from GeneticAlgo import GeneticAlgo
from NetlistParser import NetlistParser
from SpecParser import SpecParser


class Application:

    def run_genetic_algo(self, population_size, generations):
        self._netlist.parameter_names = self._parameter_constraints.keys()
        gen_algo = GeneticAlgo(self._sim_folder, self._scales)
        return gen_algo.genetic_algorithm( self._netlist.parse(), self._spec.parse(), \
                                           population_size, generations, self._parameter_constraints, 0.6)
 

    # Getters and setters

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
    def netlist(self, netlist_path):
        self._netlist = NetlistParser(netlist_path)

    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, spec_path):
        self._spec = SpecParser(spec_path)

    