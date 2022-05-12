import os
from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///api/db/blackjack.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    from .api.models.models import User, Leaderboard, db
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all(app)
    # db.session.commit()

    # from .api import users, leaderboard
    # app.register_blueprint(users.bp)
    # app.register_blueprint(leaderboard.bp)

    return app
