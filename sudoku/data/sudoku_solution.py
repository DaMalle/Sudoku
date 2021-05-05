#! /usr/bin/env python

# Buit-in imports
import copy as cp
import random

class SudokuSolution:
    def __init__(self):
        self.baseline = 3
        self.grid_len = self.baseline**2
        self.grid = self.grid_len**2

    def create(self):
        """creates valid sudoku solution"""

        self.shuffled_baseline = self._shuffle([ i for i in range(self.baseline) ])

        # generates and shuffles row- & column-numbers in groups, based on the length of the tile. example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        self.rows = [ group * self.baseline + row for group in self.shuffled_baseline for row in self.shuffled_baseline ]
        self.columns = [ group * self.baseline + column for group in self.shuffled_baseline for column in self.shuffled_baseline ]

        self.shuffled_numbers = self._shuffle([ i for i in range(1, self.grid_len + 1) ])

        # returns a valid grid, based on the pattern-algorithm
        return [ [ self.shuffled_numbers[self._apply_pattern(row, column)] for column in self.columns ] for row in self.rows ]

    # support/internal functions
    def _shuffle(self, data):
        return random.sample(data, len(data))
    
    def _apply_pattern(self, row, column):
        """creates a default board by rotating cells in the tile by 3 and then by 1 more for each new tile"""
        return (self.baseline * (row % self.baseline) + row // self.baseline + column) % self.grid_len