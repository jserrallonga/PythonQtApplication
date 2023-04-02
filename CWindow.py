from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QPointF

class CWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('My Window')
        self.width = 500
        self.height = 500

        self.setGeometry(200, 200, self.width, self.height)

    def paintEvent(self, event):
        # Create a painter object
        painter = QPainter(self)

        # Set the rendering environment
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(QColor(255, 0, 0)))

        # Draw a rectangle
        painter.drawRect(50, 50, 400, 400)

        pen = QPen()
        pen.setWidth(3);

        painter.setPen(pen);
        
        for x in range(0, 5):
            painter.drawLine(QPointF(50 + x * 100, 50), QPointF(50 + x * 100, 450))

        for y in range(0, 5):
            painter.drawLine(QPointF(50, 50 + y * 100), QPointF(450, 50 + y * 100))