import random

################ Creating Deck ################


class Deck:

    def __init__(self):
        self.suits = ['Spades',
                      'Hearts',
                      'Diamonds',
                      'Clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8',
                      '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = []
        self.pot = 0

    def new_deck(self):
        # [create a 52 card deck]
        for rank in self.ranks:
            for suit in self.suits:
                value = 0
                if rank == 'Jack' or rank == 'Queen' or rank == 'King':
                    value = 10
                elif rank == 'Ace':
                    value = 11
                else:
                    value = int(rank)
                    self.deck.append(
                        {'Rank': rank, 'Suit': suit, 'Value': value})
        # [shuffle the deck]
        random.shuffle(self.deck)
