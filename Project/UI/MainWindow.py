from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLineEdit
from UI.ResultWindow import ResultWindow
from DataProcessing.ConstraintsParser import ConstraintsParser


class MainWindow(QMainWindow):
    def __init__(self, application_ref):
        super().__init__()
        self.setWindowTitle("Sizing Tool")

        self.application_ref = application_ref  

        self.label1 = QLabel()
        self.label2 = QLabel()
        self.button1 = QPushButton("Choose Netlist File")
        self.button1.clicked.connect(self.openFileDialog1)
        self.button2 = QPushButton("Choose Specification File")
        self.button2.clicked.connect(self.openFileDialog2)

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("Number of generations")
        self.lineEdit1.editingFinished.connect(lambda: setattr(self.application_ref, 'generations', int(self.lineEdit1.text())))

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Number of individuals")
        self.lineEdit2.editingFinished.connect(lambda: setattr(self.application_ref, 'population', int(self.lineEdit2.text())))


        self.param_constraints = QLineEdit()
        self.param_constraints.setPlaceholderText("Parameter constraints")
        parser = ConstraintsParser()
        self.param_constraints.editingFinished.connect(lambda: setattr(self.application_ref, 'constraints', parser.parse(self.param_constraints.text())))

        self.buttonRun = QPushButton("Generate")
        self.buttonRun.clicked.connect(self.runFunction)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.label1)
        layout.addWidget(self.button2)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.param_constraints)
        layout.addWidget(self.buttonRun)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def openFileDialog1(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if fileName:
            self.label1.setText(fileName)
            self.application_ref.netlist = fileName

    def openFileDialog2(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if fileName:
            self.label2.setText(fileName)
            self.application_ref.spec = fileName
      


    def runFunction(self): # sample for now
        result, fitnesses = self.application_ref.run()
        
        self.result_window = ResultWindow(result, fitnesses)
        self.result_window.show()

