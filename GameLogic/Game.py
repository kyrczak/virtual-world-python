import pathlib

import GUI.GameWindow
from GUI.TileButton import TileButton
from GameLogic.Animals.Antelope import Antelope
from GameLogic.Animals.Cybersheep import Cybersheep
from GameLogic.Animals.Fox import Fox
from GameLogic.Animals.Human import Human
from GameLogic.Animals.Sheep import Sheep
from GameLogic.Animals.Turtle import Turtle
from GameLogic.Animals.Wolf import Wolf
from GameLogic.Plants.Belladonna import Belladonna
from GameLogic.Plants.Dandelion import Dandelion
from GameLogic.Plants.Grass import Grass
from GameLogic.Plants.Guarana import Guarana
from GameLogic.Plants.Hogweed import Hogweed
from GameLogic.Systems.Keys import Keys
from GameLogic.Systems.Point import Point
from GameLogic.World import World
from GameLogic.Organism import Organism


class Game:
    def __init__(self, width=30, height=30):
        self.world = World(width, height)
        self.world.rand_new_organisms()
        self.gui = GUI.GameWindow.GameWindow(self)
        self.draw_game_board()

    def game_next_turn(self):
        self.get_world().next_turn()
        self.clear_game_board()
        self.draw_game_board()
        self.get_world().set_key(Keys.DEFAULT)

    def save_game(self, text):
        path = pathlib.Path().resolve()
        save = open(rf'{path}\saves\{text}.txt', "x")
        save.write(self.world.get_name()+" "+str(self.world.get_width())+" "+str(self.world.get_height())+" "+str(len(self.world.get_organisms()))+" \n")
        for organism in self.get_world().get_organisms():
            if isinstance(organism, Human):
                save.write(organism.get_name()+" "+str(organism.get_position().get_x())+" "+str(organism.get_position().get_y())+" "+str(organism.get_power())+" "+str(organism.get_initiative())+" "+str(organism.get_age())+" "+str(organism.get_ability_cooldown())+" "+str(organism.get_ability_time())+" "+str(int(organism.get_ability_active()))+" \n")
            else:
                save.write(organism.get_name() + " " + str(organism.get_position().get_x()) + " " + str(organism.get_position().get_y()) + " " + str(organism.get_power()) + " " +str(organism.get_initiative()) + " " +str(organism.get_age())+" \n")
        save.close()

    def load_game(self, path):
        file = open(path, "r")
        world_line = file.readline()
        elements = world_line.split(" ")
        size = int(elements[1])
        new_world = World(size, size)
        for line in file:
            elements = line.split(" ")
            match elements[0]:
                case "Human":
                    new_world.add_organism(
                        Human(Point(int(elements[1]), int(elements[2])),new_world, int(elements[3]), int(elements[4]),
                              int(elements[5]), int(elements[6]), bool(elements[7])))
                case "Wolf":
                    new_world.add_organism(
                        Wolf(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[4]),
                             int(elements[5])))
                case "Sheep":
                    new_world.add_organism(
                        Sheep(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[4]),
                             int(elements[5])))
                case "Cybersheep":
                    new_world.add_organism(
                        Cybersheep(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[4]),
                              int(elements[5])))
                case "Fox":
                    new_world.add_organism(
                        Fox(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[4]),
                             int(elements[5])))
                case "Turtle":
                    new_world.add_organism(
                        Turtle(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[4]),
                             int(elements[5])))
                case "Antelope":
                    new_world.add_organism(
                        Antelope(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[4]),
                             int(elements[5])))
                case "Belladonna":
                    new_world.add_organism(
                        Belladonna(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]),
                                   int(elements[5])))
                case "Grass":
                    new_world.add_organism(
                        Grass(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]), int(elements[5])))
                case "Dandelion":
                    new_world.add_organism(
                        Dandelion(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]),
                                  int(elements[5])))
                case "Guarana":
                    new_world.add_organism(
                        Guarana(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]),
                                  int(elements[5])))
                case "Hogweed":
                    new_world.add_organism(
                        Hogweed(Point(int(elements[1]), int(elements[2])), new_world, int(elements[3]),
                                  int(elements[5])))
        new_world.add_awaiting_organisms()
        self.world = new_world
        self.gui = GUI.GameWindow.GameWindow(self)
        self.gui.show()
        self.clear_game_board()
        self.draw_game_board()


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
