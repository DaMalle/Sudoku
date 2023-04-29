#! /usr/bin/env python


# built-in imports
from enum import Enum


class Modes(Enum):
    Expert = "Expert"
    Hard = "Hard"
    Medium = "Medium"
    Easy = "Easy"


class GameMode:
    def __init__(self, mode, solution, board_imp, random_lib):
        self.mode = mode

        # Local import dependencies
        self.solution = solution
        self.board_imp = board_imp

        # Libaries
        self.random_lib = random_lib

    def get_player_board(self):
        match self.mode:
            case Modes.Expert:
                empty_cells = 50
            case Modes.Hard:
                empty_cells = 47
            case Modes.Medium:
                empty_cells = 45
            case _:
                empty_cells = 43
            
        return self.board_imp(self.solution, empty_cells, self.random_lib).create()


class GamePlay:
    def __init__(self, solution, player_board):
        self.solution = solution
        self.player_board = player_board