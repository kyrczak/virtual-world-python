from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from GUI.TileButton import TileButton
from GameLogic.Systems.Point import Point


class GameBoardPanel(QWidget):
    def __init__(self, game):
        super(GameBoardPanel, self).__init__()
        self.game = game
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        for i in range(80):
            for j in range(80):
                button = TileButton(Point(j, i), self.game)
                self.layout.addWidget(button, i, j)

        self.setLayout(self.layout)