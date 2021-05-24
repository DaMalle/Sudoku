#! /usr/bin/env python


# Built-in imports
import tkinter as tk
import random

# Local imports
from sudoku.layout.sudoku_board import SudokuBoard           # presentation
from sudoku.layout.sudoku_numpad import SudokuNumPad         # presentation
from sudoku.logic.game_logic import GameMode                 # logic
from sudoku.logic.game_logic import GamePlay                 # logic
from sudoku.data.sudoku_board_data import PlayerBoard        # data
from sudoku.data.sudoku_solution_data import SudokuSolution  # data


class WinPage(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self['bg'] = 'white'

        self.draw_widget()
        
    def draw_widget(self):
        tk.Button(self, text='You Won!', height=20, width=20, font=('Arial', 32), command=self.main.destroy).pack()


class GamePage(tk.Frame):
    def __init__(self, main, game_data):
        super().__init__(main)
        self.main = main
        self.game_data = game_data
        self['bg'] = 'white'

        self.draw_widget()

    def draw_widget(self):
        self.win = WinPage(self).grid(row=0, column=0, sticky='news')
        self.game_frame = tk.Frame(self, bg='white')
        self.game_frame.grid(row=0, column=0, sticky='news')
        self.board = SudokuBoard(self.game_frame, self.game_data).pack()
        self.numpad = SudokuNumPad(self.game_frame).pack()


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
        self.player_board = GameMode(self.mode, self.solution, PlayerBoard, random).get_player_board()
        GamePage(self.main.main, GamePlay(self.solution, self.player_board)).grid(row=0, column=0, sticky='news')

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
    root.title('Sudoku')
    MainApp(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
