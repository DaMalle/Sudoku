#! /usr/bin/env python


# Built-in imports
import random

# Third-party imports
import numpy as np

class SudokuSolution:
    def __init__(self):
        self._BASE = 3
        self._SIDE = 9
        self._GRID = 81


    def create(self) -> np.ndarray:
        """creates valid sudoku solution:
        1) shuffles first row numbers
        2) shuffles row and column order
        3) applies pattern and returns
        """

        self._shuffled_nums = self.shuffle(range(1, 10))

        # generates and shuffles row- & column-numbers in groups, 
        # based on the length of the tile. 
        # example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        self._row_order = [
            g * self._BASE + r
            for g in self.shuffle(range(self._BASE))
            for r in self.shuffle(range(self._BASE))
        ]
        self._col_order = [
            g * self._BASE + c
            for g in self.shuffle(range(self._BASE))
            for c in self.shuffle(range(self._BASE))
        ]


        # returns a valid grid, based on simple sudoku pattern-algorithm
        return np.array([
                [ self._shuffled_nums[self.apply_pattern(row, col)]
                 for col in self._col_order ] 
                 for row in self._row_order
            ]
        )

    # support/internal functions
    def shuffle(self, data: range) -> range:
        return random.sample(data, len(data))
    
    def apply_pattern(self, row: int, col: int) -> int:
        """creates a default board by rotating cells in the tile by 3
        and then by 1 more for each new tile
        """

        return (self._BASE * (row % self._BASE)
                + row // self._BASE + col) % self._SIDE


class PlayerBoard:
    def __init__(self, solution: np.ndarray, empty_cells_count: int) -> None:
        self.solution = solution
        self.empty_cells_count = empty_cells_count
    
    def create(self) -> np.ndarray:
        """Continues to create a player board 
        until one is found with only one solution
        """

        player_board_found = False
        while not player_board_found:
            self.player_board = np.array(self.solution)
            self.unfill_cells(self.player_board)
            self.player_board_copy = np.array(self.player_board)
            self.empty_cells = self.get_empty_cells(self.player_board)
            self.reduce_possibilities()
            player_board_found = self.is_one_solution()
        return self.player_board_copy


    # Support/internal functions
    def get_empty_cells(self, board: np.ndarray) -> list[tuple[int]]:
        """Returns coordinates for cells = 0 in sudoku grid"""
        return [
            (x, y) for y in range(9) for x in range(9)
            if board[y][x] == 0
        ]

    def unfill_cells(self, board: np.ndarray) -> None:
        for i in random.sample(range(81), self.empty_cells_count):
            board[i // 9][i % 9] = 0
    
    def solve(self, board: np.ndarray) -> np.ndarray | None:
        """Solves a sudoku board with recursion and backtracking"""

        for i in range(len(self.empty_cells)):
            x, y = self.empty_cells[i]
            numbers = self.numbers[f'{x}{y}']
            numbers.remove(self.solution[y][x])
            numbers.append(self.solution[y][x])
            for n in numbers:
                if self.is_possible(board, x, y, n):
                    board[y][x] = n
                    del self.empty_cells[0]
                    self.solve(board)
                    if self.empty_cells != []:
                        board[y][x] = 0
                        self.empty_cells.insert(0, (x, y))
            break
        if self.empty_cells == []:
            return board

    def reduce_possibilities(self) -> None:
        self.numbers = dict(
            (f"{ec[0]}{ec[1]}", 
                [i for i in range(1, 10)
                if self.is_possible(self.player_board, ec[0], ec[1], i)])
            for ec in self.empty_cells
        )
        no_single_values = True
        while(no_single_values):
            no_single_values = False
            for empty_cell in self.empty_cells:
                x, y = empty_cell
                key = f"{x}{y}"
                value = self.numbers[key]
                if len(value) == 1:
                    self.player_board[y][x] = value[0]
                    self.empty_cells.remove((x, y))
                    self.numbers.pop(key)
                    no_single_values = True
                    break

    def is_possible(self, board: np.ndarray, x: int, y: int, n: int) -> bool:
        """Checks if inserted number is a currently valid input in cell"""
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

    def is_one_solution(self) -> bool:
        """Returns true if solve() is same as solution."""

        found_solution = self.solve(self.player_board)
        return np.array_equal(self.solution, found_solution)