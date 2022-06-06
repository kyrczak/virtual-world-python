import secrets

from PyQt5.QtGui import QColor

from GameLogic.Animal import Animal
from GameLogic.Plant import Plant
from GameLogic.Systems.Keys import Keys


class Human(Animal):
    is_ability_active = False
    ability_cooldown = 5
    ability_time = 5

    def __init__(self, position, world, power=5, initiative=4, age=0):
        super(Human, self).__init__(position, power, initiative, age, world)
        self.world.is_human_alive = True

    def set_ability_active(self, ability_active):
        self.is_ability_active = ability_active

    def set_ability_cooldown(self, ability_cooldown):
        self.ability_cooldown = ability_cooldown

    def set_ability_time(self, ability_time):
        self.ability_time = ability_time

    def get_ability_active(self):
        return self.is_ability_active

    def get_ability_cooldown(self):
        return self.ability_cooldown

    def get_ability_time(self):
        return self.ability_time

    def get_sign(self):
        return 'H'

    def get_name(self):
        return "Human"

    def get_color(self):
        return QColor(0, 0, 255)

    def move(self):
        key: Keys = self.get_world().get_key()
        if key is not Keys.DEFAULT and key is not Keys.KEY_F:
            proposed_position = self.proposed_position(key.value)
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
                            self.get_world().add_activity("Organism " + organism.get_name() + " was killed by " + self.get_name())
                        self.set_position(proposed_position)
        elif key == Keys.KEY_F:
            if self.get_ability_active() == False and self.get_ability_cooldown() == 5:
                self.set_ability_active(True)
                self.get_world().add_activity("Human used his special ability")
        self.ability_time_management()

    def collision(self, attacker):
        if self.get_ability_active() is False:
            return self.fight(attacker)
        else:
            self.get_world().add_activity("Alzur's shield deflected the attack from "+attacker.get_name())
            empty_positions = self.free_positions()
            chosen_position = self.choose_free_position(empty_positions)
            if chosen_position is not None:
                attacker.set_position(chosen_position)
            return False

    def ability_time_management(self):
        if self.get_ability_active():
            self.set_ability_time(self.get_ability_time()-1)
            if self.get_ability_time() == 0:
                self.set_ability_time(5)
                self.set_ability_active(False)
                self.set_ability_cooldown(self.get_ability_cooldown()-1)
        elif self.get_ability_active() is False and self.get_ability_cooldown() < 5:
            self.set_ability_cooldown(self.get_ability_cooldown()-1)
            if self.get_ability_cooldown() == 0:
                self.set_ability_cooldown(5)
