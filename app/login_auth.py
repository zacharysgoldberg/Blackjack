import csv
import hashlib
import os.path
from app.src.models import User, db
from .wsgi import create_app
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


class Main():
    def __init__(self):
        self.app = create_app()
        self.app.app_context().push()

    # Confirm user doest not exist in db
    def confirm_registration(self, username):
        # for postgres db
        exists = db.session.query(User.username).filter(
            User.username == username).first() is not None
        return exists

    # Login method

    def login(self):
        print('\nLOGIN')

        while True:
            username_validate = input(
                'Enter username: ')
            password_validate = input('Enter Password: ').strip()
            try:
                exists = db.session.query(User.username).filter(
                    User.username == username_validate).first() is not None
                password = db.session.query(User.password).filter(
                    User.username == username_validate)

                # # Getting the key back from storage as bytes
                # key_validate = hashlib.pbkdf2_hmac(
                #     'sha256', password_validate.encode(
                #         'utf-8'), salt.encode('utf-8'), 100000)

            except:
                print('Username does not exist')
                return False
            # Checking user hashed and salted password input against hased and salted password in db
            if exists is not None or check_password_hash(password, password_validate) is True:
                print('\nLogin Successfull')
                db.session.commit()
                return username_validate

            else:
                print('Incorrect password')
                return False


main = Main()
