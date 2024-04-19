from QtWindow import MainWindow
from Application import Application

from CsvParser import CsvParser

if __name__ == "__main__":
    parser = CsvParser("/home/atmokam/Desktop/DiplomaProject/DiplomaProject/sim/output.csv")

    ntl_list, fitnesses, measures_data = parser.parse()

    print(ntl_list, fitnesses, measures_data)
    # from PyQt5.QtWidgets import QApplication
    # import sys

    # app = QApplication(sys.argv)

    # application = Application()

    # mainWindow = MainWindow(application)
    # mainWindow.show()

    # sys.exit(app.exec_())