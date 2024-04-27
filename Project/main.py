from MainWindow import MainWindow
from Application import Application

from CsvWriter import CsvWriter
from CsvParser import CsvParser

from Model import Model
from Trainer import Trainer

from DataScaler import DataScaler

from Constraints import Constraints



if __name__ == "__main__":

    _ntl, _, _measures = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/Project/files/output (3).csv").parse()


    constraints = Constraints()
    constraints.netlist_constraints = {
        'w': (0.2, 0.5),
        'l': (0.3, 1.05),
        'nf': (1, 4)
    }
    constraints.measure_constraints = constraints.calculate_measure_constraints(_measures)


    scaler = DataScaler(constraints)
    for data, meas in zip(_ntl, _measures):
        scaler.scale(data, meas)


    # trainer = Trainer(_ntl, _measures)
    
    # trainer.train(400, 5)
    # trainer.save("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/model.keras")
    model = Model()
    model.load("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/Project/files/model_loss00018.keras")

    validation_ntl, _, validation_measures = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output (2).csv").parse()

    for data, meas in zip(validation_ntl, validation_measures):
        scaler.scale(data, meas)
    

    for data, meas in zip(validation_ntl, validation_measures):
        print(model.predict(data), meas)