from CWindow import *
from CBoard import *
from CButton import *

from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CWindow("MyWindow", 200, 200, 500, 500)
    window.AddEntity(CBoard())
    window.AddEntity(CButton(window))

    window.show()

    # Run the event loop
    sys.exit(app.exec_())