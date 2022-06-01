import secrets
from . login_auth import auth as login
from . import menu
import re
import random
from ... import create_db
from app.models import Leaderboard, session, User


################## Creating Players ##################

# [create dealer and player (empty hands)]


class Players:

    def __init__(self):
        self.db = create_db()

        self.user_login = {'salt': secrets.token_hex(16),
                           'full_name': None,
                           'username': None,
                           'email': None,
                           'password': None}

    # [ensure email is valid]
    def check_email(self, email):
        regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if regex.fullmatch(email):
            return True

        else:
            return False

    # [prompt user to register an account]

    def register(self):
        while True:
            self.user_login['full_name'] = input(
                'Enter full name to register: ')
            name = self.user_login['full_name'].lower(
            ).title().strip().split(" ")

            # [generate username from full name]
            first_name = name[0]
            first_letter_last = name[-1][0].capitalize()
            number = '{:01d}'.format(random.randrange(1, 999))
            username = '{}{}{}'.format(
                first_name, first_letter_last, number)
            self.user_login['username'] = username

            # [confirm username does not exist]
            exists = login.confirm_registration(self.user_login['username'])
            menu.clear_console()

            full_name = self.user_login['full_name'].replace(" ", "")

            # [ensure full name is at least 2 characters long and contains only letters]
            if exists is None and len(self.user_login['full_name']) > 2 and full_name.isalpha():

                while True:
                    email = input('Enter email: ')
                    # [validate email and that it is not already in use]
                    valid_email = self.check_email(email)
                    exists = session.query(User.id).filter(
                        User.email == email).first()
                    menu.clear_console()

                    if valid_email == True and exists is None:
                        self.user_login['email'] = email
                    else:
                        print('Invalid Email or Email is already in use')
                        continue

                    password = input('Enter Password: ').strip()

                    # [ensure password is at least 8 characters long]
                    if len(password) >= 8:
                        self.user_login['password'] = password
                        self.success = True
                        break

                    else:
                        print('Password must contain 8 characters')
                        continue

                break

            elif len(self.user_login['username']) < 2:
                print('Username must have at least 2 alphanumeric letters')

            elif exists == True:
                print("Username already exists")

        # [add new user to postgres leaderboard]
        menu.add_user_to_leaderboard(self.user_login['username'], 0, 0, None)
        # [add new user info to db]
        menu.new_register(self.user_login['full_name'], self.user_login['username'],
                          self.user_login['email'], self.user_login['password'])


players = Players()
