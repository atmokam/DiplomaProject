from PyQt5.QtWidgets import QLabel, QFileDialog, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QMainWindow
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MPLWidget(QWidget):
    def __init__(self, parent=None):
        super(MPLWidget, self).__init__(parent)

        self.figure = Figure(figsize=(2, 2))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self, data):
        ax = self.figure.add_subplot(111)
        ax.plot(data)
        self.canvas.draw()

class ResultWindow(QMainWindow):
    def __init__(self, result, data):
        super().__init__()
        self.setWindowTitle("Result Window")

        self.textEdit = QTextEdit()
        self.textEdit.setText(result)
        self.textEdit.setFixedSize(500, 500)

        self.graph = MPLWidget()
        self.graph.setFixedSize(500, 500)
        self.graph.plot(data)

        layout = QHBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.graph)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

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
        self.param_constraints.editingFinished.connect(lambda: self.application_ref.parameter_constraints(self.param_constraints.text()))

        self.buttonRun = QPushButton("Run Simulation")
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
        result = """Best individual:

xm13 net23 net23 vdd vdd p25 w=0.3u l=0.44u nf=5 m=1
xm16 out   net22 vdd vdd p25 w=0.3u l=0.44u nf=5 m=1
xm15 net41 net41 vdd vdd p25 w=0.32u l=0.42u nf=1 m=1
xm14 net22 net23 vdd vdd p25 w=0.32u l=0.42u nf=3 m=1
xm12 net41 net41 vss vss n25 w=0.32u l=0.55u nf=1 m=1
xm10 net15 net41 vss vss n25 w=0.67u l=0.42u nf=1 m=1
xm9  net22 inp net15 vss n25 w=0.32u l=0.42u nf=1 m=1
xm17 net23 inm net15 vss n25 w=0.32u l=0.42u nf=1 m=1
xm11 out   net41 vss vss n25 w=0.86u l=1.03u nf=1 m=1
"""
        data = [-1.5 , -1.3, -1.2, 0.5, 1.3, 2.2, 3.5, 4] 
        self.result_window = ResultWindow(result, data)
        self.result_window.show()

