import secrets

from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal
from GameLogic.Plant import Plant


class Turtle(Animal):
    def __init__(self, position, world, power=2, initiative=1, age=0):
        super(Turtle, self).__init__(position, power, initiative, age, world)

    def get_sign(self):
        return 'T'

    def get_name(self):
        return "Turtle"

    def get_color(self):
        return QColor(0x1e3d24)

    def is_same_species(self, other):
        return isinstance(other, Turtle)

    def create_organism(self, position, world):
        self.get_world().add_organism(Turtle(position, world))

    def move(self):
        direction = secrets.randbelow(16)
        if direction < 4:
            proposed_position = self.proposed_position(direction)
            if self.is_in_bounds(proposed_position):
                organism = self.get_world().get_organism(proposed_position)
                if organism is None:
                    self.set_position(proposed_position)
                elif self.is_same_species(organism):
                    if secrets.randbelow(self.reproduction_chance) == 0:
                        self.reproduce()
                else:
                    if organism.collision(self):
                        if isinstance(organism, Plant) is False:
                            self.get_world().add_activity(
                                "Organism " + organism.get_name() + " was killed by " + self.get_name())
                        self.set_position(proposed_position)

    def collision(self, attacker):
        if attacker.get_power < 5:
            self.get_world().add_activity("Turtle blocked attack from "+attacker.get_power())
            return False
        else:
            return self.fight(attacker)
