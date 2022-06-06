from PyQt5.QtGui import QColor

from GameLogic.Organism import Organism
from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point
from GameLogic.World import World


class Belladonna(Plant):
    def __int__(self, position: Point, world: World, power=99, age=0):
        super(Belladonna, self).__init__(position, power, age, world)

    def get_sign(self):
        return 'b'

    def get_name(self):
        return "Belladonna"

    def get_color(self):
        return QColor(0x131670)

    def create_organism(self, position, world):
        self.get_world().add_organism(Belladonna(position, world))

    def collision(self, attacker: Organism):
        attacker.set_alive(False)
        self.get_world().add_activity("Belladonna killed " + attacker.get_name())
        return self.fight(attacker)