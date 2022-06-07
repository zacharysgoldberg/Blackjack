import random
from . import game_class as game

################# Reset ###################

# [reseting user's split score format to original]


def reset_score():
    orig_score = {'Score': 0}
    del game.new_game.user['Score 1']
    del game.new_game.user['Score 2']
    game.new_game.user.update(orig_score)

# [clearing player's hand and re-inserting cards into deck, randomly]


def reset_hand(player):
    if 'Score' in player:
        for i, el in enumerate(player['Hand']):
            game.new_game.deck.deck.insert(
                random.randint(0, len(game.new_game.deck.deck)), el)
    if 'Score' not in game.new_game.user:
        for i, el in game.new_game.user['Hand'][0].items():
            for index, j in enumerate(el):
                game.new_game.deck.deck.insert(
                    random.randint(0, len(game.new_game.deck.deck)), j)
        reset_score()
    player['Hand'].clear()
