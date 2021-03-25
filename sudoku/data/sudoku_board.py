#! /usr/bin/env python

import random

class SudokuBoard:
    def __init__(self):
        self.solution = self.create()

    def create(self):
        """creates valid sudoku board"""
        
        self.side = 3 # tile side length
        self.tile = self.side**2

        self.shuffled_side_range = self.shuffle([i for i in range(self.side)])

        self.rows = [group * self.side + row for group in self.shuffled_side_range for row in self.shuffled_side_range]
        self.columns = [group * self.side + column for group in self.shuffled_side_range for column in self.shuffled_side_range]

        self.shuffled_num_range = self.shuffle([i for i in range(1, 10)])

        return [[self.shuffled_num_range[self.pattern(row, column)] for column in self.columns] for row in self.rows]

    def empty_cells(self):
        pass

    def check_solutions(self):
        pass
    
    # support functions
    def shuffle(self, data):
        return random.sample(data, len(data))
    
    def pattern(self, row, column):
        """creates a default board by rotating cells in the tiles"""
        return (self.side * (row % self.side) + row // self.side + column) % self.tile
    
    # functions for testing
    def create_with_columns_as_rows(self):
        return [[self.shuffled_num_range[self.pattern(column, row)] for column in self.columns] for row in self.rows]
    
SudokuBoard()