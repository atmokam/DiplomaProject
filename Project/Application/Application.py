import os, sys
from PyQt5.QtWidgets import QApplication
from UI.MainWindow import MainWindow
from MainAlgorithm.Constraints import Constraints
from DataProcessing.NetlistParser import NetlistParser
from DataProcessing.SpecParser import SpecParser
from DataProcessing.CsvParser import CsvParser
from MainAlgorithm.Controller import Controller


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self._generations = 0
        self._population = 0
        self._constraints = Constraints()
        self._scales = {"pic": 10**-12, "pico": 10**-12, "nan": 10**-9, "nano": 10**-9, "0": 1,
                         "kil": 10**3 , "kilo": 10**3, "meg": 10**6, "mega":  10**6}
        self.run_gui()

    def run_gui(self):
        mainWindow = MainWindow(self)
        mainWindow.show()
        sys.exit(super().exec_())


    def _process_input(self):
        parser = NetlistParser(self._netlist, self._constraints.netlist_constraints.keys())
        specs = SpecParser(self._spec).parse()
        _, _, measures = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/Project/files/output (3).csv").parse()
        self._constraints.measure_constraints = self._constraints.calculate_measure_constraints(measures)
        
        netlist = parser.parse()
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
    def measure_constraints(self):
        return self._constraints.measure_constraints
    
    @measure_constraints.setter
    def measure_constraints(self, constraints):
        self._constraints.measure_constraints = constraints


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

    