#! /usr/bin/env python


# built-in imports
from enum import Enum


class GameModes(Enum):
    Expert = "Expert"
    Hard = "Hard"
    Medium = "Medium"
    Easy = "Easy"


class GameMode:
    def __init__(self, mode, solution, board_imp):
        self.mode = mode

        # Local import dependencies
        self.solution = solution
        self.board_imp = board_imp

    def get_player_board(self):
        match self.mode:
            case GameModes.Expert:
                empty_cells_count = 50
            case GameModes.Hard:
                empty_cells_count = 47
            case GameModes.Medium:
                empty_cells_count = 45
            case _:
                empty_cells_count = 1 # 43
            
        return self.board_imp(self.solution, empty_cells_count).create()


class GamePlay:
    def __init__(self, solution, player_board):
        self.solution = solution
        self.player_board = player_board