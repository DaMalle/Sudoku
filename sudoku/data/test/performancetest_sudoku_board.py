#! /usr/bin/env python

# Built-in imports
import timeit

# Local imports
from sudoku.data.sudoku_board import BoardData


class TestSudokuBoard:
    def __init__(self):
        self.setup = 'from sudoku.data.sudoku_board import BoardData'

    def test_create(self):
        pass


def main():
    TestSudokuBoard().test_create()

if __name__ == '__main__':
    main()