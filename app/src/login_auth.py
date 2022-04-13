import csv
import hashlib
import os.path
from app.src.models import User, db
from app.src.menu import clear_console
from ..wsgi import create_app
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
import time


class Auth():
    def __init__(self):
        self.app = create_app()
        self.app.app_context().push()

    # Confirm user doest not exist in db

    def confirm_registration(self, username):
        # for postgres db
        exists = db.session.query(User.id).filter(
            User.username == username).first()
        return exists

    # Login method

    def login(self):
        print('\nLOGIN')

        while True:
            user_validate = input(
                'Enter username: ')
            try:
                # Check if username exists
                exists = db.session.query(User.username).filter(
                    User.username == user_validate).first()[0]
                clear_console()

                # if username exists, prompt user for password
                if exists is not None:
                    password_validate = input('Enter Password: ').strip()
                    password = db.session.query(User.password).filter(
                        User.username == user_validate).first()[0]

                    clear_console()

                    # Checking user input against password in db
                    if check_password_hash(password, password_validate) is True:
                        db.session.commit()
                        clear_console()
                        print('\nLogin Successfull')
                        time.sleep(2)
                        return user_validate

                    elif check_password_hash(password_validate, password) is False:
                        clear_console()
                        print('Incorrect password')
                        return False
            except:
                clear_console()
                print('Username does not exist')
                return False


auth = Auth()
