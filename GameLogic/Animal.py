import secrets
from GameLogic.Organism import Organism
from GameLogic.Plant import Plant
from GameLogic.Systems.Point import Point
from GameLogic.World import World


class Animal(Organism):
    def __init__(self, position: Point, power, initiative, age, world: World):
        super(Animal, self).__init__(position, world, power, initiative, age)
        self.reproduction_chance = 14

    def action(self):
        self.move()
        self.set_age(self.get_age()+1)

    def collision(self, attacker):
        return self.fight(attacker)

    def move(self):
        direction = secrets.randbelow(4)
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
                        self.get_world().add_activity("Organism " + organism.get_name() + " was killed by "+self.get_name())
                    self.set_position(proposed_position)

    def fight(self, attacker):
        if self.get_power() < attacker.get_power():
            self.set_alive(False)
            return True
        elif self.get_power() == attacker.get_power():
            self.set_alive(False)
            return True
        else:
            attacker.set_alive(False)
            return False
