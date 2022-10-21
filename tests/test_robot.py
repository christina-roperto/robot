import unittest
from unittest.mock import patch
from robot import Robot


class TestRobotPlacement(unittest.TestCase):
    def test_constructor(self):
        robot = Robot()
        self.assertIsInstance(robot, Robot)

    def test_ask_for_input(self):
        robot = Robot()
        with patch('builtins.input', return_value="COMMAND"):
            actual = robot.ask_for_input()
        expected = ["COMMAND", ""]
        self.assertEqual(expected, actual)

    def test_parse_command_returns_command_in_uppercase(self):
        robot = Robot()
        actual = robot.parse_command('command subcommand')
        self.assertEqual(['COMMAND', 'SUBCOMMAND'], actual)

    def test_parse_command_returns_command_with_one_subcommand(self):
        robot = Robot()
        actual = robot.parse_command('command subcommand another')
        self.assertEqual(['COMMAND', 'SUBCOMMAND ANOTHER'], actual)

    def test_parse_command_always_provides_subcommand(self):
        robot = Robot()
        actual = robot.parse_command('SINGLE_COMMAND')
        self.assertEqual(['SINGLE_COMMAND', ''], actual)

    def test_place_works(self):
        r = Robot()
        r.place("1,3,EAST")
        self.assertEqual(1, r.x)
        self.assertEqual(3, r.y)
        self.assertEqual(Robot.EAST, r.facing)
        self.assertTrue(r.placed)

    def test_place_ignored_if_argument_count_invalid(self):
        r = Robot()
        actual = r.place("1,3")
        self.assertEqual(None, actual)

    def test_place_works_even_if_whitespaces_in_position(self):
        r = Robot()
        r.place("1      , 3,EAST")
        self.assertEqual(1, r.x)
        self.assertEqual(3, r.y)
        self.assertTrue(r.placed)

    def test_place_works_even_if_whitespaces_in_facing(self):
        r = Robot()
        actual = r.place("1, 3,        EAST    ")
        self.assertEqual(Robot.EAST, r.facing)
        self.assertTrue(r.placed)

    def test_place_ignored_if_position_is_not_an_integer(self):
        r = Robot()
        actual = r.place("x, y, EAST ")
        self.assertEqual(None, actual)

    def test_place_ignored_if_x_below_minimum(self):
        r = Robot()
        actual = r.place("-5,3,EAST")
        self.assertEqual(None, actual)

    def test_place_ignored_if_x_above_maximum(self):
        r = Robot()
        actual = r.place("7,3,EAST")
        self.assertEqual(None, actual)

    def test_place_ignored_if_y_below_minimum(self):
        r = Robot()
        actual = r.place("1,-5,EAST")
        self.assertEqual(None, actual)

    def test_place_ignored_if_y_above_maximum(self):
        r = Robot()
        actual = r.place("1,7,EAST")
        self.assertEqual(None, actual)

    def test_place_ignored_if_facing_is_invalid(self):
        r = Robot()
        actual = r.place("1,3, blabla")
        self.assertEqual(None, actual)

    def test_left_requires_placed_first(self):
        r = Robot()
        r.left()
        self.assertFalse(r.placed)
        r.place("1,3,EAST")
        self.assertTrue(r.placed)

    def test_right_requires_placed_first(self):
        r = Robot()
        r.right()
        self.assertFalse(r.placed)
        r.place("1,3,EAST")
        self.assertTrue(r.placed)

    def test_move_requires_placed_first(self):
        r = Robot()
        r.move()
        self.assertFalse(r.placed)
        r.place("1,3,EAST")
        self.assertTrue(r.placed)



if __name__ == "__main__":
    unittest.main()
