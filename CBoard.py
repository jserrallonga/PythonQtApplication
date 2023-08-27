from CEntity import *
from CCell import *
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QPoint, QSize, QLine

class CBoard(CEntity):
    def __init__(self, window, cols, rows):
        self.window = window
        self.cols = cols
        self.rows = rows
        
        self.margin = 50
        self.cellWidth = 100
        self.cellHeight = 100
        #self.cellColor = QColor(200, 200, 200)
        
        self.cells = []
        self.lines = []

        self.init()

    def init(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pos = QPoint(col * self.cellWidth, row * self.cellHeight) + QPoint(self.margin, self.margin)
                size = QSize(self.cellWidth, self.cellHeight)
                #self.cells.append(CCell(self.window, pos, size))
        
        # Vertical lines
        y = self.rows * self.cellHeight + self.margin
        for vLine in range(self.cols + 1):
            x = vLine * self.cellWidth + self.margin
            self.lines.append(QLine(x, self.margin, x, y))

        # Horitzontal lines
        x = self.cols * self.cellWidth + self.margin
        for hLine in range(self.rows + 1):
            y = hLine * self.cellHeight + self.margin
            self.lines.append(QLine(self.margin, y, x, y))

    def renderCells(self, painter):
        for cell in self.cells:
            cell.render(painter)

    def renderLines(self, painter):
        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(3)
        painter.setPen(pen)

        for line in self.lines:
            painter.drawLine(line)


        #y = self.rows * self.cellHeight + self.margin
        #for x in range (self.margin, (self.cols + 1) * self.cellWidth + self.margin, self.cellWidth * 2):
        #    painter.drawLine(QPoint(x, self.margin), QPoint(x, y))
        #    print("VLine: x = " + str(x))

        #x = self.cols * self.cellWidth + self.margin
        #for y in range (self.margin, (self.rows + 1) * self.cellHeight + self.margin, self.cellHeight * 2):
        #    painter.drawLine(QPoint(self.margin, y), QPoint(x, y))
        #    print("HLine: y = " + str(y))


    def render(self, painter):
        #self.renderCells(painter)
        self.renderLines(painter)