import re


class Parser:
    """ Parser prerequisites: netlist is valid"""
    def __init__(self, path, out, w_tuple, l_tuple, nf_tuple):
        self.path = path
        self.out = out
        self.w_tuple = w_tuple
        self.l_tuple = l_tuple
        self.nf_tuple = nf_tuple

    def parse(self):
        with open(self.path) as file:
            output = {}
            for line in file:
                if line.startswith('xm'):
                    tokens = line.split()
                    print(tokens)

                    name = tokens[0]

                    params = {}
                    pattern = re.compile(r'(\w+)\s*?=\s*?([\d.]+)')
                    for token in tokens[1:]:
                        match = pattern.match(token)
                        if match:
                            key = match.group(1)
                            value = match.group(2)
                            params[key] = value

                    output[name] = params

        return output

    # noinspection PyMethodMayBeStatic
    def replacer(self, regex, line, param):
        start = 0
        new_string = ''
        for match in re.finditer(regex, line):
            end, new_start = match.span(1)
            new_string += line[start:end] + param
            start = new_start
        new_string += line[start:]
        return new_string

    def modify_transistor_params(self, new_params:  dict[str, dict[str, str]]):
        # Read the original file
        with open(self.path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):

            for key, values in new_params.items():
                if self.w_tuple[0] >= float(values["w"]):
                    values["w"] = str(self.w_tuple[0])
                if self.w_tuple[1] <= float(values["w"]):
                    values["w"] = str(self.w_tuple[1])
                if self.nf_tuple[0] >= float(values["nf"]):
                    values["nf"] = str(self.nf_tuple[0])
                if self.nf_tuple[1] <= float(values["nf"]):
                    values["nf"] = str(self.nf_tuple[1])
                if self.l_tuple[0] >= float(values["l"]):
                    values["l"] = str(self.l_tuple[0])
                if self.l_tuple[1] <= float(values["l"]):
                    values["l"] = str(self.l_tuple[1])

            if line.startswith("xm"):
                name = line.split(' ', 1)[0]
                if name not in new_params:
                    continue
                line = self.replacer(r"w\s*?=\s*([\d.]+)", line, new_params[name]["w"])
                line = self.replacer(r"nf\s*?=\s*([\d.]+)", line, new_params[name]["nf"])
                line = self.replacer(r"l\s*?=\s*([\d.]+)", line, new_params[name]["l"])

            lines[i] = line

        with open(self.path, 'w') as f:
            f.writelines(lines)
