#! /usr/bin/env python


class SudokuSolution:
    def __init__(self, random_lib):
        self.baseline = 3
        self.grid_len = self.baseline**2
        self.grid = self.grid_len**2
        
        # Libaries
        self.random_lib = random_lib

    def create(self):
        """creates valid sudoku solution"""

        self.shuffled_baseline = self.shuffle(list(range(self.baseline)))

        # generates and shuffles row- & column-numbers in groups, based on the length of the tile. example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        self.rows = [ group * self.baseline + row for group in self.shuffled_baseline for row in self.shuffled_baseline ]
        self.columns = [ group * self.baseline + column for group in self.shuffled_baseline for column in self.shuffled_baseline ]

        self.shuffled_numbers = self.shuffle(list(range(1, self.grid_len + 1)))

        # returns a valid grid, based on the pattern-algorithm
        return [ [ self.shuffled_numbers[self.apply_pattern(row, column)] for column in self.columns ] for row in self.rows ]

    # support/internal functions
    def shuffle(self, data):
        return self.random_lib.sample(data, len(data))
    
    def apply_pattern(self, row, column):
        """creates a default board by rotating cells in the tile by 3 and then by 1 more for each new tile"""
        return (self.baseline * (row % self.baseline) + row // self.baseline + column) % self.grid_len