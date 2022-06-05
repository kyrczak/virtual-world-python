from GUI.GameWindow import GameWindow
from GameLogic.World import World


class Game:
    def __init__(self):
        self.world = World()
        # TODO Add rand_new_organisms()
        self.gui = GameWindow()
        # TODO self.draw_game_board()

    def __init__(self, width, height):
        self.world = World(width, height)
        # TODO Add rand_new_organisms()
        self.gui = GameWindow()
        # TODO self.draw_game_board()

    def game_next_turn(self):
        # TODO self.clear_game_board()
        # TODO self.draw_game_board()
        # TODO self.get_world().next_turn()
        # TODO self.clear_game_board()
        # TODO self.draw_game_board()
        # TODO self.get_world().set_key(Keys.DEFAULT)
        return
