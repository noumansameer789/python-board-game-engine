import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from board_game.engine import Board, Game


class GameTest(unittest.TestCase):
    def test_turn_order_and_jump(self):
        game = Game(["A", "B"], board=Board(jumps={3: 11}))
        self.assertEqual(game.play_turn(3).position, 11)
        self.assertEqual(game.play_turn(2).name, "B")

    def test_validation(self):
        with self.assertRaises(ValueError):
            Game(["solo"])
        with self.assertRaises(ValueError):
            Game(["A", "A"])


if __name__ == "__main__":
    unittest.main()
