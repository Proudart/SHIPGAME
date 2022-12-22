# AdaShip
Ada advanced programming project
This code shows a battleship game made by Deividas Dapkus for advance progrmaing module part 2.

This is a Python implementation of the classic board game, Battleship.

uml diagram = Ada_battleship_uml.png
unittest = shipgame_unittests.py
best experience = on windows

**Initial plan**
a. The implementation of a battleship game is the issue that this code seeks to fix. Several ships are placed on a board for the game, and players take turns trying to sink their opponent's ships by predicting where they are on the board. The suggested remedy is to develop a programme that enables participants to participate in the game by entering their educated predictions and obtaining feedback on whether or not those guesses were correct.

b. The initial general solution is depicted in a UML-style diagram, along with classes for the Board and Ship objects and any other utility classes or functions required to control input/output and game flow. The relationships between these classes, as well as the methods and characteristics they each include, are also depicted in the diagram. Two board objects are created by the main game loop, and they can be used in the main game loop to produce their own ships.

c. The initial general solution is depicted in a UML-style diagram, along with classes for the Board and Ship objects and any other utility classes or functions required to control input/output and game flow. The relationships between these classes, as well as the methods and characteristics they each include, are also depicted in the diagram. Two board objects are created by the main game loop, and they can be used in the main game loop to produce their own ships.

d. The overall problem can be decomposed into several epic tasks, such as implementing the basic game flow, allowing the player to manually place ships on the board, and implementing the logic for guessing and sinking ships.
-Get the basic classes down e.g Board and Ship.
-Get the parameters of the classes like health, ship length and the placement of the ships.
-Create functions for the classes to interact with the parameters like ships and health

e. Initial object-oriented design ideas  include creating classes for the Board and Ship and defining appropriate attributes and methods for each class to manage the game's data and behaviour. The problem could then be further broken down into smaller tasks, such as implementing the place_ships method or the logic for checking if a ship has been sunk. These tasks could be organised into a phased breakdown, with each phase focusing on a specific aspect of the game's functionality like turns, attacking the other player and auto placing the ships.


**Development**
a. The initial general solution is depicted in a UML-style diagram, along with classes for the Board and Ship objects and any other utility classes or functions required to control input/output and game flow. The relationships between these classes, as well as the methods and characteristics they each include, are also depicted in the diagram. Two board objects are created by the main game loop, and they can be used in the main game loop to produce their own ships.
b. During the first development phase, tasks could include implementing the basic structure of the game, including creating the Board and Ship classes and defining their attributes and methods. Code review and changes at this stage might involve refactoring code to make it more readable or efficient, or adding additional functionality as needed. These tasks and changes are linked to the analysis and decomposition of the problem into epic tasks and the initial object-oriented design ideas.
c. This process would be repeated for each subsequent development phase, with tasks and code review focused on adding or refining specific features or functionality.
Like at the end of development where you would refactor your code and put it into different files to make it easier for a person to read.
d. In the final development phase, tasks could include testing the game to ensure that it is working correctly and fixing any bugs that are discovered that could be achieved with unit tests.
e. It would be crucial to thoroughly test the game and address any faults found in order to guarantee quality. This could entail creating unit tests to verify the behaviour of certain game elements or manually playing the entire game to make sure everything works as it should. These initiatives are connected to the overall issue, the suggested fix, and the development methodologies and phases.
f. Key design challenges during development might include implementing the logic for guessing and sinking ships or managing the game flow and user input. Innovations could include adding additional features or functionality to the game, such as allowing the player to choose the position of their ships or providing feedback on the accuracy of their guesses. The difficulties I encountered were how to obtain the other person's placement; at first, I tried hiding it in the same board, but that proved ineffective, so I created a new parameter that was hidden from the players when playing and only shown when played. 

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

Some logic to check if the ship is correctly placed


**Evaluation**

a. Refactoring was a big part of this project as it meant I could quickly get something running and then refactor it if I needed to change it for later or for anyone else to see it. The biggest part of refactoring was separating the code into different files to make it easier to read and edit independently without messing anything else up.
Example: moving the two classes separately and isolating the Ship class as its only used to create ships and edit ship later when being moved.

class Ship:
    def __init__(self, length, name, icon, row, col, direction):
        self.length = length  # length of the ship
        self.name = name  # name of the ship
        self.sunk = False  # whether the ship has been sunk
        self.row = row  # row the ship is located on
        self.col = col  # column the ship is located on
        self.direction = direction  # direction the ship is facing (H for horizontal, V for vertical)
        self.health = length  # current health of the ship
        self.icon = icon  # icon representing the ship on the board
 
    # return whether the ship has been sunk
    def is_sunk(self):
        if self.health == 0:
            self.sunk = True
        return self.sunk
 
    # reduce the ship's health by 1 and set sunk to True if health reaches 0
    def hit(self):
        self.health -= 1
        if self.health == 0:
            self.sunk = True

Ship here being edited
 for i in range(len(self.ships)):
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

 
b. The code could be examined for chances to employ design patterns or other programming techniques to enhance its design or functionality. This could entail locating portions of the code where design patterns, such the factory pattern or the observer pattern, could be used to enhance the code's structure or maintainability.

Some examples of advanced techniques is the use of classes:
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

Another example is the use of arrays and the manipulation of them
 self.ship_board = []  # board showing ship locations
        # create empty board
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.board.append(row)

                if valid_placement:
                    # Place the ship vertically
                    for i in range(ship.length):
                                self.ship_board[row + i][col] = ship.icon
                    ship.row = row
                    ship.col = col
                    ship.direction = 'V'
                    return True

And using functions with a constant output like true or false.

c. It would be a good time to highlight any cutting-edge features or functionality that were added to the game during the evaluation period. This can contain features like extra game modes or player customisation choices. Examples of these characteristics and their advantages ought to be given.

Some of the features are going again if you hit an enemy ship and an enemy ai that guesses where your ships are:
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


Automatically and randomly placing the ships which required advanced ai model prediction to take the best place possible for the player not to guess:
row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

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



d. To enhance the game's performance or efficiency, better algorithms were investigated, devised, put into practice, and tested. This can entail locating computationally expensive portions of the code and looking into algorithms that could be applied to optimise these areas. Examples highlighting the advantages of these upgraded algorithms will be included in the documentation, along with the research, design, implementation, and testing.

Parts where performance was taken into account were during the ship placement phase as you do not want to brute force the code so that it does not take long and does not eat all of the resources
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



e. This project was quite fun to do but took longer than expected and is not the best when you are sick, but I think I did the best I could with the time taken to do it. However, there are several different things that I would change or add if I had more time or redone this project.
 
There are several opportunities to improve the code and enhance the gameplay experience. One potential improvement would be to allow the player to choose the difficulty level of the game, perhaps by adjusting the number of ships or the size of the board. Another improvement could be to add a scoring system that rewards the player for sinking ships quickly or with a minimum number of attacks.
 
Additionally, the code could be made more user-friendly by implementing a graphical user interface rather than relying on command-line input and output. This would allow the player to easily view the game board and make attacks using a mouse or touch screen.
 
Overall, this code provides a solid foundation for a Battleship game, and there is plenty of room for continued professional development to add new features and improve the gameplay experience.




**Requirements**

Python 3

colorama (for coloring text in the terminal)

configparser (for reading configuration settings from a file)

  

## Setup

Clone the repository to your local machine.

Install the required packages by running pip install -r requirements.txt in the terminal.

Create a file called configuration.ini in the root directory of the project and define the following settings:

board_size: the dimensions of the board (must be an integer)

ship_names: a comma-separated list of names for the ships (must be strings)

ship_sizes: a comma-separated list of sizes for the ships (must be integers)

ship_icons: a comma-separated list of single-character icons to represent the ships on the board (must be strings)

  

**Running the game**

To start the game, run the following command in the terminal:

python shipgame.py

You will be prompted to choose whether you or the computer will place the ships on the board. Follow the on-screen instructions to place your ships.

  

Once the ships have been placed, the game will begin. You and another player or the computer will take turns entering coordinates to attack. The game will end when all of one player's ships have been sunk.

  

## Customizing the game

You can customize the game by modifying the settings in the configuration.ini file. Change the board_size to adjust the dimensions of the board, and change the ship_names, ship_sizes, and ship_icons to customize the ships in the game. Make sure to match the lengths of the ship_names, ship_sizes, and ship_icons lists, as each ship's name, size, and icon should be in the same index in their respective lists.

  
  

The Ship class has the following attributes:

  

 - length: an integer representing the length of the ship
 - name: a string representing the name of the ship
 - sunk: a boolean indicating whether the ship has been sunk or not
 - row: an integer representing the row of the top left corner of the
   ship
 - col: an integer representing the column of the top left corner of the
   ship
 - direction: a string representing the direction in which the ship is
   placed on the board, either 'H' for horizontal or 'V' for vertical


 The Board class has the following attributes:

  

 - size: an integer representing the size of the board, i.e. the number
   of rows and columns
 - board: a 2D list of strings representing the current state of the
   board, where each string is either '-' for an unoccupied cell, 'S'
   for an occupied cell containing a ship, or 'X' for a cell that has
   been attacked
 - ship_board: a 2D list of strings representing the locations of the
   ships on the board, where each string is either '-' for an unoccupied
   cell or 'S' for an occupied cell containing a ship
 - ships: a list of Ship objects representing the ships on the board

The Board class has several methods:

  

 - print_ship: prints the name and length of each ship on the board
   
 - is_game_over: returns True if all ships on the board have been sunk, 
   and False otherwise

   
 

 - auto_place_ship: attempts to place a given ship on the board   
   automatically by first trying to place it horizontally, and if that  
   fails, trying to place it vertically

   

 - place_ships: prompts the player to enter the placement for each ship 
   on the board or to place the ship automatically

   

 - print_ships: prints the board with the ships placed on it

   

 - print_board: prints the board with the attacks made on it

   

 - is_valid_move: checks if a given move is a valid attack on the board

   

 - play_move: makes an attack on the board and updates the board and   
   ship states accordingly

   

 - play_game: the main game loop that handles player input, validation, 
   and game updates until the game is over.
