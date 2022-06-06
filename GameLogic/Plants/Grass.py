from PyQt5.QtGui import QColor

from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point


class Grass(Plant):
    def __int__(self, position: Point, world, power=0, age=0):
        super(Grass, self).__init__(position, power, age, world)

    def get_sign(self):
        return 'g'

    def get_name(self):
        return "Grass"

    def get_color(self):
        return QColor(0x00ff00)

    def create_organism(self, position, world):
        self.get_world().add_organism(Grass(position, world))
