#! /usr/bin/env python

# built-in imports
import tkinter as tk


class SudokuNumPad(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main

        self.configure_widget()
        self.draw_widgets()
    
    def configure_widget(self):
        self['bg'] = 'white'
        self['height'] = 100
        self['width'] = 500

    def draw_widgets(self):
        self.buttons = [ NumPadButton(self, i, 0, i) for i in range(1, 11) ]


class NumPadButton(tk.Button):
    def __init__(self, main, num, row, col):
        super().__init__(main)
        self.main = main
        self.num = num
        self.col = col
        self.row = row
        self.configure_widget()
    
    def focus_button(self):
        self.focus_set()
        for i in range(len(self.main.buttons)): self.main.buttons[i].configure(relief=tk.RAISED, fg='black', activeforeground='black')
        self.configure(relief=tk.SUNKEN, fg='dodgerblue', activeforeground='dodgerblue')

    def configure_widget(self):
        self['command'] = self.focus_button
        self['width'] = 6
        self['height'] = 4
        self['bg'] = 'White'
        self['text'] = self.num
        self['highlightthickness'] = 0
        self['border'] = 0
        self.configure(activebackground='white', activeforeground='black')
        if self.num == 10:
            self.configure(text='remove', width=8, fg='dodgerblue', activeforeground='dodgerblue')
            self.num = 0
            self.focus_set()
        self.grid(row=self.row, column=self.col, sticky="nsew")
