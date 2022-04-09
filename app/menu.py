import os
import csv
from csv import writer
from .src.models import User, Leaderboard, db
from sqlalchemy import insert
import sqlalchemy
import random
from werkzeug.security import generate_password_hash, check_password_hash


############ Menu ###########


def menu():
    print("")
    print("          === Blackjack Menu ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register        |")
    print("------------------------------------------")
    print('|              3. Exit                    |')
    print('------------------------------------------')
    return input(
        '\nSelect option\n').lower().strip()


# clear command line UI


def clear_console():
    command = 'clear'
    # If program is running on Windows, use cls
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# Add new user to db


def new_register(full_name, username, email, password):
    rows = db.session.query(User).count()
    new_user = User(full_name=full_name, username=username, email=email,
                    password=generate_password_hash(password, method='sha256'), leaderboard_id=rows + 1)

    db.session.add(new_user)
    db.session.commit()


# Adding user null results to postgres leaderboard for tallyings
def add_user_to_leaderboard(username, wins, losses, last_game):
    score = Leaderboard(username=username, wins=wins,
                        losses=losses, last_game=last_game)

    db.session.add(score)
    db.session.commit()