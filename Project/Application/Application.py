import os, sys
from PyQt5.QtWidgets import QApplication
from UI.MainWindow import MainWindow
from MainAlgorithm.Constraints import Constraints
from DataProcessing.NetlistParser import NetlistParser
from DataProcessing.SpecParser import SpecParser
from MainAlgorithm.Controller import Controller


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self._generations = 0
        self._population = 0
        self._constraints = Constraints()
        self._scales = {}
        self.run_gui()

    def run_gui(self):
        mainWindow = MainWindow(self)
        mainWindow.show()
        sys.exit(super().exec_())


    def _process_input(self):
        parser = NetlistParser(self._netlist, self._constraints.netlist_constraints.keys())
        netlist = parser.parse()
        print(netlist, self._constraints.netlist_constraints)
        
        specs = SpecParser(self._spec).parse()
        measure_names = parser.parse_measure_names()
        name = os.path.splitext(os.path.basename(self._netlist))[0] + '.keras'
        self._simulator_path = os.path.join(os.path.dirname(self._netlist), name)
        return netlist, specs, measure_names


    def run(self):
        netlist, specs, meas_names = self._process_input()
        controller = Controller(self._simulator_path, netlist, specs,
                                 meas_names, self._scales, self._constraints)
        return controller.run(self.population, self.generations)
       

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
    def constraints(self):
        return self._constraints
    
    @constraints.setter
    def constraints(self, constraints):
        self._constraints = constraints


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
        print(path)
      

    @property
    def spec(self):
        return self._spec
    
    @spec.setter
    def spec(self, path):
        self._spec = path

    