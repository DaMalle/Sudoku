#! /usr/bin/env python

# buit-in imports
import copy as cp
import random

#import numpy as np

class SudokuBoard:
    def __init__(self):
        self.BASELINE = 3
        self.grid_len = self.BASELINE**2
        self.grid = self.grid_len**2
        self.UNFILED_CELLS = 20

        self._board = self.create_board()
        self.solution = cp.deepcopy(self._board)
        self.player_board = cp.deepcopy(self.create_player_board())

    def create_board(self):
        """creates valid sudoku board"""

        self.shuffled_baseline = self.shuffle([i for i in range(self.BASELINE)])

        # generates and shuffles row- & column-numbers in groups, based on the length of the tile. example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        self.rows = [ group * self.BASELINE + row for group in self.shuffled_baseline for row in self.shuffled_baseline ]
        self.columns = [ group * self.BASELINE + column for group in self.shuffled_baseline for column in self.shuffled_baseline ]

        self.shuffled_numbers = self.shuffle([i for i in range(1, self.grid_len + 1)])

        # returns a valid grid, based on the pattern-algorithm
        return [ [ self.shuffled_numbers[self.apply_pattern(row, column)] for column in self.columns ] for row in self.rows ]

    def create_player_board(self):
        self.unfill_cells(self._board)
        return self._board

    # support functions
    def unfill_cells(self, board):
        for i in random.sample(range(self.grid), self.UNFILED_CELLS):
            board[i // self.grid_len][i % self.grid_len] = 0
    
    def shuffle(self, data):
        return random.sample(data, len(data))
    
    def apply_pattern(self, row, column):
        """creates a default board by rotating cells in the tile by 3 and then by 1 more for each new tile"""
        return (self.BASELINE * (row % self.BASELINE) + row // self.BASELINE + column) % self.grid_len