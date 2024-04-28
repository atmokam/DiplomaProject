import re


class NetlistParser:
    def __init__(self, path, names = []):
        self._file = self._read_file(path)
        self._parameter_names = names
   
    @property
    def parameter_names(self):
        return self._parameter_names

    @parameter_names.setter
    def parameter_names(self, params):
        self._parameter_names = params
    

    def _read_file(self, path):
        with open(path, 'r') as f:
            return f.readlines()


    def parse(self):
        output = {}
        for line in self._file:
            params = {}
            for val in self.parameter_names:
                pattern = re.compile(f"^(x\\w+).*?({val})\\s*=\\s*([\\d.]+)")
                match = pattern.search(line)
                if match:
                    name = match.group(1)
                    key = match.group(2)
                    value = match.group(3)
                    try:
                        value = int(value)
                    except ValueError:
                        value = float(value)
                    params[key] = value
                    output[name] = params            

        return output
    
    def parse_measure_names(self):
        output = []
        pattern = re.compile(r"^\.meas\s+?\w+?\s+?(\w+)")
        for line in self._file:
            match = pattern.search(line)
            if match:
                output.append(match.group(1))

        return output
