from . import game_class as game
from .display_cards import face_up
import time

############ Update Scores #############

# [update score]


def update_score(player):
    # [update player's score]
    if player['Name'] != 'Dealer':
        points = 0
        for index in player['Hand']:
            if index['Rank'] == 'Ace' and len(player['Hand']) > 2:
                index['Value'] = 1

            points += index['Value']
        player['Score'] = points
        print(f"\n{player['Name']}'s Score: {player['Score']}\n")

    # [update score for dealer]
    else:
        points = 0
        for index in player['Hand']:
            points += index['Value']

        player['Score'] = points
        # [if dealers score is <= 16, dealer must draw additional cards until their total score is >= 17]
        while player['Score'] <= 16:
            print('\nDealer is drawing a card...')
            time.sleep(2)
            points = 0
            card = game.new_game.deck.deck.pop()
            player['Hand'].append(card)
            print(
                f"\nDealer draws a {player['Hand'][-1]['Rank']} of {player['Hand'][-1]['Suit']}")
            for index in player['Hand']:
                points += index['Value']

            player['Score'] = points

        print(f"\nDealer's Score: {player['Score']}\n")


# [update score for split hands]


def split_score():
    points1 = 0
    points2 = 0
    for i, v in game.new_game.user['Hand'][0].items():
        for index, j in enumerate(v):
            if j['Rank'] == 'Ace' and len(v) >= 2:
                j['Value'] = 1
            if i == 'Hand 1':
                points1 += j['Value']
            elif i == 'Hand 2':
                points2 += j['Value']
    game.new_game.user['Score 1'] = points1
    game.new_game.user['Score 2'] = points2

    for i, v in game.new_game.user['Hand'][0].items():
        if i == 'Hand 2':
            print()

        for index, j in enumerate(v):
            print("{} has {a} {b} of {c} for {}".format(game.new_game.user['Name'], i,

                                                        a='an' if j['Rank'] == '8' or j['Rank'] == 'Ace' else 'a', b=j['Rank'], c=j['Suit']))
    print(
        f"\nHand 1 Score: {game.new_game.user['Score 1']}, Hand 2 Score: {game.new_game.user['Score 2']}\n")
