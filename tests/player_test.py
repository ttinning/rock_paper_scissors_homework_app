import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Johnnie Walker", "paper")

    def test_player_has_name(self):
        expected = "Johnnie Walker"
        actual = self.player.name
        self.assertEqual(expected, actual)

    def test_player_has_a_choice(self):
        expected = "paper"
        actual = self.player.choice
        self.assertEqual(expected, actual)