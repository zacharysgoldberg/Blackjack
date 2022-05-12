from app.api.models.models import User, Leaderboard, db
from ...wsgi import create_app
from . import game_class as game
from . import win_lose
from .menu import clear_console

# [update scores in leaderboard]


class UpdateScore():
    def __init__(self):
        self.app = create_app()
        self.app.app_context().push()

    # [insert new scores]
    def insert(self, player):
        id = db.session.query(
            Leaderboard.id).filter(Leaderboard.username == player).first()[0]

        # [retrieve user/leaderboard object based on id]
        leaderboard = Leaderboard.query.get(id)

        wins = int(leaderboard.wins) + int(win_lose.total_wins)
        losses = int(leaderboard.losses) + int(win_lose.total_losses)

        leaderboard.wins = wins
        leaderboard.losses = losses

        db.session.commit()
        clear_console()


update = UpdateScore()
