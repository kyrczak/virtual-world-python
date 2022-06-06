from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal


class Sheep(Animal):
    def __init__(self, position, world, power=4, initiative=4, age=0):
        super(Sheep, self).__init__(position, power, initiative, age, world)

    def get_sign(self):
        return 'S'

    def get_name(self):
        return "Sheep"

    def get_color(self):
        return QColor(0xfada8e)

    def is_same_species(self, other):
        return isinstance(other, Sheep)

    def create_organism(self, position, world):
        self.get_world().add_organism(Sheep(position, world))
