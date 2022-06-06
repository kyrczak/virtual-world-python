from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

from GUI.TileButton import TileButton
from GameLogic.Systems.Point import Point


class GameBoardPanel(QWidget):
    def __init__(self, game):
        super(GameBoardPanel, self).__init__()
        self.game = game
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.size = game.get_world().get_height()

        for i in range(self.size):
            for j in range(self.size):
                button = TileButton(Point(j, i), self.game)
                button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
                self.layout.addWidget(button, i, j)

        self.setLayout(self.layout)
