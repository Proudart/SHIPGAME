# AdaShip
Ada advanced programming project
This code shows a battleship game made by Deividas Dapkus for advance progrmaing module part 2.

This is a Python implementation of the classic board game, Battleship.

uml diagram = Ada_battleship_uml.png
unittest = shipgame_unittests.py

Initial plan



Development

Evaluation



Requirements
Python 3
colorama (for coloring text in the terminal)
configparser (for reading configuration settings from a file)

Setup
Clone the repository to your local machine.
Install the required packages by running pip install -r requirements.txt in the terminal.
Create a file called configuration.ini in the root directory of the project and define the following settings:
board_size: the dimensions of the board (must be an integer)
ship_names: a comma-separated list of names for the ships (must be strings)
ship_sizes: a comma-separated list of sizes for the ships (must be integers)
ship_icons: a comma-separated list of single-character icons to represent the ships on the board (must be strings)

Running the game
To start the game, run the following command in the terminal:
python shipgame.py
You will be prompted to choose whether you or the computer will place the ships on the board. Follow the on-screen instructions to place your ships.

Once the ships have been placed, the game will begin. You and another player or the computer will take turns entering coordinates to attack. The game will end when all of one player's ships have been sunk.

Customizing the game
You can customize the game by modifying the settings in the configuration.ini file. Change the board_size to adjust the dimensions of the board, and change the ship_names, ship_sizes, and ship_icons to customize the ships in the game. Make sure to match the lengths of the ship_names, ship_sizes, and ship_icons lists, as each ship's name, size, and icon should be in the same index in their respective lists.


The Ship class has the following attributes:

length: an integer representing the length of the ship
name: a string representing the name of the ship
sunk: a boolean indicating whether the ship has been sunk or not
row: an integer representing the row of the top left corner of the ship
col: an integer representing the column of the top left corner of the ship
direction: a string representing the direction in which the ship is placed on the board, either 'H' for horizontal or 'V' for vertical
The Board class has the following attributes:

size: an integer representing the size of the board, i.e. the number of rows and columns
board: a 2D list of strings representing the current state of the board, where each string is either '-' for an unoccupied cell, 'S' for an occupied cell containing a ship, or 'X' for a cell that has been attacked
ship_board: a 2D list of strings representing the locations of the ships on the board, where each string is either '-' for an unoccupied cell or 'S' for an occupied cell containing a ship
ships: a list of Ship objects representing the ships on the board
The Board class has several methods:

print_ship: prints the name and length of each ship on the board
is_game_over: returns True if all ships on the board have been sunk, and False otherwise
auto_place_ship: attempts to place a given ship on the board automatically by first trying to place it horizontally, and if that fails, trying to place it vertically
place_ships: prompts the player to enter the placement for each ship on the board or to place the ship automatically
print_ships: prints the board with the ships placed on it
print_board: prints the board with the attacks made on it
is_valid_move: checks if a given move is a valid attack on the board
play_move: makes an attack on the board and updates the board and ship states accordingly
play_game: the main game loop that handles player input, validation, and game updates until the game is over.