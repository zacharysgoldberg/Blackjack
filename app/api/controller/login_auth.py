from app.models import User, session
from .menu import clear_console
from ... import create_db
from werkzeug.security import generate_password_hash, check_password_hash
import time
from sqlalchemy.orm import sessionmaker


class Auth():
    def __init__(self):
        self.db = create_db()

    # [confirm user doest not exist in db]

    def confirm_registration(self, username):
        # for postgres db
        exists = session.query(User.id).filter(
            User.username == username).first()
        return exists

    # [login method]

    def login(self):
        print('\nLOGIN')

        while True:
            user_validate = input(
                'Enter username or email: ')
            # [check if username exists]
            exists = session.query(User).filter(
                User.username == user_validate).first()
            if exists is None:
                try:
                    exists = session.query(User).filter(
                        User.email == user_validate).first()

                    clear_console()

                except:
                    clear_console()
                    print('Username does not exist')
                    return False

            # [if username exists, prompt user for password]
            if exists is not None:
                password_validate = input('Enter Password: ').strip()

                clear_console()

                # [checking user input against password in session]
                if check_password_hash(exists.password, password_validate) is True:
                    session.commit()
                    clear_console()
                    print('\nLogin Successfull')
                    time.sleep(2)
                    return user_validate

                elif check_password_hash(exists.password, password_validate) is False:
                    clear_console()
                    print('Incorrect password')
                    return False


auth = Auth()
