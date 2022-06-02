from ... import db
import json
from . import game_class as game
from . import win_lose
from .menu import clear_console

# [update scores in leaderboard]


class UpdateScore():
    def __init__(self):
        pass

    # [insert new scores]
    def insert(self, player):
        user = json.loads(db.execute_command('JSON.GET', player))

        wins = int(user['score']['wins']) + int(win_lose.total_wins)
        losses = int(user['score']['losses']) + int(win_lose.total_losses)

        user['score']['wins'] = wins
        user['score']['losses'] = losses

        db.execute_command('JSON.SET', player, '.', json.dumps(user))

        db.save()
        clear_console()


update = UpdateScore()
