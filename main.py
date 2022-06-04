from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from GUI.GameBoardPanel import GameBoardPanel
from GUI.TileButton import *
from GameLogic.Systems.Point import Point

def main():
    app = QApplication([])
    window = QWidget()
    # window.setGeometry(100, 100, 500, 500)
    window.setFixedSize(800,800)
    window.setWindowTitle("Virtual World")

    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)
    label = QLabel("Press the button below")
    button = TileButton(Point(5, 5), 2)
    gameBoard = GameBoardPanel(2)
    gameBoard.setFixedSize(600, 600)
    layout.addWidget(label)
    layout.addWidget(gameBoard)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
