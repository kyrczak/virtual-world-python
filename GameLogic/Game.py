from GUI.GameWindow import GameWindow
from GUI.TileButton import TileButton
from GameLogic.Animals.Human import Human
from GameLogic.Systems.Keys import Keys
from GameLogic.World import World
from GameLogic.Organism import Organism


class Game:
    def __init__(self, width=30, height=30):
        self.world = World(width, height)
        self.world.rand_new_organisms()
        self.gui = GameWindow(self)
        self.draw_game_board()

    def game_next_turn(self):
        self.get_world().next_turn()
        self.clear_game_board()
        self.draw_game_board()
        self.get_world().set_key(Keys.DEFAULT)

    def save_game(self, text):
        save = open(rf'C:\Users\pat20\PycharmProjects\virtua-world-python\saves\{text}.txt', "x")
        save.write(self.world.get_name()+" "+str(self.world.get_width())+" "+str(self.world.get_height())+" "+str(len(self.world.get_organisms()))+"\n")
        for organism in self.get_world().get_organisms():
            if isinstance(organism, Human):
                save.write(organism.get_name()+" "+str(organism.get_position().get_x())+" "+str(organism.get_position().get_y())+" "+str(organism.get_power())+" "+str(organism.get_initiative())+" "+str(organism.get_age())+" "+str(organism.get_ability_cooldown())+" "+str(organism.get_ability_time())+" "+str(organism.get_ability_active())+"\n")
            else:
                save.write(organism.get_name() + " " + str(organism.get_position().get_x()) + " " + str(organism.get_position().get_y()) + " " + str(organism.get_power()) + " " +str(organism.get_initiative()) + " " +str(organism.get_age())+"\n")
        save.close()

    # TODO Load Game

    def clear_game_board(self):
        for tile in self.get_gui().get_tiles():
            if isinstance(tile, TileButton):
                tile_coordinates = tile.get_position()
                organism = self.get_world().get_organism(tile_coordinates)
                if organism is None:
                    tile.clear_style()

    def draw_game_board(self):
        for tile in self.get_gui().get_tiles():
            if isinstance(tile, TileButton):
                tile_coordinates = tile.get_position()
                organism: Organism = self.get_world().get_organism(tile_coordinates)
                if organism is not None:
                    tile.set_style(organism.get_color())
        self.get_gui().get_journal_panel().set_journal_activities()

    def get_world(self):
        return self.world

    def get_gui(self):
        return self.gui

    def set_world(self, world):
        self.world = world
