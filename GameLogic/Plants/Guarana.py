from PyQt5.QtGui import QColor

from GameLogic.Organism import Organism
from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point
from GameLogic.World import World


class Guarana(Plant):
    fruit_power = 3

    def __int__(self, position: Point, world: World, power=0, age=0):
        super(Guarana, self).__init__(position, power, age, world)

    def get_sign(self):
        return '@'

    def get_name(self):
        return "Guarana"

    def get_color(self):
        return QColor(0x651F45)

    def create_organism(self, position, world):
        self.get_world().add_organism(Guarana(position, world))

    def collision(self, attacker: Organism):
        attacker.set_power(attacker.get_power() + self.fruit_power)
        self.get_world().add_activity("Organism " + attacker.get_name() + " ate guaranna fruit")
        return self.fight(attacker)
