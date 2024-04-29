import re

class ConstraintsParser:
    def parse(self, constraints : str):
        pattern = "(\w+?)\s*?:\s*?(\d+?)\s*?(\d+?)"
        regex = re.compile(pattern)
        param_constraints = {}
        for match in regex.finditer(constraints):
            param_constraints[match.group(1)] = (float(match.group(2)), float(match.group(3)))

        return param_constraints
