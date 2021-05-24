#! /usr/bin/env python


class GameMode:
    def __init__(self, mode, solution, board_imp, random_lib):
        self.mode = mode

        # Local import dependencies
        self.solution = solution
        self.board_imp = board_imp

        # Libaries
        self.random_lib = random_lib

    def get_player_board(self):
        if self.mode == 'Expert':
            self.player_board = self.board_imp(self.solution, 50, self.random_lib).create()

        elif self.mode == 'Hard':
            self.player_board = self.board_imp(self.solution, 47, self.random_lib).create()

        elif self.mode == 'Medium':
            self.player_board = self.board_imp(self.solution, 45, self.random_lib).create()

        else:          # Easy/Default
            self.player_board = self.board_imp(self.solution, 43, self.random_lib).create()

        return self.tiles_to_row(self.player_board)
    
    def tiles_to_row(self, board):
        return [ [ board[y][x] for y in range(i // 3 * 3, (i // 3 * 3) + 3) 
                               for x in range(i * 3 % 9, (i * 3 % 9) + 3) ]
                               for i in range(9) ]


class GamePlay:
    def __init__(self, solution, player_board):
        self.solution = [ tuple(solution[y][x] for y in range(i // 3 * 3, (i // 3 * 3) + 3)
                                               for x in range(i * 3 % 9, (i * 3 % 9) + 3))
                                               for i in range(9) ]
        self.player_board = player_board
    
    def check_guess(self, y, x):
        return self.solution[y][x] == self.player_board[y][x]

    def check_win(self):
        return self.solution == [ tuple(i) for i in self.player_board ]