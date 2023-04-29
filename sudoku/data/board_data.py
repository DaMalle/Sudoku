#! /usr/bin/env python


# Third-party imports
import numpy as np

class SudokuSolution:
    def __init__(self, random_lib):
        self._BASE = 3
        self._SIDE = 9
        self._GRID = 81
        
        # Libaries
        self.random_lib = random_lib

    def create(self) -> np.ndarray:
        """creates valid sudoku solution"""

        # generates and shuffles row- & column-numbers in groups, based on the length of the tile. example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        self._row_order = [ g * self._BASE + r for g in self.shuffle(range(self._BASE)) for r in self.shuffle(range(self._BASE)) ]
        self._col_order = [ g * self._BASE + c for g in self.shuffle(range(self._BASE)) for c in self.shuffle(range(self._BASE)) ]

        self._shuffled_nums = self.shuffle(range(1, 10))

        # returns a valid grid, based on the pattern-algorithm
        return np.array([[ self._shuffled_nums[self.apply_pattern(row, col)] for col in self._col_order ] for row in self._row_order])

    # support/internal functions
    def shuffle(self, data):
        return self.random_lib.sample(data, len(data))
    
    def apply_pattern(self, row, col):
        """creates a default board by rotating cells in the tile by 3 and then by 1 more for each new tile"""
        return (self._BASE * (row % self._BASE) + row // self._BASE + col) % self._SIDE


class PlayerBoard:
    def __init__(self, solution, emptied_cells, random_lib):
        self.solution = solution
        self.emptied_cells = emptied_cells

        # Libaries
        self.random_lib = random_lib
    
    def create(self):
        player_board_found = False
        while not player_board_found:
            self.board = np.array(self.solution)
            self.unfill_cells(self.board)
            self.player_board = [ tuple(i) for i in self.board ]
            
            self.empty_cells = [ (x, y) for y in range(9) for x in range(9) if self.board[y][x] == 0 ]
            
            player_board_found = self.is_one_solution(self.board, self.empty_cells)
        return self.player_board


    # Support/internal functions
    def unfill_cells(self, board: np.ndarray):
        for i in self.random_lib.sample(range(81), self.emptied_cells):
            board[i // 9][i % 9] = 0
    
    def solve(self, board: np.ndarray, emptied_cells) -> np.ndarray:
        empty_cells = emptied_cells
        for i in range(len(empty_cells)):
            x, y = empty_cells[i]
            numbers = list(range(1, 10))
            numbers.append(numbers.pop(self.solution[y][x]-1))
            for n in numbers:
                if self.is_possible(board, y,x,n):
                    board[y][x] = n
                    del empty_cells[0]
                    self.solve(board, empty_cells)
                    if empty_cells != []:
                        board[y][x] = 0
                        empty_cells.insert(0, (x, y))
            break
        if empty_cells == []:
            return board

    def is_possible(self, board, y,x,n):
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(9):
            if board[y][i] == n: # Checks horizontal
                return False
            if board[i][x] == n: # Checks vertical
                return False
            if board[y0 + (i // 3)][x0 + (i % 3)] == n:  # Checks tile
                return False
        return True

    def is_one_solution(self, board: np.ndarray, empty_cells) -> bool:
        """Returns true if solve() is same as solution."""

        return np.array_equal(self.solution, self.solve(board, empty_cells))