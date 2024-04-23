from QtWindow import MainWindow
from Application import Application

from CsvWriter import CsvWriter
from CsvParser import CsvParser

if __name__ == "__main__":
    wr = CsvWriter("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/out.csv")

    ntl = [{
        'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
        'xm2': {'w': 0.3, 'l': 0.4, 'nf': 2},
        'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3}
    }, 
    {
        'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
        'xm2': {'w': 0.3, 'l': 0.4, 'nf': 2},
        'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3}
    }, 
    {
        'xm1': {'w': 0.2, 'l': 0.3, 'nf': 1},
        'xm2': {'w': 0.3, 'l': 0.4, 'nf': 2},
        'xm3': {'w': 0.4, 'l': 0.5, 'nf': 3}
    }]
    fit = [1, 2, 3]

    meas = [
        {'vds': 1, 'vgs': 2, 'id': 3},
        {'vds': 4, 'vgs': 5, 'id': 6},
        {'vds': 7, 'vgs': 8, 'id': 9}
    ]

    wr.write(ntl, fit, meas)

    parser = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/out.csv")

    ntl, fit, meas = parser.parse()

    print(ntl, fit, meas)

    

    # from PyQt5.QtWidgets import QApplication
    # import sys

    # app = QApplication(sys.argv)

    # application = Application()

    # mainWindow = MainWindow(application)
    # mainWindow.show()

    # sys.exit(app.exec_())