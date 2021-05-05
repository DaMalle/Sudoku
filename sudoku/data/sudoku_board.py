#! /usr/bin/env python

class SudokuBoard:
    def __init__(self, solution, remaining_cells, random_lib, copy_lib):
        self._solution = solution
        self._remaining_numbers = remaining_cells

        # Libaries
        self.random_lib = random_lib
        self.copy_lib = copy_lib
    
    def create(self):
        self._board = [list(i) for i in self._solution]
        self.copy_lib.deepcopy(self._board)

        self._unfill_cells(self._board)

        self._empty_cells = [ (x, y) for y in range(9) for x in range(9) if self._board[y][x] == 0 ]

        if self._is_solution(self._board, self._empty_cells):
            return self._board

    # Support/internal functions
    def _unfill_cells(self, board):
        for i in self.random_lib.sample(range(81), self._remaining_numbers):
            board[i // 9][i % 9] = 0
    
    def _solve(self, board, empty_cells):
        for i in range(len(empty_cells)):
            y = empty_cells[i][1]
            x = empty_cells[i][0]
            test_list = [ i for i in range(1, 10) if i != self._solution[y][x] ]
            test_list.append(self._solution[y][x])
            for n in test_list:
                if self._is_possible(y,x,n):
                    board[y][x] = n
                    del empty_cells[0]
                    self._solve(board, empty_cells)
                    if empty_cells != []:
                        board[y][x] = 0
                        empty_cells.insert(0, (x, y))
            break
        return [tuple(i) for i in board]

    def _is_possible(self, board, y,x,n):
        for i in range(9): # Checks horizontal
            if board[y][i] == n:
                return False

        for i in range(9): # Checks vertical
            if board[i][x] == n:
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3): # Checks tile
            for j in range(3):
                if board[y0+i][x0+j] == n:
                    return False
        return True

    def _is_solution(self, board, empty_cells):
        """Returns true if solve() is same as solution.
        Else it returns false."""
        return not any(filter(lambda x: x not in self._solution, self._solve(board, empty_cells)))