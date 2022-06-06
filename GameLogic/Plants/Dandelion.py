import secrets

from PyQt5.QtGui import QColor

from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point


class Dandelion(Plant):
    def __int__(self, position: Point, world, power=0, age=0):
        super(Dandelion, self).__init__(position, power, age, world)

    def get_sign(self):
        return 'd'

    def get_name(self):
        return "Dandelion"

    def get_color(self):
        return QColor(0xfff203)

    def create_organism(self, position, world):
        self.get_world().add_organism(Dandelion(position, world))

    def grow(self):
        for i in range(3):
            chance = secrets.randbelow(self.growth_rate)
            if chance == 0:
                self.reproduce()