from MainWindow import MainWindow
from Application import Application

from CsvWriter import CsvWriter
from CsvParser import CsvParser

from Model import Model
from Trainer import Trainer

from DataScaler import DataScaler


def calculate_measure_constraints(measures): # shouldnt be here
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

    print(meas_constr)
    return meas_constr


if __name__ == "__main__":

    _ntl, _, _measures = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output (3).csv").parse()
    
    ntl_constraints = {
        'w': (0.2, 0.5),
        'l': (0.3, 1.05),
        'nf': (1, 4)
    }

    meas_constr = calculate_measure_constraints(_measures)

    scaler = DataScaler(ntl_constraints, meas_constr)
    for data, meas in zip(_ntl, _measures):
        scaler.scale(data, meas)


    trainer = Trainer(_ntl, _measures)
    
    trainer.train(400, 10)
    trainer.save("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/model.keras")
    model = trainer.get_trained_model()

    
    print(model.predict({
        'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
        'xm2': {'w':0.3, 'l': 0.4, 'nf': 2},
        'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3},
        'xm14': {'w': 0.2, 'l': 0.3, 'nf': 1},
        'xm24': {'w':0.3, 'l': 0.4, 'nf': 2},
        'xm34': {'w': 0.4, 'l': 0.5, 'nf': 3},
        'xm11': {'w': 0.2, 'l': 0.3, 'nf': 1},
        'xm21': {'w':0.3, 'l': 0.4, 'nf': 2},
        'xm31': {'w': 0.4, 'l': 0.5, 'nf': 3}
    }))

