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
        self.board = Canvas(self.window, bg=BACKGROUND_COLOUR, width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.board.pack()
        self.window.bind("<Button-1>", self.play_again)
        self.board_state = Othello.Othello()
        self.start = False

    def draw_board(self):
        self.board.delete(ALL)
        self.draw_lines()
        self.draw_all_disks()

    def draw_lines(self):
        for i in range(ROWS):
            self.board.create_line(i * BOARD_WIDTH / ROWS, 0, i * BOARD_WIDTH / ROWS, BOARD_WIDTH, )
        for i in range(COLS):
            self.board.create_line(0, i * BOARD_HEIGHT / COLS, BOARD_HEIGHT, i * BOARD_HEIGHT / COLS, )

    def draw_all_disks(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.board_state.get_board()[x][y] != Othello.EMPTY:
                    self.draw_disk(x, y)

    def draw_disk(self, row, col):
        self.board.create_oval(col * BOARD_WIDTH / COLS, row * BOARD_HEIGHT / ROWS,
                               (col + 1) * BOARD_WIDTH / COLS, (row + 1) * BOARD_HEIGHT / ROWS,
                               fill=PLAYERS[self.board_state.get_board()[row][col]], outline="")

    def game_over(self):
        scores = self.board_state.disks_count()
        self.board.delete(ALL)

        if self.board_state.get_winner() is None:
            title_text = "It is a draw! \n"
            colour_winner = "Yellow"
        else:
            title_text = PLAYERS[self.board_state.get_winner()] + " wins! \n"
            colour_winner = PLAYERS[self.board_state.get_winner()]

        play_again_text = "Click to play new match \n"
        player1_text = "Black \n"
        player2_text = "White \n"

        self.board.create_text(BOARD_WIDTH / 1.935,
                               BOARD_HEIGHT / 6,
                               font="cmr 60 bold",
                               fill=colour_winner,
                               text=title_text)

        self.board.create_text(BOARD_WIDTH / 3,
                               3 * BOARD_HEIGHT / 8,
                               font="cmr 40 bold",
                               fill="Black",
                               text=player1_text)

        self.board.create_text(BOARD_WIDTH / 3.1,
                               1 * BOARD_HEIGHT / 2,
                               font="cmr 40 bold",
                               fill="Black",
                               text=str(scores['B']))

        self.board.create_text(BOARD_WIDTH / 1.5,
                               3 * BOARD_HEIGHT / 8,
                               font="cmr 40 bold",
                               fill="White",
                               text=player2_text)

        self.board.create_text(BOARD_WIDTH / 1.5,
                               1 * BOARD_HEIGHT / 2,
                               font="cmr 40 bold",
                               fill="White",
                               text=str(scores['W']))

        self.board.create_text(BOARD_WIDTH / 2,
                               BOARD_HEIGHT / 1.33,
                               font="cmr 30 bold",
                               fill=colour_winner,
                               text=play_again_text)

    def play_again(self, event):
        self.board_state.reset_board()
        self.draw_board()

    def update_board_state(self, new_state):
        self.board_state = new_state

    def mainloop(self):
        self.draw_board()

        while True:
            self.window.update()
