import time
from . import menu
from . import splitting
from . import deck_class as deck
from . import display_cards as disp
from . import manage_acc as manage
from .login_auth import login
from .players_class import players

############### Game setup #################


class Game:
    def __init__(self):
        # [initialize user and dealer]
        self.user = {}
        self.dealer = {}
        # [new deck]
        self.deck = deck.Deck()
        self.deck.new_deck()
        # [exit toggle]
        self.exit = False
        self.logout = False
        self.play = False
        self.activity()

    def activity(self):
        while self.play == False:
            menu_choice = menu.main_menu()

            if menu_choice == '1':
                username, email = login()
                # [update user and dealer dict with game info]
                self.user.update({'Name': username, 'Email': email,
                                  'Chips': 100, 'Hand': [], 'Score': 0})
                self.dealer.update({'Name': 'Dealer', 'Chips': 0, 'Hand': [],
                                    'Score': 0})
                if username == False:
                    continue

                else:
                    self.logout = False
                    # [display logged in menu]
                    while self.logout == False:
                        choice = menu.logged_in_menu()
                        if choice == '1':
                            # [player chooses play]
                            self.play = True
                            break

                        if choice == '2':
                            # [player chooses to update account info]
                            manage.update.patch(self.user['Email'])
                            continue

                        elif choice == '3':
                            menu.clear_console()
                            # [player chooses to logout]
                            self.user.clear()
                            self.dealer.clear()
                            self.logout = True
                            break

                        else:
                            print('Invalid Option')
                            continue

            if menu_choice == '2':
                # [register new user]
                players.register()

            if menu_choice == '3':
                # [leave menu]
                self.exit = True
                return
            else:
                print('Invalid Option')

    # [deal 2 cards to both dealer and user]

    def deal(self, player):
        print('\nDealing cards...')
    # i[ntentional delay...]
        time.sleep(1)
        for i in range(2):
            card = self.deck.deck.pop()
            player['Hand'].append(card)

        disp.hide_one(player)
        if player['Name'] == self.user['Name'] and self.user['Hand'][0]['Rank'] == self.user['Hand'][1]['Rank']:
            splitting.split()

    # [ante up]

    def ante(self):
        print('\nYielding Ante...')
        time.sleep(1)
        # [ensure the user cannot exceed their total amount of chips]
        if self.user['Chips'] >= 5:
            self.user['Chips'] -= 5
            self.deck.pot += 10
            print(f"\nCurrent pot: {self.deck.pot} chips")

    def deck_list(self):
        for i, el in enumerate(self.deck.deck):
            print(i, el)


new_game = Game()
