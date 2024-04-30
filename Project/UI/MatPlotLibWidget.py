from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas


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
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Fitness value")
        ax.plot(data)
        self.canvas.draw()