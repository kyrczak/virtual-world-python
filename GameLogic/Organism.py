import secrets
from PyQt5.QtGui import QColor
from GameLogic.Systems.Point import Point
from GameLogic.World import World


class Organism:
    age = 0
    power = 0
    initiative = 0
    world: World = None
    position = None
    is_alive = True
    color = QColor(255, 255, 255)

    def __init__(self, position: Point, world: World, power=0, initiative=0, age=0):
        self.position = position
        self.power = power
        self.initiative = initiative
        self.world = world
        self.age = age

    def action(self):
        pass

    def collision(self, attacker):
        pass

    def is_same_species(self, other):
        pass

    def create_organism(self, position, world):
        pass

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
        empty_positions = self.free_positions()
        chosen_position = self.choose_free_position(empty_positions)
        if chosen_position is not None:
            self.create_organism(chosen_position, self.get_world())

    def choose_free_position(self, empty_positions):
        if empty_positions:
            random_number = secrets.randbelow(empty_positions.len())
            position = Point(empty_positions[random_number].get_x(), empty_positions[random_number].get_y())
            return position
        else:
            return None

    def is_in_bounds(self, point):
        return 0 <= point.get_x() < self.get_world().get_width() and 0 <= point.get_y() < self.get_world().get_height()

    def free_positions(self):
        free_positions = []
        steps = [
            Point(self.get_position().get_x(), self.get_position().get_y()-1),
            Point(self.get_position().get_x(), self.get_position().get_y()+1),
            Point(self.get_position().get_x()+1, self.get_position().get_y()),
            Point(self.get_position().get_x()-1, self.get_position().get_y())
        ]
        for step in steps:
            if self.get_world().get_organism(step) is None and self.is_in_bounds(step):
                free_positions.append(step)
        return free_positions

    def set_position(self, position):
        self.position = position

    def set_age(self, age):
        self.age = age

    def set_power(self, power):
        self.power = power

    def set_alive(self, alive):
        self.is_alive = alive
