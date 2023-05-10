#! /usr/bin/env python


# Built-in imports
import tkinter as tk

# Local imports
from sudoku.logic.game_logic import GameModes, GamePlay


class SudokuBoard(tk.Canvas):
    def __init__(self, main: tk.Frame, data: GamePlay) -> None:
        super().__init__(main)
        self.main = main
        self._data = data
        self._TILE_SIDE = 50
        self._MARGIN = 20
        self._GRID_SIDE = self._TILE_SIDE * 9
        self._BOARD_SIDE = self._GRID_SIDE + 2 * self._MARGIN

        self.current_board = list(list(row) for row in self._data.player_board.board)

        # default focus coordinates
        self.column = 0
        self.row = 0

        self._configure_bindings()
        self._configure_widget()
        self._draw_grid()
        self._draw_start_board()
        self._draw_cursor()
    
    def _configure_bindings(self) -> None:
        """Assigns keybindings to function for moving cursor and inserting numbers"""

        self.bind('<Button-1>', self._focus_tile)
        for key in ['<Up>', '<Down>', '<Left>', '<Right>', 'h', 'j', 'k', 'l']:
            self.bind_all(key, self._move__focus_tile)
        for key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '<BackSpace>']:
            self.bind_all(key, self._insert_key_value)
    
    def _configure_widget(self) -> None:
        self['width'] = self._BOARD_SIDE
        self['height'] = self._BOARD_SIDE
        self['bg'] = 'white'

    def check_game_state(self) -> None:
        current_solution = tuple(tuple(row) for row in self.current_board)
        if current_solution == self._data.solution.board:
            self.main.destroy()

    def _draw_grid(self):
        for i in range(10):
            self.create_line( # draws vertical lines
                self._MARGIN + i * self._TILE_SIDE, self._MARGIN,
                self._MARGIN + i * self._TILE_SIDE, self._BOARD_SIDE - self._MARGIN,
                fill = 'black' if i % 3 == 0 else 'gray',
                width = 2 if i % 3 == 0 else 1
            )
            
            self.create_line( # draws horizontal lines
                self._MARGIN, self._MARGIN + i * self._TILE_SIDE,
                self._BOARD_SIDE - self._MARGIN, self._MARGIN + i * self._TILE_SIDE,
                fill = 'black' if i % 3 == 0 else 'gray',
                width = 2 if i % 3 == 0 else 1
            )
    
    def _draw_start_board(self) -> None:
        for iy, row in enumerate(self.current_board):
            for ix, number in enumerate(row):
                if number != 0:
                    x = ix * self._TILE_SIDE + self._MARGIN + self._TILE_SIDE // 2
                    y = iy * self._TILE_SIDE + self._MARGIN + self._TILE_SIDE // 2
                    self.create_text(x, y, text=number, font=('Arial', self._TILE_SIDE // 4))
    
    def _insert_key_value(self, event: tk.Event) -> None:
        if self._data.player_board.board[self.row][self.column] == 0:
            self.delete(f'x={self.column}y={self.row}')
            if event.keysym == 'BackSpace':
                self.current_board[self.row][self.column] = 0
            else:
                self.current_board[self.row][self.column] = int(event.keysym)
                x = self.column * self._TILE_SIDE + self._MARGIN + self._TILE_SIDE // 2
                y = self.row * self._TILE_SIDE + self._MARGIN + self._TILE_SIDE // 2
                self.create_text(x, y, text=event.keysym,
                                tag=f'x={self.column}y={self.row}',
                                font=('Arial', self._TILE_SIDE // 4),
                                fill='royalblue')
        self.check_game_state()

    def _move__focus_tile(self, event: tk.Event) -> None:
        """Assign keys to move focus on sudoku grid"""

        match event.keysym:
            case 'j' | 'Down':
                self.row += 1
                self.row = self.row if self.row <= 8 else 0
            case 'k' | 'Up':
                self.row -= 1
                self.row = self.row if self.row >= 0 else 8
            case 'h' | 'Left':
                self.column -= 1
                self.column = self.column if self.column >= 0 else 8
            case 'l' | 'Right':
                self.column += 1
                self.column = self.column if self.column <= 8 else 0
        self._draw_cursor()

    def _focus_tile(self, event: tk.Event) -> None:
        if self._is_in_grid(event.x, event.y):
            self.column = (event.x - self._MARGIN) // self._TILE_SIDE
            self.row = (event.y - self._MARGIN) // self._TILE_SIDE
            self.delete('focus_box')
            self._draw_cursor()
    
    def _is_in_grid(self, x: int, y: int) -> bool:
        """returns true if mouse-click is in grid and false if it is not"""

        return (
           self._MARGIN < y < self._GRID_SIDE + self._MARGIN and
           self._MARGIN < x < self._GRID_SIDE + self._MARGIN
        )
    
    def _draw_cursor(self) -> None:
        """Draws new focus box on canvas"""

        self.delete("cursor")
        self.create_rectangle(
            self._MARGIN + self.column * self._TILE_SIDE + 1,
            self._MARGIN + self.row * self._TILE_SIDE + 1,
            self._MARGIN + self.column * self._TILE_SIDE + self._TILE_SIDE - 1,
            self._MARGIN + self.row * self._TILE_SIDE + self._TILE_SIDE - 1,
            width=2, outline='red', tag='cursor')


class WinPage(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self['bg'] = 'white'

        self._draw_widget()
        
    def _draw_widget(self):
        tk.Button(self, text='You Won!', height=20, width=20, font=('Arial', 32), command=self.main.destroy).pack()


class GamePage(tk.Frame):
    def __init__(self, main, game_data):
        super().__init__(main)
        self.main = main
        self.game_data = game_data
        self['bg'] = 'white'

        self._draw_widget()

    def _draw_widget(self):
        self.win = WinPage(self).grid(row=0, column=0, sticky='news')
        self.game_frame = tk.Frame(self, bg='white')
        self.game_frame.grid(row=0, column=0, sticky='news')
        self.board = SudokuBoard(self.game_frame, self.game_data).pack()
        

class ModeButton(tk.Button):
    def __init__(self, main, mode):
        super().__init__(main)
        self.main = main
        self.mode = mode
        self._configure_widget()
    
    def _start_game(self):
        GamePage(self.main, GamePlay(self.mode)).grid(row=0, column=0, sticky='news')

    def _configure_widget(self):
        self['width'] = 12
        self['height'] = 2
        self['font'] = ('Arial', 32)
        self['bg'] = 'White'
        self['bd'] = 0
        self['highlightthickness'] = 1
        self['text'] = self.mode.name
        self['command'] = self._start_game


class MainApp(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.main['bg'] = 'white'

        self._draw_widget()

    def _draw_widget(self):
        for mode in GameModes:
            ModeButton(self, mode).grid()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sudoku')
    MainApp(root).pack()
    root.mainloop()