import random
import os
import colorama
import configparser
# clear the console screen

config = configparser.ConfigParser()
config.read('configuration.ini')
board_size = config.getint('game', 'board_size')
ship_names = config.get('game', 'ship_names').split(',')
ship_sizes = config.get('game', 'ship_sizes').split(',')
ship_sizes = [int(size) for size in ship_sizes]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_column(code):
    val = 0
    for ch in code:
        val = val * 26 + ord(ch) - ord("A") + 1
    return val - 1

# define a Ship class to represent each ship


class Ship:
    def __init__(self, length, name):
        self.length = length
        self.name = name
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
            self.ships.append(Ship(ship_sizes[i], ship_names[i]))

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def place_ships(self):
        # Place each ship on the board
        for ship in self.ships:
            valid_placement = False
            while not valid_placement:
                # Print the board and the ship placement prompt
                self.print_board()
                print("Enter placement for ship %s (length %d):" % (ship.name, ship.length))
                row_input = input("Enter row: ")
                col_input = input("Enter col: ").upper()

                # Convert the row and column inputs to integer indices
                row = int(row_input) - 1
                col = get_column(col_input)
                orientation = input("Enter orientation (H or V): ").upper()

                # Check if the placement is valid
                if orientation == 'H':
                    if col + ship.length > self.size:
                        print("Invalid placement. Try again.")
                        continue
                    for i in range(ship.length):
                        if self.board[row][col + i] == 'S':
                            print("Invalid placement. Try again.")
                            break
                    else:
                        # Place the ship on the board
                        for i in range(ship.length):
                            self.board[row][col + i] = 'S'
                        valid_placement = True
                elif orientation == 'V':
                    if row + ship.length > self.size:
                        print("Invalid placement. Try again.")
                        continue
                    for i in range(ship.length):
                        if self.board[row + i][col] == 'S':
                            print("Invalid placement. Try again.")
                            break
                    else:
                        # Place the ship on the board
                        for i in range(ship.length):
                            self.board[row + i][col] = 'S'
                        valid_placement = True
                else:
                    print("Invalid orientation. Try again.")

                # Clear the screen
                clear_screen()

    def print_ships(self):
        # Print the column labels
        print('  ' + ' '.join(chr(ord('A') + i) for i in range(self.size)))

        # Print each row with its corresponding row number and the ship cells
        for i, row in enumerate(self.board):
            print(str(i + 1) + ' ' + ' '.join(cell if cell !=
                  'S' else '#' for cell in row))

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
            col_input = input("Enter col: ").upper()

            # Convert the row and column inputs to integer indices
            row = int(row_input) - 1
            col = get_column(col_input)

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
    board1 = Board(board_size, len(ship_sizes))
    board2 = Board(board_size, len(ship_sizes))

    board1.place_ships()
    board2.place_ships()

    # main game loop
    while True:
        # player 1's turn
        board1.handle_move(1, board2)
        board2.print_board()
        board1.print_ships()  # Print the ships for player 1
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break
        clear_screen()

        # player 2's turn
        board2.handle_move(2, board1)
        board1.print_board()
        board2.print_ships()  # Print the ships for player 2
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break
        clear_screen()

    # print the final boards
    print("Player 1's board:")
    board1.print_board()
    print("Player 1's ships:")
    board1.print_ships()
    print("Player 2's board:")
    board2.print_board()
    print("Player 2's ships:")
    board2.print_ships()


# start the game
play_game()
