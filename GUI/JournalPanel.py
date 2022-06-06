import PyQt5.QtWidgets
import PyQt5.QtCore
from PyQt5.QtGui import *
from PyQt5.Qt import *


class JournalPanel(QWidget):
    def __init__(self, game):
        super(JournalPanel, self).__init__()
        self.game = game
        self.journal = QTextEdit()
        self.journal.setReadOnly(True)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.journal)
        self.journal.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setLayout(self.layout)

    def set_journal_activities(self):
        self.journal.setText("")
        for string in self.game.get_world().get_journal():
            self.journal.append(string + "\n")
        self.game.get_world().get_journal().clear()