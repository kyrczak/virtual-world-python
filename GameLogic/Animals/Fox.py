import secrets

from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal
from GameLogic.Plant import Plant


class Fox(Animal):
    def __init__(self, position, world, power=3, initiative=7, age=0):
        super(Fox, self).__init__(position, power, initiative, age, world)

    def get_sign(self):
        return 'F'

    def get_name(self):
        return "Fox"

    def get_color(self):
        return QColor(0xDC2A00)

    def is_same_species(self, other):
        return isinstance(other, Fox)

    def create_organism(self, position, world):
        self.get_world().add_organism(Fox(position, world))

    def move(self):
        direction = secrets.randbelow(4)
        proposed_position = self.proposed_position(direction)
        if self.is_in_bounds(proposed_position):
            organism = self.get_world().get_organism(proposed_position)
            if organism is None:
                self.set_position(proposed_position)
            elif self.is_same_species(organism):
                self.reproduce()
            else:
                if organism.get_power() < self.get_power():
                    if organism.collision(self):
                        if isinstance(organism, Plant) is False:
                            self.get_world().add_activity("Organism " + organism.get_name() + " was killed by " + self.get_name())
                        self.set_position(proposed_position)
