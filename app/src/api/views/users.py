# add handlers for user input and import variables from player_class/game_class
from flask import Blueprint, jsonify, abort, request
from ..models.models import Leaderboard, User, db
import hashlib
import sqlalchemy

# from ..blackjack_modules.game_class import user_login, successful

bp = Blueprint('users', __name__, url_prefix='/users')


# Read


@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = [u.serialize() for u in users]
    return jsonify(result)


@bp.route('/<int:id>')
def get_user(id: int):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())


# Create user and leaderboard score

"""
@bp.route('', methods=['POST'])
def create_user():

    # if successful == False:
    length = [len(request.json['username']), len(request.json['password'])]
    lst = ['username', 'password']

    if length[0] < 3 or length[1] < 8 or any(item not in request.json for item in lst):
        return abort(400)

    # request.json['full_name'] = user_login['full_name']
    # request.json['username'] = user_login['username']
    # request.json['password'] = user_login['passowrd']
    # request.json['date_of_birth'] = user_login['date_of_birth']
    # request.json['email'] = user_login['email']

    score = Leaderboard(
        username=new_game.username,
        wins=None,
        losses=None,
        last_game=None
    )

    db.session.add(score)

    user = User(
        full_name=new_game.full_name,
        username=new_game.username,
        password=new_game.password,
        email=new_game.email,
        leaderboard_id=db.session.query(Leaderboard.id).filter(
            Leaderboard.username == new_game.username)
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize())
"""

# Update


@ bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    user = User.query.get_or_404(id)
    lst = ['username', 'password', 'email']
    valid_email = players.check_email(request.json['email'])
    if all(item not in request.json for item in lst):
        return abort(400)

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        user.username = request.json['username']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        # user.password = hashpass(request.json['password'])

    if 'email' in request.json:
        if valid_email is False:
            return abort(400)
        user.email = request.json['email']

    try:
        db.session.commit()
        return jsonify(user.serialize())

    except:
        return jsonify(False)


# Delete

@ bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
