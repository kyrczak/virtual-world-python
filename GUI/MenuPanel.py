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

        self.next_turn_button.clicked.connect(lambda: self.game.game_next_turn())
        self.save_game_button.clicked.connect(self.save_function)
        self.load_game_button.clicked.connect(self.button_click)

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

    def save_game(self, text, panel):
        self.game.save_game(text)
        print(text)
        panel.close()
    # TODO Save game
    #  Load game
