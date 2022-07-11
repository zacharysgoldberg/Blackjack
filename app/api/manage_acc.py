import re
import time
import json
from . import game_class as game
from . menu import clear_console
from werkzeug.security import generate_password_hash
from .. import db


class UpdateAccount():
    def check_email(self, email):
        regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if regex.fullmatch(email):
            return True

        else:
            return False

    def patch(self, player):
        # [get user object]
        user = json.loads(db.execute_command('JSON.GET', player))

        clear_console()

        print("\n        === Blackjack Menu ===          ")
        print("------------------------------------------")
        print("| 1.  Update Name  |  2. Update Password |")
        print("------------------------------------------")
        print('|            3. Return to Menu           |')
        print('------------------------------------------')

        while True:
            choice = input('Select an option: ')
            # [update email]
            if choice == '1':
                # [update name]
                name = input('Enter name: ').lower(
                ).title().strip()

                user['profile']['full_name'] = name

                db.execute_command('JSON.SET', player, '.',
                                   json.dumps(user))
                # db.save()
                clear_console()
                print(
                    f"\nYour name has successfully updated, {name}.")
                break

            elif choice == '2':
                new_password = input('Enter new password: ').strip()

                if len(new_password) >= 8:
                    # [update password]
                    user['profile']['password'] = generate_password_hash(
                        new_password, method='sha256')

                    db.execute_command('JSON.SET', player, '.',
                                       json.dumps(user))
                    # db.save()
                    clear_console()
                    print(
                        f"\nYour password has successfully updated.")
                    break

            elif choice == '3':
                # [return to main menu]
                print('Returning to main menu..')
                time.sleep(2)
                clear_console()
                break

            else:
                print('Invalid Option')
                continue


update = UpdateAccount()
