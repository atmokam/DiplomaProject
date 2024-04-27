class Constraints:
    def __init__(self):
        self.netlist_constraints = {}
        self.measure_constraints = {}

    
    def calculate_measure_constraints(self, measures):
        meas_constr = {}
        for meas in measures:
            for key, val in meas.items():
                if key not in meas_constr:
                    meas_constr[key] = [val, val]
                else:
                    if val < meas_constr[key][0]:
                        meas_constr[key][0] = val
                    if val > meas_constr[key][1]:
                        meas_constr[key][1] = val

        return meas_constr
