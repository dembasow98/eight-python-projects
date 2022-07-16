from player import Player
import random

from tic_tac_toe.human_vs_computer.human import Human


#Computer player that inherits the player class
class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, board):
        #spot = random.choice(board.available_spots())
        #return spot
        return random.choice(board.available_spots())

