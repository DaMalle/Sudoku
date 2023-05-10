#! /usr/bin/env python


# Built-in imports
from enum import Enum

# Local imports
from sudoku.data.board_data import PlayerBoard, SudokuSolution


class GameModes(Enum):
    Expert = "Expert"
    Hard = "Hard"
    Medium = "Medium"
    Easy = "Easy"


class GamePlay:
    def __init__(self, mode: GameModes):
        self.mode = mode
        self.solution = SudokuSolution().create()
        self.player_board = self._get_player_board()

    def _get_player_board(self) -> PlayerBoard:
        match self.mode:
            case GameModes.Expert:
                empty_cells_count = 50
            case GameModes.Hard:
                empty_cells_count = 47
            case GameModes.Medium:
                empty_cells_count = 45
            case _:
                empty_cells_count = 43
        return PlayerBoard(self.solution, empty_cells_count).create()