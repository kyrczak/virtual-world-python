from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GameLogic.Systems import *


class TileButton(QPushButton):
    def __init__(self, point, game):
        super(TileButton, self).__init__()
        self.position = point
        self.game = game
        self.setStyleSheet("QPushButton {"
                           "border-style: none;"
                           "background-color: white;"
                           "}")
        self.setText("*")
        self.clicked.connect(self.on_click)
        self.setToolTip(str(self.position))

    # TODO Adding organisms
    def on_click(self):
        print(self.position)

    def get_position(self):
        return self.position

    def get_game(self):
        return self.game
