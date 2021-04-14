#! /usr/bin/env python

# built-in imports
import unittest

# local imports
from sudoku.data.sudoku_board import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.sudoku_board = SudokuBoard()
        self.solution = self.sudoku_board.solution
        self.baseline = self.sudoku_board.BASELINE
        self.grid_len = self.sudoku_board.grid_len

    def test_create_compare_horizontal(self):
        """tests if the horizontal lines are valid in the sudoku board"""
        for row in self.solution: self.assertEqual(sorted(row), [ i for i in range(1, self.grid_len + 1) ])
    
    def test_create_compare_vertical(self):
        """tests if the vertical lines are valid in the sudoku board"""
        for i in range(9): self.assertEqual(sorted([ row[i] for row in self.solution ]), [ i for i in range(1, self.grid_len + 1) ])
            
    def test_create_compare_tiles(self):
        """tests if the tiles are valid in the sudoku board"""

        def v_start(i): return i // self.baseline * self.baseline # pattern for vertical startpoint of each tile
        def h_start(i): return i * self.baseline % self.grid_len  # pattern for horizontal startpoint of each tile

        for i in range(9): self.assertEqual(sorted([ self.solution[k][j] for k in range(v_start(i), v_start(i) + self.baseline)
                                                                         for j in range(h_start(i), h_start(i) + self.baseline) ]), 
                                            [ i for i in range(1, self.grid_len + 1) ])


if __name__ == '__main__':
    unittest.main()