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
    def __init__(self, length, name, row, col, direction):
        self.length = length
        self.name = name
        self.sunk = False
        self.row = row
        self.col = col
        self.direction = direction

    def is_sunk(self):
        return self.sunk

    def sink(self):
        self.sunk = True

# define a Board class to represent the game board


class Board:
    def __init__(self, size, num_ships):
        self.size = size
        self.board = []
        self.ship_board = []

        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.board.append(row)

        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.ship_board.append(row)
        self.ships = []
        for i in range(num_ships):
            self.ships.append(Ship(ship_sizes[i], ship_names[i], 0, 0, 'H'))
    
    def print_ship(self):
        for i in range(len(self.ships)):
            print(self.ships[i].name, self.ships[i].length)

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def auto_place_ship(self, ship):
        # Try to place the ship horizontally
        for row in range(self.size):
            for col in range(self.size - ship.length + 1):
                valid_placement = True
                for i in range(ship.length):
                    if self.ship_board[row][col + i] == 'S':
                        valid_placement = False
                        break
                if valid_placement:
                    # Place the ship horizontally
                    for i in range(ship.length):
                        self.ship_board[row][col + i] = 'S'
                    ship.row = row
                    ship.col = col
                    ship.direction = 'H'
                    return True

        # If horizontal placement failed, try to place the ship vertically
        for row in range(self.size - ship.length + 1):
            for col in range(self.size):
                valid_placement = True
                for i in range(ship.length):
                    if self.board[row + i][col] == 'S':
                        valid_placement = False
                        break
                if valid_placement:
                    # Place the ship vertically
                    for i in range(ship.length):
                        ship.row = row
                        ship.col = col
                        self.board[row + i][col] = 'S'
                    return True

        # If automatic placement failed, return False
        return False

    def place_ships(self, choice):
        # Place each ship on the board
        if choice == 'Player':
            for ship in self.ships:
                valid_placement = False
                while not valid_placement:
                    # Print the board and the ship placement prompt
                    self.print_ships()
                    print("Enter placement for ship %s (length %d):" % (
                        ship.name, ship.length), "<Enter AUTO to place automatically>")
                    row_input = input("Enter row: ").upper()
                    if row_input == 'AUTO':
                        self.auto_place_ship(ship)
                        print("Ship placed automatically.")
                        clear_screen()
                        break
                    col_input = input("Enter col: ").upper()
                    if col_input == 'AUTO':
                        self.auto_place_ship(ship)
                        clear_screen()
                        break

                    # Convert the row and column inputs to integer indices
                    row = int(row_input) - 1
                    col = get_column(col_input)
                    orientation = input("Enter orientation (H or V): ").upper()

                    # Check if the placement is valid
                    if orientation == 'H':
                        if col + ship.length > self.size:
                            print("Invalid placement. Try again.")
                            clear_screen()

                            continue
                        for i in range(ship.length):
                            if self.ship_board[row][col + i] == 'S':
                                print("Invalid placement. Try again.")
                                clear_screen()

                                break
                        else:
                            # Place the ship on the board
                            for i in range(ship.length):
                                self.ship_board[row][col + i] = 'S'

                            valid_placement = True
                    elif orientation == 'V':
                        if row + ship.length > self.size:
                            print("Invalid placement. Try again.")
                            clear_screen()

                            continue
                        for i in range(ship.length):
                            if self.ship_board[row + i][col] == 'S':
                                print("Invalid placement. Try again.")
                                clear_screen()

                                break
                        else:
                            # Place the ship on the board
                            for i in range(ship.length):
                                self.ship_board[row + i][col] = 'S'
                            valid_placement = True
                            clear_screen()

                    else:
                        print("Invalid orientation. Try again.")

                    # Clear the screen
        elif choice == 'Computer':
            for ship in self.ships:
                if not self.auto_place_ship(ship):
                    print("Error: automatic ship placement failed.")
                    return False
        
    def hide_ships(self):
        print("SHIPSSS")
        self.print_ships()
        self.print_board()
        print("SHIPSSS2")

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'S':
                    self.board[i][j] = '-'
        
        print("WIPED")
        self.print_ships()
        self.print_board()
        print("WIPED2")

    def print_ships(self):
        colorama.init()

        # Calculate the maximum width of each cell in the board
        max_width = max(len(str(self.size)) + 1, max(
            len(str(self.ship_board[i][j])) for i in range(self.size) for j in range(self.size)))
        # Print the column labels
        print(' ' * (max_width + 3), end='')

        for i in range(self.size):
            column_number = i + 1
            column_label = ""

            while column_number > 0:
                column_label = chr((column_number - 1) %
                                   26 + ord('A')) + column_label
                column_number = (column_number - 1) // 26

            print(colorama.Fore.BLUE + column_label + colorama.Style.RESET_ALL,
                  end=' ' * (max_width - len(column_label) + 1))
        print()

        # Print the rows of the board with their corresponding row numbers
        for i, row in enumerate(self.ship_board):
            print(colorama.Fore.BLUE + str(i + 1).rjust(max_width) +
                  colorama.Style.RESET_ALL, end=' ')
            for j in range(self.size):
                print(str(row[j]).rjust(max_width), end=' ')
            print()

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
                column_label = chr((column_number - 1) %
                                   26 + ord('A')) + column_label
                column_number = (column_number - 1) // 26

            print(colorama.Fore.RED + column_label + colorama.Style.RESET_ALL,
                  end=' ' * (max_width - len(column_label) + 1))
        print()

        # Print the rows of the board with their corresponding row numbers
        for i, row in enumerate(self.board):
            print(colorama.Fore.RED + str(i + 1).rjust(max_width) +
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


        print("Player %d's turn:" % player)


        comeback = True
        
        
        while comeback == True:

            self.print_board()

            other_board.print_ships()

            row_input = input("Enter row: ")
            col_input = input("Enter col: ").upper()

            # Convert the row and column inputs to integer indices
            row = int(row_input) - 1
            col = get_column(col_input)

            if other_board.ship_board[row][col] == 'S':
                self.board[row][col] = 'H'
                self.check_hit(row, col)
                if self.is_game_over():
                    self.print_board()
                    print("Game over! You won!")
                    comeback = False
                    return True  
                else:
                    self.print_board()
                    print("Hit!")
                    comeback = True
            elif self.board[row][col] == 'H' or self.board[row][col] == 'M':
                self.print_board()
                print("You already guessed that location.")
                comeback = True
            else:
                self.board[row][col] = 'M'
                self.print_board()
                print("Miss.")
                comeback = False
                return False

    def check_hit(self, row, col):
        for ship in self.ships:
            if ship.row == row and ship.col == col:
                ship.sink()
                return
            elif ship.direction == 'H':
                if ship.row == row and col in range(ship.col, ship.col + ship.length):
                    ship.sink()
                    return
            elif ship.direction == 'V':
                if col == ship.col and row in range(ship.row, ship.row + ship.length):
                    ship.sink()
                    return

# define the game loop


def play_game():
    # initialize the boards
    board1 = Board(board_size, len(ship_sizes))
    board2 = Board(board_size, len(ship_sizes))

    # menu

    print("Welcome to Battleship!")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Player vs Player")
        choice1 = "Player"
        choice2 = "Player"
    elif choice == "2":
        print("Player vs Computer")
        choice1 = "Player"
        choice2 = "Computer"

    # place the ships on the boards

    board1.place_ships(choice1)
    #board1.hide_ships()
    board2.place_ships(choice2)
    #board2.hide_ships()

    # main game loop
    print("All ships placed. Let's play!")
    while True:
        # player 1's turn

        board1.handle_move(1, board2)
        clear_screen()
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break

        # player 2's turn

        board2.handle_move(2, board1)
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
