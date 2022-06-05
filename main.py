from PyQt5.Qt import *

from GUI.GameWindow import *
from GUI.StartWindow import *


def main():
    app = QApplication([])
    s = StartWindow()
    w = GameWindow(2)
    s.show()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
