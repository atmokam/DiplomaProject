import re


class SpecParser:
    def __init__(self, path):
        self.path = path

    def parse_specs(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()

        result = {}
        pattern = re.compile(r"^[\s]*([\w\-]+)\s+([\d\-]+)\s+([\d\-]+)\s+([\w\-]+)\s+([\w\-]+)\s+\{([\s\w\-]+)}")
        for line in lines:
            match = pattern.search(line)
            if match:
                param_name = match.group(1)
                spec_lo = match.group(2)
                spec_hi = match.group(3)
                scale = match.group(4)
                unit = match.group(5)
                description = match.group(6)

                result[param_name] = {}
                result[param_name]["SpecLo"] = spec_lo
                result[param_name]["SpecHi"] = spec_hi
                result[param_name]["Scale"] = scale
                result[param_name]["Unit"] = unit
                result[param_name]["descr"] = description

        return result
        