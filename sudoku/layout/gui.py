#! /usr/bin/env python

#built-in imports
import tkinter as tk

class MainApp(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.pack()
        self.main.geometry('500x500')

def main():
    root = tk.Tk()
    MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
