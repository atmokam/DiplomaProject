

class DataScaler:
    def __init__(self, constraints):
        self.ntl_constraints = constraints.netlist_constraints
        self.meas_constraints = constraints.measure_constraints
        
    def scale_ntl(self, netlist):
        for val in netlist.values():
            for key, constraint in self.ntl_constraints.items():
                atkey = val.get(key)
                if atkey > 1:
                    val[key] = (atkey - constraint[0]) / (constraint[1] - constraint[0])

    def scale_meas(self, measure):
        for key, val in measure.items():
            constraint = self.meas_constraints.get(key)
            if constraint[0] != constraint[1]:
                measure[key] = (val - constraint[0]) / (constraint[1] - constraint[0])
            else:
                measure[key] = 0.0

    def unscale_meas(self, measure):
        for key, val in measure.items():
            constraint = self.meas_constraints.get(key)
            measure[key] = val * (constraint[1] - constraint[0]) + constraint[0]
        
