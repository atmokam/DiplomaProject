import re


class NetlistParser:
    def __init__(self, path, names = []):
        self._parameter_names = names
        self._file = self._read_file(path)
   
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
                pattern = re.compile(f"^(x\w+).*?({val})\\s*=\\s*([\\d.]+)")
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


    def _replacer(self, regex, line, param):
        start = 0
        new_string = ''
        for match in re.finditer(regex, line):
            end, new_start = match.span(2)
            new_string += line[start:end] + param
            start = new_start
        new_string += line[start:]
        return new_string

    
    def _clamp(self, n, smallest, largest):
        return max(smallest, min(n, largest))

    def _constrain(self, new_params, param_constraints):
        for values in new_params.values():
            for param, p_tuple in param_constraints.items():
                values[param] = str(self._clamp(values[param], p_tuple[0], p_tuple[1]))


    def modify_transistor_params(self, new_params:  dict[str, dict[str, str]], out: str, constraints = None):
        
        if constraints:
            self._constrain(new_params, constraints)

        for i, line in enumerate(self._file):
            if line.startswith("x"):
                name = line.split(' ', 1)[0]
                if name not in new_params:
                    continue
                for param in self.parameter_names:
                    line = self._replacer(f"({param})\\s*=\\s*([\\d.]+)", line, new_params[name][param])
                    self._file[i] = line

        with open(out, 'w') as f:
            f.writelines(self._file)
