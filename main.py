import sys
from PyQt5.Qt import *
from GUI.GameWindow import *
from GUI.StartWindow import *


def main():
    app = QApplication(sys.argv)
    s = StartWindow()
    s.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
