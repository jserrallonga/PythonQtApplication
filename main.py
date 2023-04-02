from PyQt5.QtWidgets import QApplication
from CWindow import CWindow
import sys

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the window instance
    window = CWindow()

    # Show the window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())