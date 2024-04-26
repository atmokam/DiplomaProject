import subprocess
#import time
import os
import glob

class Simulator:
    def __init__(self, path):
        self.path = path

    def run_script(self, script_path):
        subprocess.check_call(['bash', script_path])

        files = glob.glob(os.path.join(self.path, "*.m*"))
        if not files:
            raise Exception("no file found with .m*")
        original_file_path = files[0] 

        return original_file_path
    
    def run_model(self, model, ntl):
        return model.predict(ntl)
    
