from CEntity import *
from PyQt5.QtWidgets import QPushButton

class CButton(CEntity):
    def __init__(self, window):
        self.button = QPushButton("", window)
        self.button.setGeometry(100, 100, 30, 30)

        self.button.setStyleSheet(
        """
        QPushButton {
            background-color: #2244cc;
            color: white;
            border: none;
            border-radius: 15px;
        }
		            
        QPushButton:hover {
            background-color: #4466cc;
        }

        QPushButton:pressed {
            background-color: #1133aa;
        }
        """
        )

        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button Clicked")