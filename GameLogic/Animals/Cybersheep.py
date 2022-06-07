import math
import secrets

import GameLogic.Animals.Sheep
import GameLogic.Plants.Hogweed
from PyQt5.QtGui import QColor

from GameLogic.Plant import Plant


class Cybersheep(GameLogic.Animals.Sheep.Sheep):
    def __init__(self, position, world, power=11, initiative=4, age=0):
        super(Cybersheep, self).__init__(position, world, power, initiative, age)

    def get_sign(self):
        return 'C'

    def get_name(self):
        return "Cybersheep"

    def get_color(self):
        return QColor(0x00FFFF)

    def is_same_species(self, other):
        return isinstance(other, Cybersheep)

    def create_organism(self, position, world):
        self.get_world().add_organism(Cybersheep(position, world))

    def move(self):
        height = self.get_world().get_height()
        width = self.get_world().get_width()
        min_distance = math.sqrt(math.pow(height, 2)+math.pow(width, 2))
        closest_organism = None
        for organism in self.get_world().get_organisms():
            distance = math.sqrt(math.pow(organism.get_position().get_x()-self.get_position().get_x(), 2)+math.pow(organism.get_position().get_y()-self.get_position().get_y(), 2))
            if isinstance(organism, GameLogic.Plants.Hogweed.Hogweed) and distance < min_distance:
                min_distance = distance
                closest_organism = organism

        if closest_organism is not None:
            if abs(self.get_position().get_x()-closest_organism.get_position().get_x()) > abs(self.get_position().get_y()-closest_organism.get_position().get_y()):
                if self.get_position().get_x() > closest_organism.get_position().get_x():
                    self.normal_move(3)
                else:
                    self.normal_move(2)
            else:
                if self.get_position().get_y() > closest_organism.get_position().get_y():
                    self.normal_move(0)
                else:
                    self.normal_move(1)
        else:
            super().move()

    def normal_move(self, direction):
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
