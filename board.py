import colorama
import configparser
import random
import time
from ship import Ship
from universal import clear_screen, get_column

# read configuration settings from configuration.ini file
config = configparser.ConfigParser()
config.read('configuration.ini')
board_size = config.getint('game', 'board_size')
ship_names = config.get('game', 'ship_names').split(',')
ship_sizes = config.get('game', 'ship_sizes').split(',')
ship_sizes = [int(size) for size in ship_sizes]
ship_icons = config.get('game', 'ship_icons').split(',')

# class representing a ship in the game

# class representing the game board


class Board:
    def __init__(self, size, num_ships):
        """
        Constructor for the Board class. Initializes the size of the board, creates
        empty boards for the attack and ship locations, and creates a list of Ship
        objects.

        Parameters:
        size (int): The dimensions of the board (size x size).
        num_ships (int): The number of ships on the board.
        """
        self.size = size  # dimensions of the board
        self.board = []  # board showing attacks
        self.ship_board = []  # board showing ship locations
        # create empty board
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.board.append(row)
        # create empty ship board
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.ship_board.append(row)
        self.ships = []  # list of Ship objects on the board
        # create Ship objects
        for i in range(num_ships):
            self.ships.append(
                Ship(ship_sizes[i], ship_names[i], ship_icons[i], 0, 0, 'H'))

    def is_game_over(self):
        """
        Check if the game is over by checking if all of the ships have been sunk.
        Returns:
        bool: True if the game is over, False otherwise.
        """
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def auto_place_ship(self, ship):
        """
        Try to place the ship on the board automatically by randomly selecting a
        location and direction for the ship and checking if it is a valid placement.
        If the placement is valid, it places the ship and returns True. If it is not
        able to find a valid placement after 100 attempts, it returns False.

        Parameters:
        ship (Ship): The ship to be placed on the board.

        Returns:
        bool: True if the ship was placed successfully, False otherwise.
        """
        for i in range(len(self.ships)):
            while True:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                direction = random.choice(['H', 'V'])
                if direction == 'H':
                    if col + ship.length > self.size:
                        continue
                    valid_placement = True
                    for i in range(ship.length):
                        if any(icon in self.ship_board[row][col + i] for icon in ship_icons):
                            valid_placement = False
                            break
                    if valid_placement:
                        # Place the ship horizontally
                        for i in range(ship.length):
                            self.ship_board[row][col + i] = ship.icon
                        ship.row = row
                        ship.col = col
                        ship.direction = 'H'
                        return True
                else:
                        if row + ship.length > self.size:
                            continue
                        valid_placement = True
                        for i in range(ship.length):
                            if any(icon in self.ship_board[row + i][col] for icon in ship_icons):
                                valid_placement = False
                                break
                            valid_placement = True
                        if valid_placement:
                            # Place the ship vertically
                            for i in range(ship.length):
                                        self.ship_board[row + i][col] = ship.icon
                            ship.row = row
                            ship.col = col
                            ship.direction = 'V'
                            return True
        # If automatic placement failed, return False
        return False

    def place_ships(self, choice):
        """
        Place the ships on the board. The choice argument specifies whether the
        player or the computer will be placing the ships. If the player is placing
        the ships, the method prompts the player to enter the row and column where
        they want to place the ship, and the direction (horizontal or vertical). If
        the player enters 'AUTO', the method calls the auto_place_ship method to
        place the ship automatically. If the computer is placing the ships, the
        auto_place_ship method is called to place the ships automatically.

        Parameters:
        choice (str): 'Player' if the player is placing the ships, 'Computer' if the
                      computer is placing the ships.
        """
        clear_screen()
        # Place each ship on the board
        if choice == 'Player':
            for ship in self.ships:
                valid_placement = False
                while not valid_placement:
                    # Print the board and the ship placement prompt
                    self.print_ships()
                    print("Enter placement for ship %s (length %d):" % (
                        ship.name, ship.length), "<Enter AUTO to place automatically>")
                    while True:
                        try:
                            row_input = input("Enter row: ").upper()
                            if row_input == 'AUTO' or int(row_input) in range(1, self.size + 1):
                                break
                            clear_screen()
                            self.print_ships()
                            print("Enter placement for ship %s (length %d):" % (
                                ship.name, ship.length), "<Enter AUTO to place automatically>")
                            print("Invalid input. Try again.")
                        except:
                            clear_screen()
                            self.print_ships()
                            print("Enter placement for ship %s (length %d):" % (
                                ship.name, ship.length), "<Enter AUTO to place automatically>")
                            print("Invalid input. Try again.")

                    if row_input == 'AUTO':
                        self.auto_place_ship(ship)
                        print("Ship placed automatically.")
                        clear_screen()
                        break
                    while True:
                        try:
                            col_input = input("Enter col: ").upper()
                            if row_input == 'AUTO' or get_column(col_input) in range(self.size):
                                break
                            clear_screen()
                            self.print_ships()
                            print("Enter placement for ship %s (length %d):" % (
                                ship.name, ship.length), "<Enter AUTO to place automatically>")
                            print("Invalid input. Try again.")
                        except:
                            clear_screen()
                            self.print_ships()
                            print("Enter placement for ship %s (length %d):" % (
                                ship.name, ship.length), "<Enter AUTO to place automatically>")
                            print("Invalid input. Try again.")
                    if col_input == 'AUTO':
                        self.auto_place_ship(ship)
                        clear_screen()
                        break

                    # Convert the row and column inputs to integer indices
                    row = int(row_input) - 1
                    col = get_column(col_input)
                    while True:
                        try:
                            orientation = input(
                                "Enter orientation (H or V): ").upper()
                            if orientation in ['H', 'V']:
                                break
                            clear_screen()
                            self.print_ships()

                            print("Invalid input. Try again.")
                        except:
                            clear_screen()
                            self.print_ships()
                            print("Invalid input. Try again.")

                    # Check if the placement is valid
                    if orientation == 'H':
                        if col + ship.length > self.size:
                            print("Invalid placement. Try again.")
                            clear_screen()

                            continue
                        for i in range(ship.length):
                            if any(icon in self.ship_board[row][col + i] for icon in ship_icons):
                                print("Invalid placement. Try again.")
                                clear_screen()

                                break
                        else:
                            # Place the ship on the board
                            for i in range(ship.length):
                                self.ship_board[row][col + i] = ship.icon

                            valid_placement = True
                    elif orientation == 'V':
                        if row + ship.length > self.size:
                            print("Invalid placement. Try again.")
                            clear_screen()

                            continue
                        for i in range(ship.length):
                            if any(icon in self.ship_board[row + i][col] for icon in ship_icons):
                                clear_screen()
                                print("Invalid placement. Try again.")

                                break
                        else:
                            # Place the ship on the board
                            for i in range(ship.length):
                                self.ship_board[row + i][col] = ship.icon
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

    def print_ships(self):
        """
        Print the current state of the ship board, showing the location of the ships.
        """
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
        """
        Print the current state of the attack board, showing the locations where the
        player has attack.
        """
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
            print(colorama.Fore.GREEN + str(i + 1).rjust(max_width) +
                  colorama.Style.RESET_ALL, end=' ')
            for j in range(self.size):
                print(str(row[j]).rjust(max_width), end=' ')
            print()

    def handle_move(self, player, other_board, choice):
        """
        Handle a player's attack on the specified row and column of the board. If the
        attack hits a ship, the ship is damaged and the attack board is updated to
        show a hit. If the attack misses, the attack board is updated to show a miss.
        If the attack sinks a ship, the ship's sunk status is updated.

        Parameters:
        player (int): The player number.
        other_board (object): The other player's board.
        choice (str): if the opponent is a computer or a player
        """

        print("Player %d's turn:" % player)

        column_number = self.size
        column_label = ""

        while column_number > 0:
            column_label = chr((column_number - 1) %
                               26 + ord('A')) + column_label
            column_number = (column_number - 1) // 26

        comeback = True
        message = False
        while comeback == True:
            clear_screen()
            self.print_board()
            if message:
                print(message)
            if choice == '1':
                while True:
                    try:
                        row_input = input("Enter row: ").upper()
                        if int(row_input) in range(1, self.size + 1):
                            break
                        clear_screen()
                        self.print_board()
                        print("Invalid input. Max is %d. Try again." %
                              self.size)
                    except:
                        clear_screen()
                        self.print_board()
                        print("Invalid input. Max is %d. Try again." %
                              self.size)

                while True:
                    try:
                        col_input = input("Enter col: ").upper()
                        if get_column(col_input) in range(self.size):
                            break
                        clear_screen()
                        self.print_board()
                        print("Invalid input. Max is " +
                              column_label + " Try again.")

                    except:
                        clear_screen()
                        self.print_board()

                        print("Invalid input. Max is " +
                              column_label + " Try again.")

                # Convert the row and column inputs to integer indices
                row = int(row_input) - 1
                col = get_column(col_input)
            else:
                time.sleep(1)
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)

            if any(icon in other_board.ship_board[row][col] for icon in ship_icons) and self.board[row][col] != 'H':
                self.board[row][col] = 'H'
                self.check_hit(row, col)
                if self.is_game_over():
                    clear_screen()
                    print("Game over! You won! Player %d wins!" % player)
                    print("Player %d's board:" % player)
                    self.print_board()

                    print("Player %d's ships:" % player)
                    self.print_ships()
                    if player == 1:
                        player = 2
                    elif player == 2:
                        player = 1
                    print("Player %d's board:" % player)

                    other_board.board()
                    comeback = False
                    return True
                else:
                    self.print_board()
                    message = "Hit!"
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
        """
        Check if the attack at the specified row and column hit a ship. If the attack
        hit a ship, the ship is damaged and the method returns True. If the attack
        missed, the method returns False. If the attack sinks a ship, the ship's sunk
        status is updated.

        Parameters:
        row (int): The row where the attack took place.
        col (int): The column where the attack took place.

        Returns:
        bool: True if the attack hit a ship, False otherwise.
        """
        for ship in self.ships:
            if ship.row == row and ship.col == col:
                ship.hit()
                return
            elif ship.direction == 'H':
                if ship.row == row and col in range(ship.col, ship.col + ship.length):
                    ship.hit()
                    return
            elif ship.direction == 'V':
                if col == ship.col and row in range(ship.row, ship.row + ship.length):
                    ship.hit()
                    return
