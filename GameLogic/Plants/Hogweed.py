from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal
import GameLogic.Animals.Cybersheep
from GameLogic.Organism import Organism
from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point


class Hogweed(Plant):
    def __int__(self, position: Point, world, power=10, age=0):
        super(Hogweed, self).__init__(position, power, age, world)

    def get_sign(self):
        return 'h'

    def get_name(self):
        return "Hogweed"

    def get_color(self):
        return QColor(0xff00ff)

    def create_organism(self, position, world):
        self.get_world().add_organism(Hogweed(position, world))

    def action(self):
        self.kill_around()
        self.grow()
        self.set_age(self.get_age() + 1)

    def collision(self, attacker: Organism):
        if isinstance(attacker,GameLogic.Animals.Cybersheep.Cybersheep):
            self.set_alive(False)
            self.get_world().add_activity("Cybersheep killed Hogweed")
            return True
        else:
            attacker.set_alive(False)
            return False

    def kill_around(self):
        positions_around = [
            Point(self.get_position().get_x(), self.get_position().get_y()-1),
            Point(self.get_position().get_x(), self.get_position().get_y()+1),
            Point(self.get_position().get_x()+1, self.get_position().get_y()),
            Point(self.get_position().get_x()-1, self.get_position().get_y())
        ]
        for position in positions_around:
            organism = self.get_world().get_organism(position)
            if organism is not None and self.is_in_bounds(position):
                if self.is_animal(organism) and isinstance(organism, GameLogic.Animals.Cybersheep.Cybersheep) is False:
                    organism.set_alive(False)

    def is_animal(self, organism: Organism):
        return isinstance(organism, Animal)
