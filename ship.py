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