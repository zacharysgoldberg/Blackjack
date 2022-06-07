import os
from .. import db
import json
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


def new_register(full_name, username, email, password, wins=0, losses=0, last_game='None'):
    record = {
        'profile': {
            'full_name': full_name,
            'username': username,
            'password': generate_password_hash(password, method='sha256')
        },
        'score': {
            "wins": wins,
            "losses": losses,
            "last_game": last_game
        }
    }
    db.execute_command('JSON.SET', email, '.', json.dumps(record))

    db.save()
    clear_console()
    print(
        f"\n{username} has been registered")
