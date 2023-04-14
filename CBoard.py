from CEntity import *

from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QPointF

class CBoard(CEntity):
    def Render(self, painter):
        # Set the rendering environment
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(QColor(255, 0, 0)))

        painter.drawRect(50, 50, 400, 400)

        pen = QPen()
        pen.setWidth(3);

        painter.setPen(pen);
        
        for x in range(0, 5):
            painter.drawLine(QPointF(50 + x * 100, 50), QPointF(50 + x * 100, 450))

        for y in range(0, 5):
            painter.drawLine(QPointF(50, 50 + y * 100), QPointF(450, 50 + y * 100))
            


