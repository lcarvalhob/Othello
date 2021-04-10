import Othello
from tkinter import *

BOARD_WIDTH = 600
BOARD_HEIGHT = 600
ROWS = Othello.ROWS
COLS = Othello.COLS
DELAY = 100
BACKGROUND_COLOUR = 'Green'
PLAYERS = {Othello.PLAYER1: 'Black', Othello.PLAYER2: 'White'}


class OthelloGUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Othello")
        self.window.configure(background=BACKGROUND_COLOUR)
        self.board = Canvas(self.window, width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.board.pack()
        self.board_state = Othello.Othello()

    def draw_board(self):
        self.board.delete(ALL)
        self.draw_lines()
        self.draw_all_disks()

    def draw_lines(self):
        for i in range(ROWS):
            self.board.create_line(0, i * BOARD_WIDTH / ROWS, i * BOARD_WIDTH / ROWS, BOARD_WIDTH, )
        for i in range(COLS):
            self.board.create_line(i * BOARD_HEIGHT / COLS, 0, BOARD_HEIGHT, i * BOARD_HEIGHT / COLS, )

    def draw_all_disks(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.board_state.get_board()[x][y] != Othello.EMPTY:
                    self.draw_disk(x, y)

    def draw_disk(self, row, col):
        self.board.create_oval(col * BOARD_WIDTH / COLS, row * BOARD_HEIGHT / ROWS,
                               (col + 1) * BOARD_WIDTH / COLS, (row + 1) * BOARD_HEIGHT / ROWS,
                               fill=PLAYERS[self.board_state.get_board()[row][col]])
