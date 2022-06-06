import secrets

from GameLogic.Organism import Organism
from GameLogic.Systems.Point import Point
from GameLogic.World import World


class Plant(Organism):
    growth_rate = 50

    def __init__(self, position: Point, power, age, world: World):
        super(Plant, self).__init__(position, world, power, 0, age)

    def action(self):
        self.grow()
        self.set_age(self.get_age() + 1)

    def collision(self, attacker):
        return self.fight(attacker)

    def grow(self):
        chance = secrets.randbelow(self.growth_rate)
        if chance == 0:
            self.reproduce()

    def fight(self, attacker):
        self.set_alive(False)
        return True
