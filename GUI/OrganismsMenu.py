from PyQt5.QtWidgets import *

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
from GameLogic.Systems.Point import Point


class OrganismsMenu(QWidget):
    def __init__(self, position, game):
        super(OrganismsMenu, self).__init__()
        self.game = game
        self.layout = QVBoxLayout()
        self.button = QPushButton("Add")
        self.organisms_list = [
            "Human",
            "Wolf",
            "Sheep",
            "Cybersheep",
            "Fox",
            "Antelope",
            "Turtle",
            "Grass",
            "Dandelion",
            "Belladonna",
            "Guarana",
            "Hogweed"
        ]
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.organisms_list)
        self.tile_position = position
        self.set_ui()

    def set_ui(self):
        self.setFixedSize(200, 200)
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.add_selected_organism)
        self.show()

    def add_selected_organism(self):
        match self.combo_box.currentText():
            case "Sheep":
                self.game.get_world().add_organism(Sheep(self.tile_position, self.game.get_world()))
            case "Wolf":
                self.game.get_world().add_organism(Wolf(self.tile_position, self.game.get_world()))
            case "Fox":
                self.game.get_world().add_organism(Fox(self.tile_position, self.game.get_world()))
            case "Antelope":
                self.game.get_world().add_organism(Antelope(self.tile_position, self.game.get_world()))
            case "Turtle":
                self.game.get_world().add_organism(Turtle(self.tile_position, self.game.get_world()))
            case "Grass":
                self.game.get_world().add_organism(Grass(self.tile_position, self.game.get_world()))
            case "Dandelion":
                self.game.get_world().add_organism(Dandelion(self.tile_position, self.game.get_world()))
            case "Guarana":
                self.game.get_world().add_organism(Guarana(self.tile_position, self.game.get_world()))
            case "Hogweed":
                self.game.get_world().add_organism(Hogweed(self.tile_position, self.game.get_world()))
            case "Belladonna":
                self.game.get_world().add_organism(Belladonna(self.tile_position, self.game.get_world()))
            case "Cybersheep":
                self.game.get_world().add_organism(Cybersheep(self.tile_position, self.game.get_world()))
            case "Human":
                if self.game.get_world().is_human_alive is False:
                    self.game.get_world().add_organism(Human(self.tile_position, self.game.get_world()))
        self.game.clear_game_board()
        self.game.get_world().add_awaiting_organisms()
        self.game.draw_game_board()
        self.close()
        pass
