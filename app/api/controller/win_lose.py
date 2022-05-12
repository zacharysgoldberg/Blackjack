from . import game_class as game
from . import reset

################ Determine Winner ###############

# [Win / Loss counter]
total_wins = 0
total_losses = 0

# [assign the user 100% of the pot upon winning]


def win():
    game.new_game.user['Chips'] += game.new_game.deck.pot
    print(
        f"You win! {game.new_game.user['Name']} now has {game.new_game.user['Chips']} chips.")
    game.new_game.deck.pot = 0
    reset.reset_hand(game.new_game.user)
    reset.reset_hand(game.new_game.dealer)


def lose():
    game.new_game.deck.pot = 0
    print(
        f"You lose... {game.new_game.user['Name']} has {game.new_game.user['Chips']} chips left.")
    reset.reset_hand(game.new_game.user)
    reset.reset_hand(game.new_game.dealer)
