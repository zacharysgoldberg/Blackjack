from app.models import User, Leaderboard, session
from ... import create_db
from . import game_class as game
from . import win_lose
from .menu import clear_console

# [update scores in leaderboard]


class UpdateScore():
    def __init__(self):
        self.db = create_db()

    # [insert new scores]
    def insert(self, player):
        # [retrieve user/leaderboard object]
        leaderboard = session.query(
            Leaderboard).filter_by(username=player).first()

        wins = int(leaderboard.wins) + int(win_lose.total_wins)
        losses = int(leaderboard.losses) + int(win_lose.total_losses)

        leaderboard.wins = wins
        leaderboard.losses = losses

        session.commit()
        clear_console()


update = UpdateScore()
