from app import betting
from app import hit_stand
from app import win_lose
from app import menu
from app import leaderboard_class as leaderboard
from app import game_class as game


################# Game logic #################

while True:
    menu.clear_console()
    if game.new_game.exit == True:
        print('Goodbye')
        break
    if game.new_game.user['Chips'] < 5:
        print('\nInsufficient Chips\nGame new_game.Over...')
        break
    print(f"You have {game.new_game.user['Chips']} chips")
    game.new_game.ante()
    # Ask player for bet before hand dealt
    betting.bet()
    game.new_game.deal(game.new_game.user)
    game.new_game.deal(game.new_game.dealer)
    # game.new_game.deck_list()
    while True:
        # If player score == 21 / if split, at least one hand == 21; blackjack
        if ('Score' in game.new_game.user and game.new_game.user['Score'] == 21) or ('Score' not in game.new_game.user and (game.new_game.user['Score 1'] == 21 or game.new_game.user['Score 2'] == 21)):
            print("Blackjack!")
            win_lose.win()
            win_lose.total_wins += 1
            break
        # If player score > 21 / if split, at least one hand is > 21; bust
        elif ('Score' in game.new_game.user and game.new_game.user['Score'] > 21) or ('Score' not in game.new_game.user and (game.new_game.user['Score 1'] > 21 or game.new_game.user['Score 2'] > 21)):
            print('Bust!')
            win_lose.lose()
            win_lose.total_losses += 1
            break
        # If player score is < 21 / if split, both hands must be < 21 to hit or stand
        elif ('Score' in game.new_game.user and game.new_game.user['Score'] < 21) or ('Score' not in game.new_game.user and (game.new_game.user['Score 1'] < 21 and game.new_game.user['Score 2'] < 21)):
            # Ask player for bet after hand dealt / after player chooses to hit
            betting.bet()
            option = hit_stand.hit_stand()

            if option == '1' or option == 'Hit':
                continue
            # If player hits, and player score is > 21 / if split, at least one hand is > 21; bust
            elif (((option == '2' or option == 'Stand') and ('Score' in game.new_game.user and game.new_game.dealer['Score'] > game.new_game.user['Score'] and game.new_game.dealer['Score'] <= 21) or ('Score' not in game.new_game.user and game.new_game.dealer['Score'] > game.new_game.user['Score 1'] and game.new_game.dealer['Score'] > game.new_game.user['Score 2'] and game.new_game.dealer['Score'] <= 21))):
                win_lose.lose()
                win_lose.total_losses += 1
                break
            # If player stands, and player score is <= 21 / if split, at least one hand is <= 21, And dealer hand is less than player hand(s); win
            elif (((option == '2' or option == 'Stand') and ('Score' in game.new_game.user and game.new_game.dealer['Score'] <= game.new_game.user['Score']) or ('Score' not in game.new_game.user and game.new_game.dealer['Score'] <= game.new_game.user['Score 1'] or game.new_game.dealer['Score'] <= game.new_game.user['Score 2']))):
                win_lose.win()
                win_lose.total_wins += 1
                break

            else:
                print('Invalid Option')
    # Ask player to play again or quit
    again = input(
        '\nPlay again?\n1) Yes\n2) No\n').lower().capitalize().strip()
    if again == '1' or again == 'Yes':
        continue
    elif again == '2' or again == 'No':
        break
    else:
        print('Invalid Option')

# Loading results to leaderboard if user did not exit the menu before a game new_game.started
if game.new_game.exit == False:
    leaderboard.results.update_total(
        game.new_game.user['Name'], win_lose.total_wins, win_lose.total_losses)
