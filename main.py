from CWindow import *
from CBoard import *
from CButton import *
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CWindow("Soduku", 500, 50, 550, 550)
    window.AddEntity(CBoard(9, 9))
    #window.AddEntity(CButton(window))

    window.show()

    # Run the event loop
    sys.exit(app.exec_())