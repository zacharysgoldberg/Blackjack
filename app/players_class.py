import secrets
import hashlib
from app.login_auth import main as login
from app import menu
import re
import random
from .wsgi import create_app
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

            first_name = name[0]
            first_letter_last = name[-1][0].capitalize()
            number = '{:01d}'.format(random.randrange(1, 999))
            username = '{}{}{}'.format(
                first_name, first_letter_last, number)
            self.user_login['username'] = username

            # Confirmusername does not exist
            exists = login.confirm_registration(self.user_login['username'])

            full_name = self.user_login['full_name'].replace(" ", "")

            # Ensure username is at least 2 characters long and contains alphanumeric letters
            if exists is not None and len(self.user_login['username']) > 2 and full_name.isalpha():

                while True:
                    email = input('Enter email: ')
                    valid_email = self.check_email(email)
                    if valid_email == True:
                        self.user_login['email'] = email
                    else:
                        print('Invalid Email')

                    password = input('Enter Password: ').strip()

                    """ Custom Password hashing and salt"""
                    # key = hashlib.pbkdf2_hmac(
                    #     'sha256',  # The hash digest algorithm for HMAC
                    #     # Convert the password to bytes
                    #     password.encode('utf-8'),
                    #     self.user_login['salt'].encode('utf-8'),
                    #     100000  # It is recommended to use at least 100,000 iterations of SHA-256
                    # )
                    # # Add random salt to user password
                    # self.user_login['password'] = str(
                    #     key) + self.user_login['salt']

                    # Ensure password is at least 8 characters long
                    if len(password) >= 8:
                        self.user_login['password'] = password
                        print(
                            f"\n{self.user_login['username']} has been registered")
                        self.success = True
                        break

                    else:
                        print('Password must contain 8 characters')
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
