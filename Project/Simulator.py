#import subprocess
#import os
#import glob
from Model import Model
from DataScaler import DataScaler
from Constraints import Constraints


class Simulator:
    def __init__(self, path = None):
        self.path = path #path to model
        self.constraints = None
        self.model = Model()

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
    
    def run_model(self, model, ntl):
        return model.predict(ntl)
    
