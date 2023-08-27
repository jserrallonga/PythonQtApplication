#from PyQt5.QtCore import QPointF
#from PyQt5.QtWidgets import QPushButton

from CEntity import *
from PyQt5.QtCore import Qt, QPoint, QSize, QRect
from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QPainter

class CCell(QGraphicsRectItem):
    def __init__(self, rect, parent=None):
        super().__init__(rect, parent)
        self.setFlag(self.ItemIsSelectable)

    def mousePressEvent(self, event):
        if self.isSelected():
            print("Item clicked:", self.rect())

    #def render(self, painter):
    #    painter.drawRect(self.rect)
