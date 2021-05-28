class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.choices = ["rock", "paper", "sissors"]

    
    def player_win_output(self, player):
        return f'{player.name} wins by playing {player.choice}'


