from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from GUI.OrganismsMenu import OrganismsMenu
from GameLogic.Systems import *


class TileButton(QPushButton):
    def __init__(self, point, game):
        super(TileButton, self).__init__()
        self.position = point
        self.game = game
        self.color = QColor(0xFFFFFF)
        self.window = None
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setStyleSheet("QPushButton {"
                           "border: 1px solid lightgray;"
                           f'background-color: rgb({self.color.red()}, {self.color.green()}, {self.color.blue()});'
                           "}")
        self.setText(" ")
        self.clicked.connect(self.on_click)
        self.setToolTip(str(self.position))

    # TODO Adding organisms
    def on_click(self):
        print(self.position)
        if self.get_game().get_world().get_organism(self.position) is None:
            self.window = OrganismsMenu(self.position, self.game)

    def get_position(self):
        return self.position

    def get_game(self):
        return self.game

    def clear_style(self):
        self.setStyleSheet("QPushButton {"
                           "border: 1px solid lightgray;"
                           f'background-color: rgb({self.color.red()}, {self.color.green()}, {self.color.blue()});'
                           "}")

    def set_style(self, color: QColor):
        self.setStyleSheet("QPushButton {"
                           "border: 1px solid lightgray;"
                           f'background-color: rgb({color.red()}, {color.green()}, {color.blue()});'
                           "}")