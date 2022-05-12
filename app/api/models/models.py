from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

# [users table]


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(128), nullable=False,
                         unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    leaderboard_id = db.Column(db.Integer, db.ForeignKey('leaderboard.id'))

    def __init__(self, full_name: str, username: str,
                 password: str,
                 email: str, leaderboard_id: int):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
        self.leaderboard_id = leaderboard_id

# [leaderboard table]


class Leaderboard(db.Model):
    __tablename__ = 'leaderboard'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, index=True)
    wins = db.Column(db.BigInteger, nullable=True)
    losses = db.Column(db.BigInteger, nullable=True)
    last_game = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True)

    user = db.relationship(
        'User', backref='leaderboard', uselist=False)

    def __init__(self, username: str, wins: int, losses: int,
                 last_game: str):
        self.username = username
        self.wins = wins
        self.losses = losses
        self.last_game = last_game
