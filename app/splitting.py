import time
from app import score
from app import game_class as game

# Splitting - When both starting cards are the same value, create 2 new hands from them. Each new hand gets another card so that the player has 2 starting cards for each


def split():
    while True:
        select = input(
            'Do you wish to Split your hand?\n1) Yes\n2) No\n').lower().capitalize().strip()
        if select == '1' or select == 'Yes':
            print('Splitting...\n')

            split_hands = {'Hand 1': [],
                           'Hand 2': []
                           }
            split_hands['Hand 1'].append(
                game.new_game.user['Hand'][0])
            split_hands['Hand 2'].append(
                game.new_game.user['Hand'][1])
            game.new_game.user['Hand'].clear()
            game.new_game.user['Hand'].append(split_hands)

            del game.new_game.user['Score']
            game.new_game.user.update({
                'Score 1': 0,
                'Score 2': 0
            })
            time.sleep(2)
            for index, el in game.new_game.user['Hand'][0].items():
                card = game.new_game.deck.deck.pop()
                el.append(card)

            score.split_score()
            break
        elif select == '2' or select == 'No':
            break
        else:
            print('Invalid Option')
