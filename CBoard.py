from CEntity import *

from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QPointF

class CCell:
    def __init__(self, x, y, isEven):
        self.x = x
        self.y = y
        self.isEven = isEven

class CBoard(CEntity):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.margin = 50

        self.cellWidth = 100
        self.cellHeight = 100
        
        self.color1 = QColor("#88ffff")
        self.color2 = QColor("#2255bb")

        self.cells = []
        for j in range (0, rows):
            for i in range (0, cols):
                isEvenCell = (i + j) % 2 == 0
                self.cells.append(CCell(i * self.cellWidth, j * self.cellHeight, isEvenCell))

    def Render(self, painter):
        for cell in self.cells:
            painter.setBrush(self.color1 if cell.isEven else self.color2)
            painter.drawRect(cell.x + self.margin, cell.y + self.margin, self.cellWidth, self.cellHeight)

        pen = QPen()
        pen.setWidth(3);
        painter.setPen(pen);
        
        y = self.rows * self.cellHeight + self.margin
        for x in range (self.margin, (self.cols + 1) * self.cellWidth + self.margin, self.cellWidth):
            painter.drawLine(QPointF(x, self.margin), QPointF(x, y))

        x = self.cols * self.cellWidth + self.margin
        for y in range (self.margin, (self.rows + 1) * self.cellHeight + self.margin, self.cellHeight):
            painter.drawLine(QPointF(self.margin, y), QPointF(x, y))



