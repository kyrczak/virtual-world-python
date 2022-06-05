from PyQt5.QtGui import *
from PyQt5.Qt import *


class MenuPanel(QWidget):
    def __init__(self, game):
        super(MenuPanel, self).__init__()
        self.game = game
        self.next_turn_button = QPushButton("Next turn")
        self.save_game_button = QPushButton("Save game")
        self.load_game_button = QPushButton("Load game")
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignHCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.next_turn_button.clicked.connect(self.button_click)
        self.save_game_button.clicked.connect(self.button_click)
        self.load_game_button.clicked.connect(self.button_click)

        self.layout.addWidget(self.next_turn_button, 1)
        self.layout.addWidget(self.save_game_button, 1)
        self.layout.addWidget(self.load_game_button, 1)

        self.setLayout(self.layout)

    def button_click(self):
        print("test")

    # TODO Next turn
    #  Save game
    #  Load game
