from PyQt5.QtCore import *
from PyQt5.Qt import *
from GUI.GameBoardPanel import GameBoardPanel
from GUI.JournalPanel import JournalPanel
from GUI.MenuPanel import MenuPanel
from GameLogic.Systems.Keys import Keys


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
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setLayout(self.layout)

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key_Up:
                self.get_game().get_world().set_key(Keys.UP)
                self.get_game().game_next_turn()
            case Qt.Key_Down:
                self.get_game().get_world().set_key(Keys.DOWN)
                self.get_game().game_next_turn()
            case Qt.Key_Left:
                self.get_game().get_world().set_key(Keys.LEFT)
                self.get_game().game_next_turn()
            case Qt.Key_Right:
                self.get_game().get_world().set_key(Keys.RIGHT)
                self.get_game().game_next_turn()
            case Qt.Key_F:
                self.get_game().get_world().set_key(Keys.KEY_F)
                self.get_game().game_next_turn()

    def get_journal_panel(self):
        return self.journal

    def get_tiles(self):
        return self.game_board.children()

    def get_game(self):
        return self.game
