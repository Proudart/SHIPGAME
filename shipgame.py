import random

# define a Ship class to represent each ship
class Ship:
    def __init__(self, length):
        self.length = length
        self.sunk = False

    def is_sunk(self):
        return self.sunk

    def sink(self):
        self.sunk = True

# define a Board class to represent the game board


class Board:
    def __init__(self, size, num_ships):
        self.size = size
        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.board.append(row)

        self.ships = []
        for i in range(num_ships):
            self.ships.append(Ship(random.randint(1, size)))

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.size:
            return False
        if col < 0 or col >= self.size:
            return False
        return self.board[row][col] != 'S'

    def handle_move(self, player, other_board):
        valid_input = False
        while not valid_input:
            print("Player %d's turn:" % player)
            other_board.print_board()
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if self.is_valid_move(row, col):
                if other_board.board[row][col] == 'S':
                    self.board[row][col] = 'X'
                    other_board.ships[row][col].sink()
                else:
                    self.board[row][col] = 'O'
                valid_input = True
            else:
                print("Invalid move. Try again.")

# define the main game loop


def play_game():
    # initialize the boards
    board1 = Board(10, 5)
    board2 = Board(10, 5)

    # main game loop
    while True:
        # player 1's turn
        board1.handle_move(1, board2)
        board1.print_board()
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break

        # player 2's turn

        board2.handle_move(2, board1)
        board2.print_board()

    # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break

    # print the final boards
    print("Player 1's board:")
    board1.print_board()
    print("Player 2's board:")
    board2.print_board()


# start the game
play_game()
