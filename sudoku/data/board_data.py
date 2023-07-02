#! /usr/bin/env python


# Built-in imports
import random


class BoardSizeError(Exception):
    """Sudoku board is not 9x9"""
    pass


class SudokuBoard:
    def __init__(self, grid: tuple[tuple[int]]) -> None:
        self._grid = grid
        if not self._is_valid_grid_size():
            raise BoardSizeError("Sudoku board is not 9x9")

    def _is_valid_grid_size(self) -> bool:
        """Checks if self._grid is 9x9"""
        for row in self._grid:
            if len(row) != 9:
                return False
        return len(self._grid) == 9

    @property
    def board(self) -> tuple[tuple[int]]:
        return self._grid

    def get_transpose(self) -> tuple[tuple[int]]:
        """Returns grid with rows as columns"""
        return tuple(map(*self._grid))

    def get_tiles(self) -> tuple[tuple[int]]:
        """Returns tuple with 9 3x3 tiles in sudoku board"""
        return tuple(
            tuple(self._grid[(i // 3) + (j // 3) * 3][(i % 3) + (j % 3) * 3]
                  for i in range(9)) for j in range(9)
        )


class SudokuSolution:
    def __init__(self) -> None:
        self._BASE = 3
        self._SIDE = 9
        self._GRID = 81

    def create(self) -> SudokuBoard:
        """creates valid sudoku solution:
        1) shuffles first row numbers
        2) shuffles row and column order
        3) applies pattern and returns
        """

        _shuffled_nums = self._shuffle(range(1, 10))

        # generates and shuffles row- & column-numbers in groups,
        # based on the length of the tile.
        # example: [|3, 1, 2,| 6, 5, 4,|7, 9, 8|]
        _row_order = tuple(
            g * self._BASE + r
            for g in self._shuffle(range(self._BASE))
            for r in self._shuffle(range(self._BASE))
        )
        _column_order = tuple(
            g * self._BASE + c
            for g in self._shuffle(range(self._BASE))
            for c in self._shuffle(range(self._BASE))
        )

        valid_grid = tuple(tuple(
            _shuffled_nums[self._apply_pattern(r, c)] for c in _column_order)
            for r in _row_order
        )
        return SudokuBoard(grid=valid_grid)

    # support/internal functions
    def _shuffle(self, data: range) -> list[int]:
        return random.sample(data, len(data))

    def _apply_pattern(self, row: int, column: int) -> int:
        """creates a default board by rotating cells in the tile by 3
        and then by 1 more for each new tile
        """

        return (self._BASE * (row % self._BASE)
                + row // self._BASE + column) % self._SIDE


class PlayerBoard:
    def __init__(self, solution: SudokuBoard, empty_cells_count: int) -> None:
        self.solution = solution
        self.empty_cells_count = empty_cells_count

    def create(self) -> SudokuBoard:
        """Continues to create a player board
        until one is found with only one solution
        """

        player_board_found = False
        while not player_board_found:
            self._board = [list(row) for row in self.solution.board]
            self._unfill_cells()
            _board_copy = tuple(tuple(row) for row in self._board)
            self._empty_cells = self._get_empty_cells()
            self._possible_cell_values = self._get_possible_cell_values()
            self._reduce_possibilities()
            self._set_initial_solution_last()
            player_board_found = self.solution.board == self._solve()
        return SudokuBoard(_board_copy)

    def _set_initial_solution_last(self) -> None:
        for cell in self._empty_cells:
            x, y = cell
            key = f'{x}{y}'
            self._possible_cell_values[key].remove(self.solution.board[y][x])
            self._possible_cell_values[key].append(self.solution.board[y][x])

    def _get_possible_cell_values(self) -> dict[str, list[int]]:
        return dict(
            (f"{cell[0]}{cell[1]}", [i for i in range(1, 10)
                if self.is_possible(cell[0], cell[1], i)])
            for cell in self._empty_cells
        )

    def _get_empty_cells(self) -> list[tuple[int, int]]:
        """Returns coordinates for cells = 0 in sudoku grid"""
        return [
            (x, y) for y in range(9) for x in range(9)
            if self._board[y][x] == 0
        ]

    def _unfill_cells(self) -> None:
        for i in random.sample(range(81), self.empty_cells_count):
            self._board[i // 9][i % 9] = 0

    def _solve(self) -> tuple[tuple[int]] | None:
        """Solves a sudoku board with recursion and backtracking"""

        for cell in self._empty_cells:
            x, y = cell
            key = f'{x}{y}'
            for n in self._possible_cell_values[key]:
                if self.is_possible(x, y, n):
                    self._board[y][x] = n
                    del self._empty_cells[0]
                    self._solve()
                    if self._empty_cells != []:
                        self._board[y][x] = 0
                        self._empty_cells.insert(0, (x, y))
            break
        if self._empty_cells == []:
            return tuple(tuple(row) for row in self._board)

    def _reduce_possibilities(self) -> None:
        no_single_values = True
        while(no_single_values):
            no_single_values = False
            for empty_cell in self._empty_cells:
                x, y = empty_cell
                key = f'{x}{y}'
                values = self._possible_cell_values[key]
                if len(values) == 1:
                    self._board[y][x] = values[0]
                    self._empty_cells.remove((x, y))
                    self._possible_cell_values.pop(key)
                    no_single_values = True
                    break

    def is_possible(self, x: int, y: int, n: int) -> bool:
        """Checks if inserted number is a currently valid input in cell"""
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(9):
            if self._board[y][i] == n:  # Checks horizontal
                return False
            if self._board[i][x] == n:  # Checks vertical
                return False
            if self._board[y0 + (i // 3)][x0 + (i % 3)] == n:  # Checks tile
                return False
        return True
