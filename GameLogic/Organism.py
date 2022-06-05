from PyQt5.QtGui import QColor

from GameLogic.Systems.Point import Point


class Organism:
    def __init__(self, position, world, power=0, initiative=0, age=0):
        self.position = position
        self.power = power
        self.initiative = initiative
        self.world = world
        self.age = age
        self.color = QColor(255, 255, 255)

    def action(self):
        return

    def collision(self, attacker):
        return

    def is_same_species(self, other):
        return

    def create_organism(self, position, world):
        return

    def proposed_position(self, direction):
        steps = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]
        return Point(self.get_position().get_x() + steps[direction].get_x(),
                     self.get_position().get_y() + steps[direction].get_y())

    def draw(self):
        self.get_world().plane[self.get_position().get_y()][self.get_position().get_x()] = self.get_sign()

    def get_power(self):
        return self.power

    def get_initiative(self):
        return self.initiative

    def get_position(self):
        return self.position

    def get_age(self):
        return self.age

    def get_world(self):
        return self.world

    def get_name(self):
        return "Organism"

    def get_sign(self):
        return '?'

    def get_color(self):
        return self.color

    def reproduce(self):
        empty_positions = self.freePositions()
        chosen_position = self.choose_free_position(empty_positions)
        if chosen_position is not None:
            self.create_organism(chosen_position, self.get_world())

    def choose_free_position(self, empty_positions):
        # TODO finish choose_free_position
        return