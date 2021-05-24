#! /usr/bin/env python


class PlayerBoard:
    def __init__(self, solution, emptied_cells, random_lib):
        self.solution = solution
        self.emptied_cells = emptied_cells

        # Libaries
        self.random_lib = random_lib
    
    def create(self):
        player_board_found = False
        while player_board_found != True:
            self.board = [ list(i) for i in self.solution ]
            self.unfill_cells(self.board)
            self.player_board = [ tuple(i) for i in self.board ]
            
            self.empty_cells = [ (x, y) for y in range(9) for x in range(9) if self.board[y][x] == 0 ]
            
            if self.is_one_solution(self.board, self.empty_cells):
                player_board_found = True
        return self.player_board


    # Support/internal functions
    def unfill_cells(self, board):
        for i in self.random_lib.sample(range(81), self.emptied_cells):
            board[i // 9][i % 9] = 0
    
    def solve(self, board, emptied_cells):
        empty_cells = emptied_cells
        for i in range(len(empty_cells)):
            y = empty_cells[i][1]
            x = empty_cells[i][0]
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
            return [tuple(i) for i in board]

    def is_possible(self, board, y,x,n):
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

    def is_one_solution(self, board, empty_cells):
        """Returns true if solve() is same as solution."""
        return self.solution == self.solve(board, empty_cells)