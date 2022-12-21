import random
import os
import string
import colorama
import math

# clear the console screen


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def decode(code):
    val = 0
    for ch in code: # base-26 decoding "plus 1"
        val = val * 26 + ord(ch) - ord("A") + 1 
    return val - 1

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
        colorama.init()

        # Calculate the maximum width of each cell in the board
        max_width = max(len(str(self.size)) + 1, max(
            len(str(self.board[i][j])) for i in range(self.size) for j in range(self.size)))
        # Print the column labels
        print(' ' * (max_width + 3), end='')

        for i in range(self.size):
            column_number = i + 1
            column_label = ""

            while column_number > 0:
                column_label = chr((column_number - 1) % 26 + ord('A')) + column_label
                column_number = (column_number - 1) // 26

            print(colorama.Fore.BLUE + column_label + colorama.Style.RESET_ALL,
                  end=' ' * (max_width - len(column_label) + 1))
        print()

        # Print the rows of the board with their corresponding row numbers
        for i, row in enumerate(self.board):
            print(colorama.Fore.BLUE + str(i + 1).rjust(max_width) +
                  colorama.Style.RESET_ALL, end=' ')
            for j in range(self.size):
                print(str(row[j]).rjust(max_width), end=' ')
            print()

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
            row_input = input("Enter row: ")
            col_input = input("Enter col: ")

            # Convert the row and column inputs to integer indices
            row = int(row_input) - 1
            col = string.ascii_uppercase.index(col_input.upper())

            if self.is_valid_move(row, col):
                if other_board.board[row][col] == 'S':
                    self.board[row][col] = 'X'
                    other_board.ships[row][col].sink()
                else:
                    self.board[row][col] = 'O'
                valid_input = True
            else:
                print("Invalid move. Try again.")

# define the game loop


def play_game():
    # initialize the boards
    board1 = Board(40, 5)
    board2 = Board(40, 5)

    # main game loop
    while True:
        # player 1's turn
        board1.handle_move(1, board2)
        board2.print_board()
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break

        # player 2's turn

        board2.handle_move(2, board1)
        board1.print_board()

    # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break
        clear_screen()

    # print the final boards
    print("Player 1's board:")
    board1.print_board()
    print("Player 2's board:")
    board2.print_board()


# start the game
play_game()
