#! /usr/bin/env python

# Built-in imports
import tkinter as tk


class SudokuBoard(tk.Canvas):
    def __init__(self, main, data):
        super().__init__(main)
        self.main = main
        self.data = data
        
        self.configure_widget()
        self.draw_widget()

    def draw_widget(self):
        self.tiles = [ SudokuTile(self, i, j) for i, j in enumerate(self.data.player_board) ]
        for i, t in enumerate(self.tiles): self.create_window(202*(i % 3)+104, 193*(i // 3)+99, window=t)

    def configure_widget(self):
        self['width'] = 610
        self['height'] = 583
        self['bg'] = '#696969'

    def check_game_state(self):
        if self.data.check_win():
            self.main.destroy()


class SudokuTile(tk.Frame):
    def __init__(self, main, tile_id, data):
        super().__init__(main)
        self.main = main
        self.data = data
        self.tile_id = tile_id

        self.draw_widget()

    def draw_widget(self):
        self.buttons = [ SudokuButton(self, self.tile_id, i, j) for i, j in enumerate(self.data) ]
        for i, b in enumerate(self.buttons): b.grid(column=i % 3, row=i // 3)


class SudokuButton(tk.Button):
    def __init__(self, main, tile_id, cell_id, num):
        super().__init__(main)
        self.main = main
        self.tile_id = tile_id
        self.cell_id = cell_id
        self.num = num
        self.configure_widget()
    
    def update(self):
        self['fg'] = 'red'
        self.new_text = self.focus_get().num
        if self.new_text != 0:
            self['text'] = self.new_text
            self.main.main.data.player_board[self.tile_id][self.cell_id] = self.new_text
            if self.main.main.data.check_guess(self.tile_id, self.cell_id):
                self['fg'] = 'dodgerblue'
        else:
            self['text'] = ''

        self.main.main.check_game_state()
    
    def configure_widget(self):
        self['command'] = self.update
        self['width'] = 5
        self['height'] = 3
        self['bg'] = 'White'
        self['bd'] = 0
        self['highlightthickness'] = 1
        if self.num != 0:
            self['text'] = self.num
            self.configure(state='disabled', disabledforeground='black') # dissables pressing button