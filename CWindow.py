from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter

class CWindow(QWidget):
    def __init__(self, title, x, y, width, height):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(x, y, width, height)
        self.entities = []

    def AddEntity(self, entity):
        self.entities.append(entity)

    def paintEvent(self, event):
        painter = QPainter(self)

        for entity in self.entities:
            entity.Render(painter)

        print("Finish paintEvent\n");
