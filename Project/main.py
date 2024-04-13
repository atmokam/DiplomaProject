from QtWindow import MainWindow
from Application import Application

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    application = Application()

    mainWindow = MainWindow(application)
    mainWindow.show()

    sys.exit(app.exec_())