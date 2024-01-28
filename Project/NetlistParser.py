import re


class NetlistParser:
    """ Parser prerequisites: netlist is valid"""
    def __init__(self, path, out, w_tuple, l_tuple, nf_tuple):
        self.path = path
        self.out = out
        self.w_tuple = w_tuple
        self.l_tuple = l_tuple
        self.nf_tuple = nf_tuple
        self.parameters = {"w": w_tuple, "l": l_tuple, "nf": nf_tuple}

    def parse(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()

        output = {}
        params = {}
        for line in lines:
            if line.startswith("x"):
                for val in self.parameters.keys():
                    name = line.split(' ', 1)[0]
                    output[name] = {}

                    pattern = re.compile(f"({val})\\s*=\\s*([\\d.]+)")
                    match = pattern.search(line)
                    if match:
                        key = match.group(1)
                        value = match.group(2)
                        params[key] = value

                    output[name].update(params)
            else:
                continue

        return output

    # noinspection PyMethodMayBeStatic
    def _replacer(self, regex, line, param):
        start = 0
        new_string = ''
        for match in re.finditer(regex, line):
            end, new_start = match.span(2)
            new_string += line[start:end] + param
            start = new_start
        new_string += line[start:]
        return new_string

    # noinspection PyMethodMayBeStatic
    def _clamp(self, n, smallest, largest):
        return max(smallest, min(n, largest))

    def modify_transistor_params(self, new_params:  dict[str, dict[str, str]]):
        # Read the original file
        with open(self.path, 'r') as f:
            lines = f.readlines()

        for key, values in new_params.items():
            for param, p_tuple in self.parameters.items():
                values[param] = str(self._clamp(float(values[param]), p_tuple[0], p_tuple[1]))

        for i, line in enumerate(lines):
            if line.startswith("x"):
                for val in self.parameters.keys():
                    name = line.split(' ', 1)[0]
                    if name not in new_params:
                        continue
                    line = self._replacer(f"({val})\\s*=\\s*([\\d.]+)", line, new_params[name][val])

                    lines[i] = line

        with open(self.out, 'w') as f:
            f.writelines(lines)
