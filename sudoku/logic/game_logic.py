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
            
        return self.tiles_to_row(self.board_imp(self.solution, empty_cells, self.random_lib).create())
    
    def tiles_to_row(self, board):
        return [ [ board[y][x] for y in range(i // 3 * 3, (i // 3 * 3) + 3) 
                               for x in range(i * 3 % 9, (i * 3 % 9) + 3) ]
                               for i in range(9) ]


class GamePlay:
    def __init__(self, solution, player_board):
        self.solution = [ tuple(solution[y][x] for y in range(i // 3 * 3, (i // 3 * 3) + 3)
                                               for x in range(i * 3 % 9, (i * 3 % 9) + 3))
                                               for i in range(9) ]
        self.player_board = player_board
    
    def check_guess(self, y, x):
        return self.solution[y][x] == self.player_board[y][x]

    def check_win(self):
        return self.solution == [ tuple(i) for i in self.player_board ]