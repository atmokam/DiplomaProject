import re


class MeasureParser:
    def __init__(self, path):
        self._measure_file = self._read_file(path)
    #let it not read
    # i'm gonna need list to dict conversion

    def _read_file(self, path):
        with open(path, 'r') as f:
            return f.readlines()

    def parse(self):
        param_list = []
        pattern = re.compile(r"(?<!\w)-?\d+?\.?\d*?e?-?\d*?(?!\w)")
        ind = 0
        for i, line in enumerate(self._measure_file):
            if line and not "VERSION" in line and not ".TITLE" in line and not "Measures" in line:
                arg_list = line.split()
                if len(arg_list) < 1:
                    continue
                matched = pattern.search(arg_list[0])
                if matched:
                    ind = i
                    break
                for arg in arg_list:
                    param_list.append(arg)

        val_list = []
        for line in self._measure_file[ind:]:
            val_list += line.split()


        output = {}
        for arg, val in zip(param_list, val_list):
            output[arg] = float(val)
                              
        return output
    

    
        