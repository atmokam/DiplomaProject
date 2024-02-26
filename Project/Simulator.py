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
    

    #  I probably don't need this part anywhere
        # original_prefix = os.path.splitext(os.path.basename(original_file_path))[1]

        # timestamp = time.strftime("%Y%m%d-%H%M%S")
        # unique_filename = "{}{}".format(timestamp, original_prefix)

        # unique_file_path = os.path.join(self.path, unique_filename)

        # os.rename(original_file_path, unique_file_path)
