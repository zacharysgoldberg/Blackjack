import time
from app import menu
from app import splitting
from app import deck_class as deck
from app import display_cards as disp
from app import manage_acc as manage
from app.login_auth import auth
from app.players_class import players

############### Game setup #################


class Game:
    def __init__(self):
        # initialize user and dealer
        self.user = {}
        self.dealer = {}
        # new deck
        self.deck = deck.Deck()
        self.deck.new_deck()
        # Exit toggle
        self.logout = False
        self.activity()

    def activity(self):
        while self.logout == False:
            menu_choice = menu.main_menu()

            if menu_choice == '1':
                username = auth.login()
                # Update user and dealer dict with game info
                self.user.update({'Name': username,
                                  'Chips': 100, 'Hand': [], 'Score': 0})
                self.dealer.update({'Name': 'Dealer', 'Chips': 0, 'Hand': [],
                                    'Score': 0})
                if username == False:
                    continue

                else:
                    while self.logout == False:
                        choice = menu.loggedin_menu()
                        if choice == '1':
                            break

                        elif choice == '2':
                            manage.update.patch(self.user['Name'])
                            menu.clear_console()
                            continue

                        elif choice == '3':
                            menu.clear_console()
                            self.logout = True
                            self.user.clear()
                            return self.logout
                    break

            elif menu_choice == '2':
                # Register new user
                players.register()

            elif menu_choice == '3':
                # Leave menu
                self.exit = True
                return
            else:
                print('Invalid Option')

    # Deal 2 cards to both dealer and user

    def deal(self, player):
        print('\nDealing cards...')
    # intentional delay...
        time.sleep(1)
        for i in range(2):
            card = self.deck.deck.pop()
            player['Hand'].append(card)

        disp.hide_one(player)
        if player['Name'] == self.user['Name'] and self.user['Hand'][0]['Rank'] == self.user['Hand'][1]['Rank']:
            splitting.split()

    # Ante up

    def ante(self):
        print('\nYielding Ante...')
        time.sleep(1)
        # Ensure the user cannot exceed their total amount of chips
        if self.user['Chips'] >= 5:
            self.user['Chips'] -= 5
            self.deck.pot += 10
            print(f"\nCurrent pot: {self.deck.pot} chips")

    def deck_list(self):
        for i, el in enumerate(self.deck.deck):
            print(i, el)


new_game = Game()
