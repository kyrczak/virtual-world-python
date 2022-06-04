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
                           "}")
        self.setText("*")
        self.clicked.connect(self.on_click)

    def on_click(self):
        print("dupa "+str(self.position.getX())+" "+str(self.position.getY()))
