from MainAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from ANN.Simulator import Simulator


class Controller:
    def __init__(self, simulator_path, netlist, specs, meas_names, scales, constraints):
        self.simulator = Simulator()
        self.simulator.path = simulator_path
        self.simulator.constraints = constraints
        self.simulator.measure_names = meas_names
        self.netlist = netlist
        self.specs = specs
        self.scales = scales
        self.constraints = constraints
 

    def run(self, population, generations):
        gen_algo = GeneticAlgorithm(self.simulator, self.scales, self.netlist, 
                               self.specs, self.constraints.netlist_constraints)
        
        result = gen_algo.genetic_algorithm(population, generations, 0.6)
        return result
            

