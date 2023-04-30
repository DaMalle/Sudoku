#! /usr/bin/env python

# Built-in imports
import timeit

# Local imports
from sudoku.data.board_data import PlayerBoard

setup = '''
from sudoku.data.sudoku_board_data import PlayerBoard
import random
        
board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3], 
                [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                [2, 3, 4, 5, 6, 7, 8, 9, 1], 
                [5, 6, 7, 8, 9, 1, 2, 3, 4], 
                [8, 9, 1, 2, 3, 4, 5, 6, 7], 
                [3, 4, 5, 6, 7, 8, 9, 1, 2], 
                [6, 7, 8, 9, 1, 2, 3, 4, 5], 
                [9, 1, 2, 3, 4, 5, 6, 7, 8]]
tpb = PlayerBoard(board, 40, random)
tpb.unfill_cells(board)
empty_cells = [ (x, y) for y in range(9) for x in range(9) if board[y][x] == 0 ]
'''

testcode = 'tpb.solve(board, empty_cells)'
print(timeit.timeit(stmt=testcode, setup=setup, number=1000))