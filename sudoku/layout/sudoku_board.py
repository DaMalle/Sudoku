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
        self.tiles = [ SudokuTile(self, i) for i in self.data ]
        for i, t in enumerate(self.tiles): self.create_window(202*(i % 3)+104, 193*(i // 3)+99, window=t)

    def configure_widget(self):
        self['width'] = 610
        self['height'] = 583
        self['bg'] = '#696969'


class SudokuTile(tk.Frame):
    def __init__(self, main, data):
        super().__init__(main)
        self.main = main
        self.data = data

        self.draw_widget()

    def draw_widget(self):
        self.buttons = [ SudokuButton(self, i) for i in self.data ]
        for i, b in enumerate(self.buttons): b.grid(column=i % 3, row=i // 3)


class SudokuButton(tk.Button):
    def __init__(self, main, num):
        super().__init__(main)
        self.main = main
        self.num = num
        self.configure_widget()
    
    def change_text(self):
        self.new_text = self.focus_get().num
        
        if self.new_text != 0:
            self['text'] = self.new_text
        else:
            self['text'] = ''
    
    def configure_widget(self):
        self['command'] = self.change_text
        self['width'] = 5
        self['height'] = 3
        self['bg'] = 'White'
        self['fg'] = 'dodgerblue'
        self['bd'] = 0
        self['highlightthickness'] = 1
        if self.num != 0:
            self['text'] = self.num
            self.configure(state='disabled', disabledforeground='black') # dissables pressing button