# add handlers for user input and import variables from player_class/game_class
from flask import Blueprint, jsonify, abort, request
from ..models.models import Leaderboard, db, User
import hashlib
import secrets
import sqlalchemy
import re
from datetime import datetime


bp = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')

# Getting users/scores


@bp.route('')
def index():
    user = Leaderboard.query.all()
    result = [u.serialize() for u in user]
    return jsonify(result)


@bp.route('/<int:id>')
def get_score(id: int):
    user = Leaderboard.query.get_or_404(id)
    return jsonify(user.serialize())


# Update scores


@ bp.route('/<int:id>', methods=['PATCH'])
def update_score(id: int):
    leaderboard = Leaderboard.query.get_or_404(id)

    wins = int(leaderboard.wins) + int(request.json['wins'])
    losses = int(leaderboard.losses) + int(request.json['losses'])

    leaderboard.wins = wins
    leaderboard.losses = losses

    db.session.commit()

    return jsonify(leaderboard.serialize())

# Delete scores from leaderboard


@ bp.route('/<int:id>', methods=['DELETE'])
def delete_score(id: int):
    score = Leaderboard.query.get_or_404(id)

    try:
        db.session.delete(score)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
