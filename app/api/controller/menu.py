import os
import csv
from ...models import User, Leaderboard, session
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

# [clear command line UI]


def clear_console():
    command = 'clear'
    # [if program is running on Windows, use cls]
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# [add new user to db]


def new_register(full_name, username, email, password):
    leaderboard_id = session.query(Leaderboard.id).filter(
        Leaderboard.username == username).first()[0]

    # [assigning new user id using length of number of records]
    new_user = User(full_name=full_name, username=username, email=email,
                    password=generate_password_hash(password, method='sha256'), leaderboard_id=leaderboard_id)

    session.add(new_user)
    session.commit()
    clear_console()
    print(
        f"\n{username} has been registered")


# [adding user null results to postgres leaderboard for tallyings]
def add_user_to_leaderboard(username, wins, losses, last_game):
    score = Leaderboard(username=username, wins=wins,
                        losses=losses, last_game=last_game)

    session.add(score)
    session.commit()
