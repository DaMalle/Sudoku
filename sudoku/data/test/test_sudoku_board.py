#! /usr/bin/env python

import unittest
from sudoku.data.sudoku_board import SudokuBoard

class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.sudoku_board = SudokuBoard()

    def test_create_horizontal(self):
        """tests if the horizontal lines are valid in the sudoku board"""
        for row in self.sudoku_board.solution: self.assertEqual(sorted(row), [i for i in range(1, 10)])
    
    def test_create_vertical(self):
        """tests if the vertical lines are valid in the sudoku board"""
        for i in range(9): self.assertEqual(sorted([row[i] for row in self.sudoku_board.solution]), [i for i in range(1, 10)])
            
    def test_create_tiles(self):
        for i in range(9):
            pass

if __name__ == '__main__':
    unittest.main()
