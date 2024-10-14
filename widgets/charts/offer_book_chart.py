from .mpl_canvas import MplCanvas
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QRadioButton
import typing

class OfferBookChart(QWidget):
    def __init__(self, parent: typing.Optional[QWidget] = ...) -> None:
        super().__init__(parent)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        
    def updatePlot(self, xdata, ydata):
        self.canvas.axes.clear()
        self.canvas.axes.plot(xdata, ydata, 'r')
        self.canvas.draw()