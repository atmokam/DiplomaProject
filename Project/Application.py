from GeneticAlgo import GeneticAlgo
from NetlistParser import NetlistParser
from SpecParser import SpecParser


class Application:
    def __init__(self):
        self._spec_path = ""
        self._netlist_path = ""
        self._sim_folder = ""
        self._parameter_constraints = {"w": (0.2, 2.4), "l": (0.03, 0.03), "nf": (1, 10)}

    @property
    def parameter_constraints(self):
        return self._parameter_constraints
    
    @parameter_constraints.setter
    def parameter_constraints(self, value):
        self._parameter_constraints = value


    @property
    def netlist_path(self):
        return self._netlist_path
    
    @netlist_path.setter
    def netlist_path(self, path):
        self._netlist_path = path


    @property
    def spec_path(self):
        return self._spec_path
    
    @spec_path.setter
    def spec_path(self, path):
        self._spec_path = path

    
    @property
    def sim_folder(self):
        return self._sim_folder
    
    @sim_folder.setter
    def sim_folder(self, path):
        self._sim_folder = path
    
    
        

    def run_genetic_algo(self, population_size, generations):

        spec_prs = SpecParser(self._spec_path)
        netlist_prs = NetlistParser(self._netlist_path)
        netlist_prs.parameter_names = self._parameter_constraints.keys()

        spec_parsed = spec_prs.parse()
        ntl_parsed = netlist_prs.parse()

        gen_algo = GeneticAlgo(self._sim_folder, self._spec_path, self._netlist_path)
        return gen_algo.genetic_algorithm(ntl_parsed, spec_parsed, population_size, generations, self._parameter_constraints, 0.6)
    
    
