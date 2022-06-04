from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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
        self.journal.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc rutrum risus id ipsum gravida, quis lacinia urna pretium. Vestibulum sagittis eget ipsum vel pulvinar. Praesent porttitor, lorem ut egestas semper, metus urna imperdiet felis, eget porttitor turpis tortor vitae odio. Vestibulum auctor nulla dui, sit amet pulvinar lorem aliquam ut. Suspendisse lacinia diam elit, sed euismod velit eleifend euismod. Donec gravida vel libero id elementum. Donec a eleifend odio. Nulla ultrices mollis purus, eu ullamcorper justo mollis a. Cras ultricies sit amet est nec mollis. Phasellus accumsan urna sed erat aliquet, a interdum enim consectetur. Cras aliquet posuere diam et malesuada. Aliquam ut nisl convallis nulla rhoncus efficitur quis quis lacus. Fusce eu nunc imperdiet, ullamcorper dolor a, vestibulum neque.")
        self.setLayout(self.layout)