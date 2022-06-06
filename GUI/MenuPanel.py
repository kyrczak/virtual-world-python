from PyQt5.QtGui import *
from PyQt5.Qt import *

import GameLogic.Game


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

        self.next_turn_button.clicked.connect(lambda: self.game.game_next_turn())
        self.save_game_button.clicked.connect(self.save_function)
        self.load_game_button.clicked.connect(self.load_game)

        self.next_turn_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.save_game_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.load_game_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.layout.addWidget(self.next_turn_button, 1)
        self.layout.addWidget(self.save_game_button, 1)
        self.layout.addWidget(self.load_game_button, 1)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setLayout(self.layout)

    def button_click(self):
        print("test")

    def save_function(self):
        panel = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Please input save file name")
        textbot = QLineEdit()
        save_button = QPushButton("Save")

        layout.addWidget(label)
        layout.addWidget(textbot)
        layout.addWidget(save_button)

        save_button.clicked.connect(lambda: self.save_game(textbot.text(), panel))
        panel.setLayout(layout)
        panel.show()

    def load_game(self):
        file_name = QFileDialog.getOpenFileName(self)
        print(file_name[0])
        self.game.get_gui().close()
        self.game = GameLogic.Game.Game()
        self.game.load_game(file_name[0])

    def save_game(self, text, panel):
        self.game.save_game(text)
        print(text)
        panel.close()