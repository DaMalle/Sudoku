#! /usr/bin/env python

# built-in imports
import tkinter as tk

grid_data = ([0, 2, 1, 6, 3, 7, 5, 8, 0],
             [6, 7, 4, 5, 1, 8, 9, 2, 3],
             [5, 8, 3, 4, 9, 2, 1, 6, 7],
             [2, 6, 9, 8, 5, 4, 3, 7, 1],
             [7, 4, 5, 3, 6, 1, 2, 9, 8],
             [1, 3, 8, 7, 2, 9, 6, 4, 5],
             [8, 5, 6, 2, 7, 3, 4, 1, 9],
             [4, 1, 2, 9, 8, 5, 7, 3, 6],
             [3, 9, 7, 1, 4, 6, 8, 5, 2])


class NumPadButton(tk.Button):
    def __init__(self, main, num, row, col):
        super().__init__(main)
        self.main = main
        self.num = num
        self.col = col
        self.row = row
        self.configure_btn()

    def configure_btn(self):
        self['width'] = 4
        self['height'] = 4
        self['bg'] = 'White'
        self['text'] = self.num
        self['highlightthickness'] = 0
        self['border'] = 0
        self.grid(row=self.row, column=self.col, sticky="nsew")


class SudokuNumPad(tk.Frame):
    def __init__(self, main, row, col):
        super().__init__(main)
        self.main = main
        self.row = row
        self.col = col
        self.configure_frame()
        self.draw_widgets()
    
    def configure_frame(self):
        self['bg'] = 'white'
        self['height'] = 100
        self['width'] = 500
        self.grid(row=self.row, column=self.col)

    def draw_widgets(self):
        #self.button_frame = tk.Frame(self)
        #self.button_frame.pack()
        self.buttons = [NumPadButton(self, i, 0, i) for i in range(1, 10)]
        self.buttons.append(NumPadButton(self, 'Remove', 0, 10).configure(width=8))


class SudokuButton(tk.Button):
    def __init__(self, main, num, row, col):
        super().__init__(main)
        self.main = main
        self.num = num
        self.row = row
        self.col = col
        self.configure_btn()
    
    def configure_btn(self):
        self['width'] = 5
        self['height'] = 3
        self['bg'] = 'White'
        self['bd'] = 0
        self['highlightthickness'] = 1
        if self.num != 0:
            self['text'] = self.num
        self.grid(row=self.row, column=self.col)


class Sudoku(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()

    def draw_widget(self):
        self.sudoku_frame = tk.Frame(self)
        self.sudoku_frame.grid(row=0, column=0)
        self.grid = [SudokuButton(self.sudoku_frame, num, col, row) for col, item in enumerate(grid_data) for row, num in enumerate(item)]
        self.numpad = SudokuNumPad(self, 1, 0)



if __name__ == '__main__':
    root = tk.Tk()
    #root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0, weight=1)
    Sudoku(root).pack()
    root.mainloop()
