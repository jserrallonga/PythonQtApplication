from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class CWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('My Window')
        self.setGeometry(100, 100, 500, 500)

    def paintEvent(self, event):
        # Create a painter object
        painter = QPainter(self)

        # Set the rendering environment
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        painter.setPen(Qt.NoPen)

        # Draw a rectangle
        painter.drawRect(50, 50, 400, 400)