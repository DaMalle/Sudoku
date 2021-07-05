#! /usr/bin/env python


import tkinter as tk
import random as rdm
import sudoku.data.sudoku_solution_data as solution
import sudoku.data.sudoku_board_data as bor


class board(tk.Canvas):
    def __init__(self, main=None):
        super().__init__(main)
        self._main = main
        self._SOLUTION = [ tuple(i) for i in solution.SudokuSolution(rdm).create() ]
        self._PUZZLE = bor.PlayerBoard(self._SOLUTION, 45, rdm).create()
        self._board = [ list(i) for i in self._PUZZLE ]
        self._MARGIN = 20
        self._SIDE = 50
        self._HEIGHT = self._MARGIN * 2 + self._SIDE * 9
        self._WIDTH = self._HEIGHT
        self.row, self.col = -1, -1

        self._configure_widget()
        self._draw_grid()
        self._draw_puzzle()

        self.bind("<Button-1>", self.cell_clicked)
        self.bind("<Key>", self.key_pressed)

    def _configure_widget(self):
        self['bg'] = 'white'
        self['width'] = self._WIDTH
        self['height'] = self._HEIGHT

    def _draw_grid(self):
        for i in range(10):
            # draws vertical lines
            self.create_line(
                self._MARGIN + i * self._SIDE, self._MARGIN,
                self._MARGIN + i * self._SIDE, self._HEIGHT - self._MARGIN,
                fill = 'black' if i % 3 == 0 else 'gray',
                width = 2 if i % 3 == 0 else 1
                )
            
            # draws horizontal lines
            self.create_line(
                self._MARGIN, self._MARGIN + i * self._SIDE,
                self._WIDTH - self._MARGIN, self._MARGIN + i * self._SIDE,
                fill = 'black' if i % 3 == 0 else 'gray',
                width = 2 if i % 3 == 0 else 1
                )
    
    def _draw_puzzle(self):
        self.delete("numbers")
        for i in range(9):
            for j in range(9):
                start = self._PUZZLE[i][j]
                answer = self._board[i][j]
                original = self._SOLUTION[i][j]
                if answer != 0:
                    color = 'red'
                    if answer == original:
                        color = 'green'
                    if start == original:
                        color = 'black'

                    self.create_text(
                        self._MARGIN + j * self._SIDE + self._SIDE / 2,
                        self._MARGIN + i * self._SIDE + self._SIDE / 2,
                        text=answer, tags="numbers",
                        fill=color
                    )

    def _draw_cursor(self):
        self.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            self.create_rectangle(
                self._MARGIN + self.col * self._SIDE + 1,
                self._MARGIN + self.row * self._SIDE + 1,
                self._MARGIN + (self.col + 1) * self._SIDE - 1,
                self._MARGIN + (self.row + 1) * self._SIDE - 1,
                outline="red", tags="cursor"
            )
    
    def cell_clicked(self, event):
        """if self.game.game_over:
            return"""
        x = event.x
        y = event.y
        if (x > self._MARGIN and x < self._WIDTH - self._MARGIN and
            y > self._MARGIN and y < self._HEIGHT - self._MARGIN):
            self.focus_set()
            row = int((y - self._MARGIN) / self._SIDE)
            col = int((x - self._MARGIN) / self._SIDE)
            if (row, col) == (self.row, self.col):
                self.row = -1
                self.col = -1
            elif self._PUZZLE[row][col] == 0:
                self.row = row
                self.col = col
        else:
            self.row = -1
            self.col = -1

        self._draw_cursor()

    def key_pressed(self, event):
        """if self.game.game_over:
            return"""
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self._board[self.row][self.col] = int(event.char)
            
            self._draw_puzzle()
            self._draw_cursor()
            """if self.game.check_win():
                self.draw_victory()"""



def main():
    root = tk.Tk()
    board(main=root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()