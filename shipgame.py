import configparser
from board import Board
from universal import clear_screen

# read configuration settings from configuration.ini file
config = configparser.ConfigParser()
config.read('configuration.ini')
board_size = config.getint('game', 'board_size')
ship_names = config.get('game', 'ship_names').split(',')
ship_sizes = config.get('game', 'ship_sizes').split(',')
ship_sizes = [int(size) for size in ship_sizes]
ship_icons = config.get('game', 'ship_icons').split(',')


# define the game loop
def play_game():

    clear_screen()
    print("Welcome to Battleship!")
    # menu
    while True:
        try:
            print("<1. Player vs Player>")
            print("<2. Player vs Computer>")
            print("<3. Quit>")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Player vs Player")
                choice1 = "Player"
                choice2 = "Player"
                break
            elif choice == 2:
                print("Player vs Computer")
                choice1 = "Player"
                choice2 = "Computer"
                break
            elif choice == 3:
                print("Quit")
                break
            else:
                clear_screen()
                print("Invalid choice")
        except:
            clear_screen()
            print("Invalid choice")
            continue

    clear_screen()
    custom = False
    while True:
        try:
            print("<1. Default Board Size 10x>")
            print("<2. Custom Board Size>")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Default")
                custom = False
                break
            elif choice == 2:
                print("Custom")
                custom = True
                break
            else:
                clear_screen()
                print("Invalid choice")
        except:
            clear_screen()
            print("Invalid choice")
            continue

    while custom:
        try:

            print("<Select the size of the ship default is 10>")
            print("<Maximum is 80 Minimum is 5>")
            size = int(input("Enter the size of the board: "))
            print(size)
            if size > 80:
                size = 80
                print("Board size is too big, defaulting to 80")
            elif size < 5:
                size = 5
                print("Board size is too small, defaulting to 5")

        except:

            clear_screen()
            print("Invalid input, try again")
            continue

        break

    # initialize the boards
    if custom:
        board1 = Board(size, len(ship_sizes))
        board2 = Board(size, len(ship_sizes))

    else:
        board1 = Board(board_size, len(ship_sizes))
        board2 = Board(board_size, len(ship_sizes))
    # place the ships on the boards

    board1.place_ships(choice1)
    board2.place_ships(choice2)

    # main game loop
    print("All ships placed. Let's play!")
    while True:
        # player 1's turn

        board1.handle_move(1, board2, "1")
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break

        # player 2's turn

        board2.handle_move(2, board1, choice1)
        # check if the game is over
        if board1.is_game_over() or board2.is_game_over():
            break


# start the game
if __name__ == '__main__':
    play_game()
