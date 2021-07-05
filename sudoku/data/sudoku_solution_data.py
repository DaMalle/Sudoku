#! /usr/bin/env python


class SudokuSolution:
    def __init__(self, random_lib):
        self._BASE = 3
        self._SIDE = 9
        self._GRID = 81
        
        # Libaries
        self.random_lib = random_lib

    def create(self):
        """creates valid sudoku solution"""

        # generates and shuffles row- & column-numbers in groups, based on the length of the tile. example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        self._row_order = [ g * self._BASE + r for g in self.shuffle(range(self._BASE)) for r in self.shuffle(range(self._BASE)) ]
        self._col_order = [ g * self._BASE + c for g in self.shuffle(range(self._BASE)) for c in self.shuffle(range(self._BASE)) ]

        self._shuffled_nums = self.shuffle(range(1, 10))

        # returns a valid grid, based on the pattern-algorithm
        return [ [ self._shuffled_nums[self.apply_pattern(row, col)] for col in self._col_order ] for row in self._row_order ]

    # support/internal functions
    def shuffle(self, data):
        return self.random_lib.sample(data, len(data))
    
    def apply_pattern(self, row, col):
        """creates a default board by rotating cells in the tile by 3 and then by 1 more for each new tile"""
        return (self._BASE * (row % self._BASE) + row // self._BASE + col) % self._SIDE