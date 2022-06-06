from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal


class Wolf(Animal):
    def __init__(self, position, world, power=9, initiative=5, age=0):
        super(Wolf, self).__init__(position, power, initiative, age, world)

    def get_sign(self):
        return 'W'

    def get_name(self):
        return "Wolf"

    def get_color(self):
        return QColor(0x616161)

    def is_same_species(self, other):
        return isinstance(other, Wolf)

    def create_organism(self, position, world):
        self.get_world().add_organism(Wolf(position, world))
