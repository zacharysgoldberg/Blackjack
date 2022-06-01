from app.models import User, Leaderboard, session
from ... import create_db
from . import game_class as game
from . menu import clear_console
import re
import time
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import sessionmaker


class UpdateAccount():

    def __init__(self):
        self.db = create_db()

    def check_email(self, email):
        regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if regex.fullmatch(email):
            return True

        else:
            return False

    def patch(self, player):
        # [get user object]
        user = session.query(User).filter_by(username=player).first()

        clear_console()

        print("\n        === Blackjack Menu ===          ")
        print("------------------------------------------")
        print("| 1.  Change Email  |  2. Change Password |")
        print("------------------------------------------")
        print('| 3.  Change Name   |  4. Return to Menu  |')
        print('------------------------------------------')

        while True:
            choice = input('Select an option: ')
            # [update email]
            if choice == '1':
                new_email = input('Enter new email: ')
                self.check_email(new_email)
                user.email = new_email

                session.commit()
                clear_console()
                print(
                    f"\nYour email ({new_email}) has been successfully updated.")
                break

            elif choice == '2':
                new_password = input('Enter new password: ').strip()

                if len(new_password) >= 8:
                    # [update password]
                    user.password = generate_password_hash(
                        new_password, method='sha256')

                    session.commit()
                    clear_console()
                    print(
                        f"\nYour password has been successfully updated.")
                    break

            elif choice == '3':
                # [update name]
                name = input('Enter new name: ').lower(
                ).title().strip()
                user.full_name = name

                session.commit()
                clear_console()
                print(
                    f"\nYour name ({name}) has been successfully updated.")
                break

            elif choice == '4':
                # [return to main menu]
                print('Returning to main menu..')
                time.sleep(2)
                clear_console()
                break

            else:
                print('Invalid Option')
                continue


update = UpdateAccount()
