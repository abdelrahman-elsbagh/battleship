import unittest

from battleship.ship import Ship


class TestSampleClass(unittest.TestCase):

    ship = Ship()
    created_ships = {
        "ships": [
            {
                "x": 2,
                "y": 1,
                "size": 4,
                "direction": "H"
            },
            {
                "x": 7,
                "y": 4,
                "size": 3,
                "direction": "V"
            },
            {
                "x": 3,
                "y": 5,
                "size": 2,
                "direction": "V"
            },
            {
                "x": 6,
                "y": 8,
                "size": 1,
                "direction": "H"
            }
        ]
    }

    created_ships_out_board = {
        "ships": [
            {
                "x": 2,
                "y": 11,
                "size": 4,
                "direction": "H"
            },
            {
                "x": 7,
                "y": 4,
                "size": 3,
                "direction": "V"
            },
            {
                "x": 3,
                "y": 5,
                "size": 2,
                "direction": "V"
            },
            {
                "x": 6,
                "y": 8,
                "size": 1,
                "direction": "H"
            }
        ]
    }

    def test_start_new_game(self):
        self.assertTrue(self.ship.start_new_game(self.created_ships))
        self.assertFalse(self.ship.start_new_game(self.created_ships_out_board))

    def test_delete_game(self):
        self.assertTrue(self.ship.delete_game())

    def test_check_shot(self):
        points = [[2, 1], [2, 2], [2, 3], [2, 4]]
        success_shot = [2, 1]

        self.assertEqual(self.ship.check_shot(points, success_shot, 'ship1'), "HIT")


    def test_is_match_shot(self):
        points = [[2, 1], [2, 2], [2, 3], [2, 4]]
        success_shot = [2, 1]
        failed_point = [2, 7]
        self.assertTrue(self.ship.is_match_shot(points, success_shot))
        self.assertFalse(self.ship.is_match_shot(points, failed_point))

    def test_is_last_point(self):
        points = [[2, 1], [2, 2], [2, 3], [2, 4]]
        rest_points = [[2, 3]]
        self.assertTrue(self.ship.is_last_point(rest_points))
        self.assertFalse(self.ship.is_last_point(points))
if __name__=="__main__":
    unittest.main()
