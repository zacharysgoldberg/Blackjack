import secrets
import hashlib
from app.src.login_auth import auth as login
from app.src import menu
import re
import random
from ..wsgi import create_app
from app.src.models import Leaderboard, db, User


################## Creating Players ##################

# Create dealer and player (empty hands)


class Players:

    def __init__(self):
        self.app = create_app()
        self.app.app_context().push()
        self.user_login = {'salt': secrets.token_hex(16),
                           'full_name': None,
                           'username': None,
                           'email': None,
                           'password': None}

    # ensure email is valid
    def check_email(self, email):
        regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if regex.fullmatch(email):
            return True

        else:
            return False

    # Prompt user to register an account
    # Check if user already exists in CSV db, upload user info to CSV database
    def register(self):
        while True:
            self.user_login['full_name'] = input(
                'Enter full name to register: ')
            name = self.user_login['full_name'].lower(
            ).title().strip().split(" ")

            # Generate username from full name
            first_name = name[0]
            first_letter_last = name[-1][0].capitalize()
            number = '{:01d}'.format(random.randrange(1, 999))
            username = '{}{}{}'.format(
                first_name, first_letter_last, number)
            self.user_login['username'] = username

            # Confirm username does not exist
            exists = login.confirm_registration(self.user_login['username'])
            menu.clear_console()

            full_name = self.user_login['full_name'].replace(" ", "")

            # Ensure full name is at least 2 characters long and contains only letters
            if exists is None and len(self.user_login['full_name']) > 2 and full_name.isalpha():

                while True:
                    email = input('Enter email: ')
                    # validate email and that it is not already in use
                    valid_email = self.check_email(email)
                    exists = db.session.query(User.id).filter(
                        User.email == email).first()
                    menu.clear_console()

                    if valid_email == True and exists is None:
                        self.user_login['email'] = email
                    else:
                        print('Invalid Email or Email is already in use')
                        continue

                    password = input('Enter Password: ').strip()

                    # Ensure password is at least 8 characters long
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

        # Add new user to postgres leaderboard
        menu.add_user_to_leaderboard(self.user_login['username'], 0, 0, None)
        # Add new user info to db
        menu.new_register(self.user_login['full_name'], self.user_login['username'],
                          self.user_login['email'], self.user_login['password'])


players = Players()
