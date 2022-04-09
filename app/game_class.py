import time
from app import menu
from app import splitting
from app import deck_class as deck
from app import display_cards as disp
from app.login_auth import main
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
        self.exit = False
        self.activity()

    def activity(self):
        while True:
            choice = menu.menu()
            if choice == '1' or choice == 'login':
                username = main.login()
                # Update user and dealer dict with game info
                self.user.update({'Name': username,
                                  'Chips': 100, 'Hand': [], 'Score': 0})
                self.dealer.update({'Name': 'Dealer', 'Chips': 0, 'Hand': [],
                                    'Score': 0})
                if username == False:
                    continue
                else:
                    break
            elif choice == '2' or choice == 'register':
                # Register new user
                players.register()

            elif choice == '3' or choice == 'exit':
                # Leave menu
                self.exit = True
                return
            else:
                print('Invalid Choice')

    # Deal 2 cards to both dealer and user

    def deal(self, player):
        print('Dealing cards...\n')
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
            print(f"\nThe pot is at {self.deck.pot} chips")

    def deck_list(self):
        for i, el in enumerate(self.deck.deck):
            print(i, el)


new_game = Game()
