import os
import csv
from csv import writer
from .api.models.models import User, Leaderboard, db
from sqlalchemy import insert
import sqlalchemy
import random
from werkzeug.security import generate_password_hash


############ Menu ###########


def main_menu():
    print("")
    print("          === Blackjack Menu ===          ")
    print("------------------------------------------")
    print("|      1.  Login        | 2.  Register    |")
    print("------------------------------------------")
    print('|               3.  Exit                  |')
    print('------------------------------------------')
    return input(
        '\nSelect option\n').strip()


def logged_in_menu():
    print("")
    print("          === Account Menu ===          ")
    print("------------------------------------------")
    print("|     1. Play      | 2.  Manage Account   |")
    print("------------------------------------------")
    print('|              3.  Logout                 |')
    print('------------------------------------------')
    return input('\nSelect option\n').strip()

# clear command line UI


def clear_console():
    command = 'clear'
    # If program is running on Windows, use cls
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# Add new user to db


def new_register(full_name, username, email, password):
    leaderboard_id = db.session.query(Leaderboard.id).filter(
        Leaderboard.username == username).first()[0]

    # assigning new user id using length of number of records
    new_user = User(full_name=full_name, username=username, email=email,
                    password=generate_password_hash(password, method='sha256'), leaderboard_id=leaderboard_id)

    db.session.add(new_user)
    db.session.commit()
    clear_console()
    print(
        f"\n{username} has been registered")


# Adding user null results to postgres leaderboard for tallyings
def add_user_to_leaderboard(username, wins, losses, last_game):
    score = Leaderboard(username=username, wins=wins,
                        losses=losses, last_game=last_game)

    db.session.add(score)
    db.session.commit()
