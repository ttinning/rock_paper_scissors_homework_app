import unittest
from src.player import Player
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Jack Daniels", "paper")
        self.player_2 = Player("Jim Beam", "rock")
        self.player_3 = Player("Sailor Jerry", "paper")
        self.player_4 = Player(None, None)
        self.game_1 = Game(self.player_1, self.player_2)
        self.game_2 = Game(self.player_1, self.player_3)
        self.game_3 = Game(self.player_1, self.player_4)

    def test_game_1_shows_winner(self):
        expected = "Jack Daniels wins by playing paper"
        actual = self.game_1.result()
        self.assertEqual(expected, actual)

    def test_game_2_returns_none(self):
        expected = None
        actual = self.game_2.result()
        self.assertEqual(expected, actual)

    def test_cpu_is_available(self):
        self.game_3.result()
        expected = "Grand Master"
        actual = self.player_4.name
        self.assertEqual(expected, actual)