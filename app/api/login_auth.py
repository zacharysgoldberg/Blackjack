import json
from .menu import clear_console
from .. import db
from werkzeug.security import check_password_hash
import time


def login():
    print('\nLOGIN')

    while True:
        print('Press "q" at any time to return to the menu')
        email = input(
            "Enter email: ")
        if email == 'q':
            return None, None
        try:
            # [check if username exists]
            exists = db.exists(email)

            # [if username exists, prompt user for password]
            if exists == 1:
                user = json.loads(db.execute_command(
                    'JSON.GET', email, '.profile'))

                password_validate = input('Enter Password: ').strip()
                clear_console()
                # [checking user input against password in session]
                if check_password_hash(user['password'], password_validate) is True:
                    clear_console()
                    print('\nLogin Successfull')
                    time.sleep(2)
                    return user['username'], email

                else:
                    clear_console()
                    print('Incorrect password\n')
                    continue
            print('\nEmail does not exist')
            return None, None

        except BaseException as e:
            # clear_console()
            print('Invalid Credentials')
            print(e)
            return False
