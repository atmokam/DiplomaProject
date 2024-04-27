#import subprocess
#import os
#import glob
from Model import Model
from DataScaler import DataScaler
from Constraints import Constraints


class Simulator:
    def __init__(self, path = None):
        self.model = Model()
        self.path = path #path to model
        self.constraints = None
        self.scaler = DataScaler()
        self.measure_names = []

    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, path):
        self._path = path
        self.model.load(path)
        

    # def run_script(self, script_path):
    #     subprocess.check_call(['bash', script_path])

    #     files = glob.glob(os.path.join(self.path, "*.m*"))
    #     if not files:
    #         raise Exception("no file found with .m*")
    #     original_file_path = files[0] 

    #     return original_file_path
    
    def run_model(self, ntl):
        for data in ntl:
            self.scaler.scale_ntl(data)

        result = self.model.predict(ntl)
        
        measures = {}
        for name, meas in zip(self.measure_names, result[0]):
            measures[name] = meas

        self.scaler.unscale_meas(measures)

        return measures

        


    
