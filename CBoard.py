from CEntity import *
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QPointF

class CBoard(CEntity):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.margin = 50

        self.cellWidth = 100
        self.cellHeight = 100
        self.cellColor = QColor(200, 200, 200)

    def RenderCells(self, painter):
        painter.setBrush(QBrush(self.cellColor))
        
        for y in range(self.margin, self.rows * self.cellHeight + self.margin, self.cellHeight):
            for x in range(self.margin, self.cols * self.cellWidth + self.margin, self.cellWidth):
                painter.drawRect(x, y, self.cellWidth, self.cellHeight)

    def RenderLines(self, painter):
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        y = self.rows * self.cellHeight + self.margin
        for x in range (self.margin, (self.cols + 1) * self.cellWidth + self.margin, self.cellWidth * 2):
            painter.drawLine(QPointF(x, self.margin), QPointF(x, y))

        x = self.cols * self.cellWidth + self.margin
        for y in range (self.margin, (self.rows + 1) * self.cellHeight + self.margin, self.cellHeight * 2):
            painter.drawLine(QPointF(self.margin, y), QPointF(x, y))

    def Render(self, painter):
        self.RenderCells(painter)
        self.RenderLines(painter)