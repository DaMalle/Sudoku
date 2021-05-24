#! /usr/bin/env python

# Built-in imports
import unittest
import random

# Local imports
from sudoku.data.sudoku_solution_data import SudokuSolution


class TestSudokuSolution(unittest.TestCase):
    def setUp(self):
        self.sudoku_Solution = SudokuSolution(random)
        self.solution = self.sudoku_Solution.create()
        self.baseline = self.sudoku_Solution.baseline
        self.grid_len = self.sudoku_Solution.grid_len

    def test_create_compare_horizontal(self):
        """Tests if the horizontal lines are valid in the sudoku board."""

        for row in self.solution: self.assertEqual(sorted(row), list(range(1, self.grid_len + 1)))
    
    def test_create_compare_vertical(self):
        """Tests if the vertical lines are valid in the sudoku board."""
        
        for i in range(9): self.assertEqual(sorted([ row[i] for row in self.solution ]), list(range(1, self.grid_len + 1)))
            
    def test_create_compare_tiles(self):
        """Tests if the tiles are valid in the sudoku board."""

        y0 = lambda y: y // self.baseline * self.baseline # Pattern for vertical startpoint of each tile.
        x0 = lambda x: x * self.baseline % self.grid_len  # Pattern for horizontal startpoint of each tile.

        for i in range(9): self.assertEqual(sorted([ self.solution[y][x] for y in range(y0(i), y0(i) + self.baseline)
                                                                         for x in range(x0(i), x0(i) + self.baseline) ]), 
                                            list(range(1, self.grid_len + 1)))


if __name__ == '__main__':
    unittest.main()