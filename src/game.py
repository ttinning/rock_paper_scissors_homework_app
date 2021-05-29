import random

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.game_list = ["rock", "paper", "scissors"]
    
    def player_win_output(self, player):
        return f'{player.name} wins by playing {player.choice}'

    def result(self):
        self.check_for_player()
        if self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_win_output(self.player_1)

        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_win_output(self.player_1)

        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_win_output(self.player_1)
        
        elif self.player_1.choice == self.player_2.choice:
            return None

        return self.player_win_output(self.player_2)

    def check_for_player(self):
        if self.player_2.choice == None:
            self.get_random_computer_player(self.player_2)

    def get_random_computer_player(self, player_2):
        player_2.choice = random.choice(self.game_list)
        player_2.name = "Grand Master"


    

