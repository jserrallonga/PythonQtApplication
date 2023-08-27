from CScene import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter

class CWindow(QMainWindow):
    def __init__(self, title, x, y, width, height):
        super().__init__()

        self.scene = CScene(self) #QGraphicsScene(self)
        
        self.setWindowTitle(title)
        self.setGeometry(x, y, width, height)

    def paintEvent(self, event):
        #self.scene.render()
        print("Finish paintEvent\n");
