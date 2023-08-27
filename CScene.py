from CCell import *
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QPoint, QSize, QLine, QRectF

class CScene:
    def __init__(self, window):
        self.scene = QGraphicsScene(window)
        self.view = QGraphicsView(self.scene)

        self.initScene()

        self.view.setScene(self.scene)
        window.setCentralWidget(self.view)

    def initScene(self):
        self.cells = []
        self.lines = []

        self.rows = 4
        self.cols = 4
        self.cellWidth = 100
        self.cellHeight = 100
        self.margin = 50

        for row in range(self.rows):
            for col in range(self.cols):
                pos = QPoint(col * self.cellWidth, row * self.cellHeight) + QPoint(self.margin, self.margin)
                size = QSize(self.cellWidth, self.cellHeight)
                rect = QRectF(pos.x(), pos.y(), size.width(), size.height())

                cell = CCell(rect)
                self.cells.append(cell)
                self.scene.addItem(cell)
        
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

    #def render(self):
    #    for cell in self.cells:
    #        cell.render()
    #    for line in self.lines:
    #        line.render()