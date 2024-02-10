import re


class NetlistParser:
   
    def __init__(self, path, parameter_names: list[str]):
        self.path = path
        self.parameter_names = parameter_names

    def parse(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()

        output = {}
        for line in lines:
            params = {}
            for val in self.parameter_names:
                pattern = re.compile(f"^(x\w+).*?({val})\\s*=\\s*([\\d.]+)")
                match = pattern.search(line)
                if match:
                    name = match.group(1)
                    key = match.group(2)
                    value = match.group(3)
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

    def modify_transistor_params(self, new_params:  dict[str, dict[str, str]], param_constraints, out: str):
        with open(self.path, 'r') as f:
            lines = f.readlines()

        for values in new_params.values():
            for param, p_tuple in param_constraints.items():
                values[param] = str(self._clamp(float(values[param]), p_tuple[0], p_tuple[1]))

        for i, line in enumerate(lines):
            if line.startswith("x"):
                for val in param_constraints.keys():
                    name = line.split(' ', 1)[0]
                    if name not in new_params:
                        continue
                    line = self._replacer(f"({val})\\s*=\\s*([\\d.]+)", line, new_params[name][val])

                    lines[i] = line

        with open(out, 'w') as f:
            f.writelines(lines)
