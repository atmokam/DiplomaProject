import re
# in file modifier 

class NetlistModifier:
    def __init__(self, path):
        self._file = self._read_file(path)

    def _read_file(self, path):
        with open(path, 'r') as f:
            return f.readlines()
        
    
    def _replacer(self, regex, line, param):
        start = 0
        new_string = ''
        for match in re.finditer(regex, line):
            end, new_start = match.span(2)
            new_string += line[start:end] + str(param)
            start = new_start
        new_string += line[start:]
        return new_string

    
    def _clamp(self, n, smallest, largest):
        return max(smallest, min(n, largest))

    def _constrain(self, new_params, param_constraints):
        for values in new_params.values():
            for param, p_tuple in param_constraints.items():
                values[param] = self._clamp(values[param], p_tuple[0], p_tuple[1])


    def modify_transistor_params(self, new_params, out, constraints):
    
        self._constrain(new_params, constraints)
        parameter_names = constraints.keys()

        for i, line in enumerate(self._file):
            if line.startswith("x"):
                name = line.split(' ', 1)[0]
                if name not in new_params:
                    continue
                for param in parameter_names:
                    line = self._replacer(f"({param})\\s*=\\s*([\\d.]+)", line, new_params[name][param])
                    self._file[i] = line

        with open(out, 'w') as f:
            f.writelines(self._file)