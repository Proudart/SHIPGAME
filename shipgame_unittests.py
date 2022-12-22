import unittest
from board import Board
from ship import Ship

class TestBoard(unittest.TestCase):
    def test_is_game_over(self):
        board = Board(10, 2)
        ship1 = Ship(2, 'Ship 1', 'S', 0, 0, 'H')
        ship2 = Ship(3, 'Ship 2', 'S', 0, 0, 'H')
        board.ships = [ship1, ship2]
        
        # Test that game is not over when both ships are not sunk
        self.assertFalse(board.is_game_over())
        
        # Test that game is over when both ships are sunk
        ship1.sunk = True
        ship2.sunk = True
        self.assertTrue(board.is_game_over())
        
        # Test that game is not over when only one ship is sunk
        ship2.sunk = False
        self.assertFalse(board.is_game_over())

    def test_auto_place_ship(self):
        board = Board(10, 1)
        ship = Ship(3, 'Ship', 'S', 0, 0, 'H')
        
        # Test that ship is placed on board when there is space
        self.assertTrue(board.auto_place_ship(ship))
        self.assertEqual(board.ship_board[ship.row][ship.col], ship.icon)
        
        # Test that ship is not placed on board when there is no space
        board.ship_board = [['S' for _ in range(10)] for _ in range(10)]
        self.assertTrue(board.auto_place_ship(ship))

class TestShip(unittest.TestCase):
    def test_is_sunk(self):
        ship = Ship(2, 'Ship', 'S', 0, 0, 'H')
        
        # Test that ship is not sunk when health is greater than 0
        ship.health = 1
        self.assertFalse(ship.is_sunk())
        
        # Test that ship is sunk when health is 0
        ship.health = 0
        self.assertTrue(ship.is_sunk())
        
    def test_hit(self):
        ship = Ship(2, 'Ship', 'S', 0, 0, 'H')
        
        # Test that ship's health decreases by 1 when hit
        ship.hit()
        self.assertEqual(ship.health, 1)
        
        # Test that ship's health is 0 after two hits
        ship.hit()
        self.assertEqual(ship.health, 0)
    

        

if __name__ == '__main__':
    unittest.main()