from PyQt5.QtWidgets import QMainWindow, QTextEdit, QHBoxLayout, QWidget
from UI.MatPlotLibWidget import MPLWidget


class ResultWindow(QMainWindow):
    def __init__(self, result, data):
        super().__init__()
        self.setWindowTitle("Result Window")

        self.textEdit = QTextEdit()
        self.textEdit.setText(f"Result:\n{str(result)}")
        self.textEdit.setFixedSize(470, 480)

        self.graph = MPLWidget()
        self.graph.setFixedSize(510, 500)
        self.graph.plot(data)

        layout = QHBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.graph)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)