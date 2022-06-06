import random
import secrets

from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal
from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point


class Antelope(Animal):
    def __init__(self, position, world, power=4, initiative=4, age=0):
        super(Antelope, self).__init__(position, power, initiative, age, world)

    def get_sign(self):
        return 'A'

    def get_name(self):
        return "Antelope"

    def get_color(self):
        return QColor(0x963700)

    def is_same_species(self, other):
        return isinstance(other, Antelope)

    def create_organism(self, position, world):
        self.get_world().add_organism(Antelope(position, world))

    def move(self):
        direction = secrets.randbelow(8)
        proposed_position = self.proposed_position(direction)
        if self.is_in_bounds(proposed_position):
            organism = self.get_world().get_organism(proposed_position)
            if organism is None:
                self.set_position(proposed_position)
            elif self.is_same_species(organism):
                self.reproduce()
            else:
                if organism.collision(self):
                    if isinstance(organism, Plant) is False:
                        self.get_world().add_activity("Organism " + organism.get_name() + " was killed by "+self.get_name())
                    self.set_position(proposed_position)

    def proposed_position(self, direction):
        steps = [
            Point(0, -1),
            Point(0, 1),
            Point(1, 0),
            Point(-1, 0),
            Point(0, 2),
            Point(0, -2),
            Point(2, 0),
            Point(-2, 0)
        ]
        return Point(self.get_position().get_x()+steps[direction].get_x(), self.get_position().get_y()+steps[direction].get_y())

    def collision(self, attacker):
        attack = random.choice([True, False])
        if attack:
            return self.fight(attacker)
        else:
            self.get_world().add_activity("Antelope escaped the fight")
            return False
