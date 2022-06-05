from PyQt5.QtCore import *
from PyQt5.Qt import *
from GUI.GameBoardPanel import GameBoardPanel
from GUI.JournalPanel import JournalPanel
from GUI.MenuPanel import MenuPanel


class GameWindow(QWidget):
    def __init__(self, game):
        super(GameWindow, self).__init__()
        self.game = game
        self.layout = QVBoxLayout()
        self.menu_panel = MenuPanel(self.game)
        self.journal = JournalPanel(self.game)
        self.game_board = GameBoardPanel(self.game)
        self.set_ui()

    def set_ui(self):
        self.setFixedSize(800, 800)
        self.setWindowTitle("Virtual World")

        self.game_board.setFixedSize(650, 650)
        self.journal.setFixedHeight(100)
        self.layout.addWidget(self.menu_panel, 0, Qt.AlignTop)
        self.layout.addWidget(self.game_board, 0, Qt.AlignCenter)
        self.layout.addWidget(self.journal, 0, Qt.AlignBottom)

        self.setLayout(self.layout)

    # TODO KeyPressEvent
    def keyPressEvent(self, event):
        return

    def get_tiles(self):
        return self.game_board.chi
    def get_game(self):
        return self.game
