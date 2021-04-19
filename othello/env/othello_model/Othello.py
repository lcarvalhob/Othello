def valid_move(row, col):
    return 0 <= row <= 7 and 0 <= col <= 7


class Othello:

    ROWS = 8
    COLS = 8
    EMPTY = '-'
    PLAYER1 = 'B'
    PLAYER2 = 'W'

    def __init__(self):
        self.empty = self.EMPTY
        self.player1 = self.PLAYER1
        self.player2 = self.PLAYER2
        self.rows = self.ROWS
        self.cols = self.COLS
        self.board = self.new_board()
        self.whose_turn = self.PLAYER1

    def new_board(self):
        board = []
        for x in range(self.rows):
            board.append([])
            for y in range(self.cols):
                board[-1].append(self.empty)
        board[3][3] = self.player2
        board[4][4] = self.player2
        board[3][4] = self.player1
        board[4][3] = self.player1

        return board

    def move(self, player, row, col):
        opponent = self.opponent()
        disks_to_flip = self.check_move(player, row, col)

        if disks_to_flip != 0:
            if opponent != player:
                self.board[row][col] = player
                for x, y in disks_to_flip:
                    self.board[x][y] = player
                if self.valid_moves(opponent):
                    self.switch_turn()
        elif self.valid_moves(opponent):
            self.switch_turn()

    def check_move(self, player, row, col):
        if self.board[row][col] != self.empty or not valid_move(row, col):
            return 0

        self.board[row][col] = player

        if player == self.player1:
            opponent = self.player2
        else:
            opponent = self.player1

        disks_to_flip = []
        for xdir in range(-1, 2):
            for ydir in range(-1, 2):
                x, y = row, col
                x += xdir
                y += ydir
                if valid_move(x, y) and self.board[x][y] == opponent:
                    x += xdir
                    y += ydir
                    if not valid_move(x, y):
                        continue
                    while self.board[x][y] == opponent:
                        x += xdir
                        y += ydir
                        if not valid_move(x, y):
                            break
                    if not valid_move(x, y):
                        continue
                    if self.board[x][y] == player:
                        while True:
                            x -= xdir
                            y -= ydir
                            if x == row and y == col:
                                break
                            disks_to_flip.append([x, y])

        self.board[row][col] = self.empty
        if len(disks_to_flip) == 0:
            return 0
        return disks_to_flip

    def valid_moves(self, player):
        valid_moves = []

        for x in range(self.rows):
            for y in range(self.cols):
                if self.check_move(player, x, y):
                    valid_moves.append([x, y])
        return valid_moves

    def game_state(self):
        return len(self.valid_moves(self.player1)) == 0 and len(self.valid_moves(self.player2)) == 0

    def disks_count(self):
        player1 = 0
        player2 = 0
        for x in range(self.rows):
            for y in range(self.cols):
                if self.board[x][y] == self.player1:
                    player1 += 1
                elif self.board[x][y] == self.player2:
                    player2 += 1
        return {self.player1: player1, self.player2: player2}

    def get_winner(self):
        winner_count = self.disks_count()
        if winner_count[self.player1] > winner_count[self.player2]:
            return self.player1
        elif winner_count[self.player1] < winner_count[self.player2]:
            return self.player2
        else:
            return None

    def switch_turn(self):
        if self.whose_turn == self.player1:
            self.whose_turn = self.player2
        else:
            self.whose_turn = self.player1

    def opponent(self):
        if self.whose_turn == self.player1:
            return self.player2
        else:
            return self.player1

    def get_board(self):
        return self.board

    def current_player(self):
        return self.whose_turn

    def action_conversion(self, action):
        return action // self.rows, action % self.cols
