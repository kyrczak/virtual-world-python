from GUI.GameWindow import GameWindow
from GUI.TileButton import TileButton
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
        self.clear_game_board()
        self.draw_game_board()
        self.get_world().next_turn()
        self.clear_game_board()
        self.draw_game_board()
        self.get_world().set_key(Keys.DEFAULT)
        return

    # TODO Save Game
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
