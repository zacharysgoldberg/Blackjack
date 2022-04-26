from app.src.score import update_score, split_score
from app.src.game_class import new_game as game
from app.src import display_cards as disp
import time

# Hit - if player's hand doesn't bust ask if they wish to be dealt another card
# Stand - take no more cards and show the dealers hand (face-down card)


def hit_stand():
    while True:
        select = input(
            'Do you wish to Hit, or Stand?\n1) Hit\n2) Stand\n').strip()
        if select == '1':
            # Hit for split hands
            if len(game.user['Hand'][0].items()) == 2:
                for index, el in game.user['Hand'][0].items():
                    card = game.deck.deck.pop()
                    el.append(card)

                split_score()
            # Hit for regular hand
            else:
                card = game.deck.deck.pop()
                game.user['Hand'].append(card)
                disp.hide_one(game.user)
                update_score(game.user)
            break

        elif select == '2':
            # Stand for split hands
            if len(game.user['Hand'][0].items()) == 2:
                split_score()
                disp.face_up(game.dealer)
            # Stand for regular hand
            else:
                update_score(game.user)
                disp.face_up(game.dealer)
                time.sleep(2)
            break

        else:
            print('Invalid Option\n')
            continue
    return select
