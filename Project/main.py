from UI.MainWindow import MainWindow
from Application.Application import Application
from DataProcessing.CsvParser import CsvParser
from MainAlgorithm.Constraints import Constraints



if __name__ == "__main__":

    _, _, _measures = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/Project/files/output (3).csv").parse()

    constraints = Constraints()
    constraints.netlist_constraints = {
        'w': (0.2, 0.5),
        'l': (0.3, 1.05),
        'nf': (1, 4)
    }
    constraints.measure_constraints = constraints.calculate_measure_constraints(_measures)
    
    application = Application()
    application.generations = 200
    application.population = 10
    application.constraints = constraints
    application.spec = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/spec.txt"
    application.netlist = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/two_stage_opamp.sp"
    application.scales = {"pic": 10**-12, "pico": 10**-12, "nan": 10**-9, "nano": 10**-9, "0": 1, "kil": 10**3 , "kilo": 10**3, "meg": 10**6, "mega":  10**6}
    application.run()
























    
    # scaler = DataScaler(constraints)
    # for data, meas in zip(_ntl, _measures):
    #     scaler.scale_ntl(data)
    #     scaler.scale_meas(meas)



    # # trainer = Trainer(_ntl, _measures)
    
    # # trainer.train(400, 5)
    # # trainer.save("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/model.keras")
    # model = Model()
    # model.load("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/model.keras")

    # validation_ntl, _, validation_measures = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output (2).csv").parse()

    # for data, meas in zip(validation_ntl, validation_measures):
    #     scaler.scale_ntl(data)
    #     scaler.scale_meas(meas)
    

    # output_file_path = "/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output_file.txt"

    # with open(output_file_path, 'a') as file:
    #     for data, meas in zip(validation_ntl, validation_measures):
    #         prediction = model.predict(data)
    #         file.write(f"Prediction: {prediction}\nActual: {meas}\n")
    #         file.write("==============================================\n")



