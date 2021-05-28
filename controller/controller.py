from flask import render_template, request
from app import app
from src.game import Game
from src.player import Player

@app.route("/")
def home():
    return render_template('home.html', title="Rock, Paper, Scissors!")

@app.route('/<choice_1>/<choice_2>')
def return_result(choice_1, choice_2):
    player_1 = Player("player_1", choice_1)
    player_2 = Player("player_2", choice_2)
    game = Game(player_1, player_2)
    winner = game.result()
    return render_template('result.html', winner=winner, choice_1 = choice_1, choice_2 = choice_2)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title="Welcome - Rock, Paper, Scissors!")

