from GeneticAlgo import GeneticAlgo
from NetlistParser import NetlistParser
from SpecParser import SpecParser


class Application:
    def __init__(self):
        self._spec_file = ""
        self._netlist_file = ""
        self._parameter_constraints = {"w": (0.2, 2.4), "l": (0.03, 0.03), "nf": (1, 10)}

    @property
    def parameter_constraints(self):
        return self._parameter_constraints
    
    @parameter_constraints.setter
    def parameter_constraints(self, value):
        self._parameter_constraints = value


    @property
    def netlist_file(self):
        return self._netlist_file
    
    @netlist_file.setter
    def netlist_file(self, path):
        self._netlist_file = self.read_from_file(path)


    @property
    def spec_file(self):
        return self._spec_file
    
    @spec_file.setter
    def spec_file(self, path):
        self._spec_file = self.read_from_file(path)
    
    def read_from_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.readlines()
        

    def run_genetic_algo(self, population_size, generations):

        spec = SpecParser(self._spec_file)
        netlist = NetlistParser(self._netlist_file, self._parameter_constraints.keys())

        spec_parsed = spec.parse()
        ntl_parsed = netlist.parse()
       
        # return GeneticAlgo.genetic_algorithm(ntl_parsed, spec_parsed, population_size,
        #                                       generations, self._parameter_constraints)
    

