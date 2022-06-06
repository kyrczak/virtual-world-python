from PyQt5.Qt import *

from GUI.GameWindow import GameWindow
from GameLogic.Game import Game


class StartWindow(QWidget):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.layout = QVBoxLayout()

        self.width = QSlider(Qt.Horizontal)
        self.width_label = QLabel(f'Size: {self.width.value()}x{self.width.value()}')
        self.width_widget = QWidget()
        self.width_layout = QHBoxLayout()

        self.new_game_button = QPushButton("New game")
        self.load_game_button = QPushButton("Load game")
        self.button_layout = QHBoxLayout()
        self.button_widget = QWidget()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("Patryk Korczak - 188618 - Computer Science")

        self.width.setRange(10, 80)
        self.width.setValue(10)
        self.width_label.setText(f'Size: {self.width.value()}x{self.width.value()}')
        self.width_layout.addWidget(self.width_label)
        self.width_layout.addWidget(self.width)
        self.width_widget.setLayout(self.width_layout)

        self.button_layout.addWidget(self.new_game_button)
        self.button_layout.addWidget(self.load_game_button)
        self.button_widget.setLayout(self.button_layout)

        self.layout.addWidget(self.width_widget)
        self.layout.addWidget(self.button_widget)

        self.width.valueChanged.connect(lambda:
                                        self.width_label.setText(f'Size: {self.width.value()}x{self.width.value()}'))
        self.new_game_button.clicked.connect(lambda: self.start_game(self.width.value()))
        self.load_game_button.clicked.connect(lambda: self.load_game())

        self.setLayout(self.layout)
        self.setFixedSize(300, 150)

    # TODO Load Game
    def load_game(self):
        file_name = QFileDialog.getOpenFileName(self)
        print(file_name[0])
        self.close()
        game = Game()
        game.get_gui().show()
        game.load_game(file_name[0])

    def start_game(self, size):
        game = Game(size, size)
        self.close()
        game.get_gui().show()
