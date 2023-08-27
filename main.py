from CWindow import *
from CBoard import *
from CButton import *
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CWindow("Soduku", 840, 50, 500, 500)
    #window.AddEntity(CBoard(window, 4, 4))

    window.show()

    # Run the event loop
    sys.exit(app.exec_())