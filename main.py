from PyQt5.Qt import *

from GUI.GameBoardPanel import GameBoardPanel
from GUI.JournalPanel import JournalPanel
from GUI.TileButton import *
from GUI.MenuPanel import *
from GameLogic.Game import Game
from GameLogic.Systems.Point import Point


def main():
    app = QApplication([])
    window = QWidget()
    window.setFixedSize(800, 800)
    window.setWindowTitle("Virtual World")
    game = Game()
    layout = QVBoxLayout()
    menu_panel = MenuPanel(game)
    journal = JournalPanel(game)
    game_board = GameBoardPanel(game)
    game_board.setFixedSize(650,650)
    journal.setFixedHeight(100)
    layout.addWidget(menu_panel, 0, Qt.AlignTop)
    layout.addWidget(game_board, 0, Qt.AlignCenter)
    layout.addWidget(journal, 0, Qt.AlignBottom)

    window.setLayout(layout)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
