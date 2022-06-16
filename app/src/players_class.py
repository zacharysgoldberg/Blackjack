from . import menu
import re
from .. import db


################## Creating Players ##################

# [create dealer and player (empty hands)]


class Players:

    def __init__(self):

        self.user_login = {
            'full_name': None,
            'username': None,
            'email': None,
            'password': None
        }

    # [ensure email is valid]
    def check_email(self, email):
        regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if regex.fullmatch(email):
            return True

        else:
            return False

     # [confirm user doest not exist in db]

    def confirm_registration(self, username):
        exists = db.exists(username)
        return exists

    # [prompt user to register an account]

    def register(self):
        while True:
            self.user_login['full_name'] = input(
                'Enter full name to register: ')
            full_name = self.user_login['full_name'].replace(" ", "")

            email = input('Enter email: ')
            # [validate email and that it is not already in use]
            valid_email = self.check_email(email)
            username = email.split('@')[0]
            self.user_login['username'] = username

            # [confirm username does not exist]
            exists = self.confirm_registration(
                self.user_login['username'])
            menu.clear_console()

            # [ensure full name is at least 2 characters long and contains only letters]
            if exists == 0 and len(self.user_login['full_name']) > 2 and full_name.isalpha():
                while True:
                    user = db.hexists(username, email)
                    if valid_email == True and user == 0:
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

            elif exists == 1:
                print("Username already exists")

        # [add new user info to db]
        menu.new_register(self.user_login['full_name'], self.user_login['username'],
                          self.user_login['email'], self.user_login['password'])


players = Players()
