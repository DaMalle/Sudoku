#! /usr/bin/env python


# Built-in imports
import tkinter as tk
import random

# Local imports
from sudoku.layout.sudoku_board import SudokuBoard      # presentation
from sudoku.layout.sudoku_numpad import SudokuNumPad    # presentation
from sudoku.logic.game_logic import GameMode            # logic
from sudoku.data.sudoku_board import BoardData          # data
from sudoku.data.sudoku_solution import SudokuSolution  # data


class GamePage(tk.Frame):
    def __init__(self, main, board):
        super().__init__(main)
        self.main = main
        self.board = board
        self['bg'] = 'white'

        self.draw_widget()

    def draw_widget(self):
        SudokuBoard(self, self.board).pack()
        SudokuNumPad(self).pack()


class SettingsPage(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.modes = ['Expert', 'Hard', 'Medium', 'Easy']

        self.draw_widget()

    def draw_widget(self):
        self.mode_buttons = [ ModeButton(self, mode) for mode in self.modes ]
        for button in self.mode_buttons: button.grid()
        

class ModeButton(tk.Button):
    def __init__(self, main, mode):
        super().__init__(main)
        self.main = main
        self.mode = mode
        self.configure_widget()
    
    def start_game(self):
        self.solution = [ tuple(i) for i in SudokuSolution(random).create() ]
        self.player_board = GameMode(self.mode, self.solution, BoardData, random).get_player_board()
        GamePage(self.main.main, self.player_board).grid(row=0, column=0, sticky='news')

    def configure_widget(self):
        self['width'] = 16
        self['height'] = 4
        self['font'] = ('Arial', 32)
        self['bg'] = 'White'
        self['bd'] = 0
        self['highlightthickness'] = 1
        self['text'] = self.mode
        self['command'] = self.start_game


class MainApp(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.main['bg'] = 'white'

        self.draw_widget()
    
    def draw_widget(self):
        SettingsPage(self).grid(row=0, column=0)


def main():
    root = tk.Tk()
    MainApp(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
