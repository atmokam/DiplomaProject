from PyQt5.QtWidgets import QLabel, QFileDialog, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMainWindow

class ResultWindow(QMainWindow):
    def __init__(self, result):
        super().__init__()
        self.setWindowTitle("Result Window")

        self.textEdit = QTextEdit()
        self.textEdit.setText(result)

        self.setCentralWidget(self.textEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sizing Tool")

        self.button1 = QPushButton("Choose File 1")
        self.button1.clicked.connect(self.openFileDialog1)
        self.label1 = QLabel()
        self.button2 = QPushButton("Choose File 2")
        self.button2.clicked.connect(self.openFileDialog2)
        self.label2 = QLabel()
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("Number of generations")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Number of individuals")
        self.buttonRun = QPushButton("Run Function")
        self.buttonRun.clicked.connect(self.runFunction)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.label1)
        layout.addWidget(self.button2)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.buttonRun)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def openFileDialog1(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if fileName:
            self.label1.setText(fileName)

    def openFileDialog2(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if fileName:
            self.label2.setText(fileName)


    def runFunction(self):
        # Replace this with your actual function
        result = "Result of function"

        self.resultWindow = ResultWindow(result)
        self.resultWindow.show()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())