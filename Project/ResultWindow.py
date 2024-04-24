from PyQt5.QtWidgets import QMainWindow, QTextEdit, QHBoxLayout, QWidget
from MatPlotLibWidget import MPLWidget


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