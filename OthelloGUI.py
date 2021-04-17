import Othello
import pygame

BOARD_WIDTH = 600
BOARD_HEIGHT = 600
ROWS = Othello.ROWS
COLS = Othello.COLS
BACKGROUND_COLOUR = (0, 128, 0)
PLAYERS = {Othello.PLAYER1: (0, 0, 0), Othello.PLAYER2: (255, 255, 255)}


class OthelloGUI:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Othello')
        self.window = pygame.display.set_mode((BOARD_HEIGHT, BOARD_WIDTH))
        self.board_state = Othello.Othello()
        self.start = False
        self.draw_board()

    def draw_board(self):
        self.window.fill(BACKGROUND_COLOUR)
        self.draw_lines()
        self.draw_all_disks()
        pygame.display.update()

    def draw_lines(self):
        for i in range(ROWS):
            pygame.draw.line(self.window, (0, 0, 0), (i * BOARD_WIDTH / ROWS, 0), (i * BOARD_WIDTH / ROWS, BOARD_WIDTH))
        for i in range(COLS):
            pygame.draw.line(self.window, (0, 0, 0), (0, i * BOARD_HEIGHT / COLS), (BOARD_HEIGHT, i * BOARD_HEIGHT / COLS))

    def draw_all_disks(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.board_state.get_board()[x][y] != Othello.EMPTY:
                    self.draw_disk(x, y)

    def draw_disk(self, row, col):
        pygame.draw.circle(self.window, PLAYERS[self.board_state.get_board()[row][col]],
                           ((col + 0.51) * 600 / 8, (row + 0.51) * 600 / 8), 37)

    def game_over(self):
        scores = self.board_state.disks_count()
        self.window.fill(BACKGROUND_COLOUR)
        title_font = pygame.font.SysFont('Helvetica', 60, True)
        player_font = pygame.font.SysFont('Helvetica', 40, True)
        play_again_font = pygame.font.SysFont('Helvetica', 30, True)

        if self.board_state.get_winner() is None:
            title_text = title_font.render('It is a draw!', True, (255, 255, 0))

        elif self.board_state.get_winner() == 'B':
            colour_winner = PLAYERS[self.board_state.get_winner()]
            title_text = title_font.render('Black wins!', True, colour_winner)
        else:
            colour_winner = PLAYERS[self.board_state.get_winner()]
            title_text = title_font.render('White wins!', True, colour_winner)

        play_again_text = play_again_font.render('Click to play new match', True, (255, 255, 0))
        player1_title = player_font.render('Black', True, PLAYERS['B'])
        player1_score = player_font.render(str(scores['B']), True, PLAYERS['B'])
        player2_title = player_font.render('White', True, PLAYERS['W'])
        player2_score = player_font.render(str(scores['W']), True, PLAYERS['W'])

        self.window.blit(title_text, title_text.get_rect(centerx=BOARD_WIDTH / 2, centery=BOARD_HEIGHT / 6))
        self.window.blit(player1_title, player1_title.get_rect(centerx=BOARD_WIDTH / 3, centery=3 * BOARD_HEIGHT / 8))
        self.window.blit(player2_title, player2_title.get_rect(centerx=BOARD_WIDTH / 1.5, centery=3 * BOARD_HEIGHT / 8))
        self.window.blit(player1_score, player1_score.get_rect(centerx=BOARD_WIDTH / 3.1, centery=1 * BOARD_HEIGHT / 2))
        self.window.blit(player2_score, player2_score.get_rect(centerx=BOARD_WIDTH / 1.5, centery=1 * BOARD_HEIGHT / 2))
        self.window.blit(play_again_text, play_again_text.get_rect(centerx=BOARD_WIDTH / 2, centery=BOARD_HEIGHT / 1.33))

        pygame.display.update()

    def play_again(self):
        self.board_state.reset_board()
        self.draw_board()

    def update_board_state(self, new_state):
        self.board_state = new_state
        self.draw_all_disks()
        pygame.display.update()
