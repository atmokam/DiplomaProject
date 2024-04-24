from MainWindow import MainWindow
from Application import Application

from CsvWriter import CsvWriter
from CsvParser import CsvParser

from Model import Model
from Trainer import Trainer

if __name__ == "__main__":
    # wr = CsvWriter("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/out.csv")

    # ntl = [{
    #     'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
    #     'xm2': {'w': 0.3, 'l': 0.4, 'nf': 2},
    #     'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3}
    # }, 
    # {
    #     'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
    #     'xm2': {'w': 0.3, 'l': 0.4, 'nf': 2},
    #     'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3}
    # }, 
    # {
    #     'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
    #     'xm2': {'w': 0.3, 'l': 0.4, 'nf': 2},
    #     'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3}
    # }]
    # fit = [1, 2, 3]

    # meas = [
    #     {'vds': 1, 'vgs': 2, 'id': 3},
    #     {'vds': 4, 'vgs': 5, 'id': 6},
    #     {'vds': 7, 'vgs': 8, 'id': 9}
    # ]

    # wr.write(ntl, fit, meas)

    # parser = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output copy.csv")

    # ntl, fit, meas = parser.parse()

    # print(ntl, fit, meas)

    

    # from PyQt5.QtWidgets import QApplication
    # import sys

    # app = QApplication(sys.argv)

    # application = Application()

    # mainWindow = MainWindow(application)
    # mainWindow.show()

    # sys.exit(app.exec_())

    


    trainer = Trainer("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output copy.csv")
    trainer.train(20, 10)
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
