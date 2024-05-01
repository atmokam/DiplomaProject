import re
from MainAlgorithm.Constraints import Constraints

class ConstraintsParser:
    def parse(self, constraints : str):
        pattern = "(\w+?)\s*?:\s*?(\d+\.*\d*)\s+?(\d+\.*\d*)"
        regex = re.compile(pattern)
        param_constraints = {}
        for match in regex.finditer(constraints):
            param_constraints[match.group(1)] = (float(match.group(2)), float(match.group(3)))

        result = Constraints()
        result.netlist_constraints = param_constraints
        return result