#! /usr/bin/env python

import random

class SudokuBoard:
    def __init__(self):
        pass

    def create(self):
        base = 3
        tile = base**2

        # pattern for a baseline valid solution
        def pattern(row, column):
            return (base * (row % base) + row // base + column) % tile

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(list):
            return random.sample(list, len(list))

        blist = [i for i in range(base)]
        rows = [group*base + row for group in shuffle(blist) for row in shuffle(blist)] 
        cols = [group*base + column for group in shuffle(blist) for column in shuffle(blist)]
        nums = shuffle([i for i in range(1, 10)])

        # produce board using randomized baseline pattern
        print(rows)
        print(cols)
        print(nums)
        """board = [[nums[pattern(r,c)] for c in cols] for r in rows]
        for i in board: print(i)"""

    def empty_cells(self):
        pass

    def check_solutions(self):
        pass
    
SudokuBoard().create()