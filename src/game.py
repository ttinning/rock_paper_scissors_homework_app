class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    
    def player_win_output(self, player):
        return f'{player.name} wins by playing {player.choice}'

    def result(self):
        if self.player_1.choice == "rock" and self.player_2.choice == "sissors":
            return self.player_win_output(self.player_1)

        elif self.player_1.choice == "sissors" and self.player_2.choice == "paper":
            return self.player_win_output(self.player_1)

        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_win_output(self.player_1)

        return self.player_win_output(self.player_2)


