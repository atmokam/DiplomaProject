#import subprocess
#import os
#import glob
from Model import Model
from DataScaler import DataScaler


class Simulator:
    def __init__(self, path = None):
        self.model = Model() 
        self.scaler = DataScaler()
        self.measure_names = []

    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, path):
        self._path = path
        self.model.load(path)

    @property
    def constraints(self):
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        self._constraints = constraints
        self.scaler.ntl_constraints = constraints.netlist_constraints
        self.scaler.meas_constraints = constraints.measure_constraints
        

    # def run_script(self, script_path):
    #     subprocess.check_call(['bash', script_path])

    #     files = glob.glob(os.path.join(self.path, "*.m*"))
    #     if not files:
    #         raise Exception("no file found with .m*")
    #     original_file_path = files[0] 

    #     return original_file_path
    
    def run_model(self, ntl):
        self.scaler.scale_ntl(ntl)

        result = self.model.predict(ntl)
        
        measures = {}
        for name, meas in zip(self.measure_names, result[0]):
            measures[name] = meas

        self.scaler.unscale_meas(measures)

        return measures

        


    
