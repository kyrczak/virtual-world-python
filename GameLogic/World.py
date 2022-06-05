import secrets

from GameLogic.Animals.Human import Human
from GameLogic.Systems.Keys import Keys
from GameLogic.Systems.Point import Point


class World:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.key = Keys.DEFAULT
        self.turn = 0
        self.is_human_alive = False
        self.plane = [[0 for x in range(self.width)] for y in range(self.height)]
        self.organisms = []
        self.to_add = []
        self.to_remove = []
        self.journal= []

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_key(self):
        return self.key

    def get_name(self):
        return "World"

    def get_organisms(self):
        return self.organisms

    def get_journal(self):
        return self.journal

    def increase_turn(self):
        self.turn += 1

    def add_organism(self, org):
        for added in self.to_add:
            if added.get_position().get_x() == org.get_position().get_x() and added.get_position().get_y() == org.get_position().get_y():
                return
        for existing in self.organisms:
            if existing.get_position().get_x() == org.get_position().get_x() and existing.get_position().get_y() == org.get_position().get_y():
                return
        self.to_add.append(org)

    def add_activity(self, activity):
        self.journal.append(activity)

    def add_awaiting_organisms(self):
        if not self.to_add:
            for org in self.to_add:
                self.organisms.append(org)
            self.organisms.clear()
        # TODO sort by initiative and age
        self.get_organisms().sort()

    def sort_organism(self):
        for org in self.organisms:
            if not org.is_alive:
                if isinstance(org, Human):
                    self.is_human_alive = False
                self.to_remove.append(org)
        if not self.to_remove:
            for org in self.to_remove:
                self.organisms.remove(org)
            self.to_remove.clear()
        self.add_awaiting_organisms()

    def get_organism(self, position):
        for org in self.organisms:
            if org.get_position().get_x() == position.get_x() and org.get_position().get_y() == position.get_y():
                return org
        return None

    def next_turn(self):
        for org in self.get_organisms():
            if org.is_alive:
                org.action()
        self.sort_organism()
        self.increase_turn()

    def clear_board(self):
        for i in range(self.height):
            for j in range(self.width):
                self.plane[i][j] = '_'

    def draw_board(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.plane[i][j])
            print("\n")
        print("\n")

    def set_key(self, key):
        self.key = key

    def rand_new_organisms(self):
        amount_of_organisms = self.get_width()+self.get_height()
        x = secrets.randbelow(self.get_width())
        y = secrets.randbelow(self.get_height())
        self.add_organism(Human())
        for i in range(amount_of_organisms):
            x = secrets.randbelow(self.get_width())
            y = secrets.randbelow(self.get_height())
            if self.get_organism(Point(x, y)) is None:
                which_organism = secrets.randbelow(11)
                # TODO switch with all organisms

        self.sort_organism()

    def get_human_alive(self):
        return self.is_human_alive
