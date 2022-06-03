from app.controller import betting
from app.controller import hit_stand
from app.controller import win_lose
from app.controller import menu
from app.controller.game_class import new_game
from app.controller.leaderboard_class import update

################# Game logic #################


def main():
    while True:
        menu.clear_console()
        if new_game.exit == True:
            print('Goodbye')
            break
        if new_game.user['Chips'] < 5:
            print('\nInsufficient Chips\nGame new_game.Over...')
            break
        print(f"You have {new_game.user['Chips']} chips")
        new_game.ante()
        # [ask player for bet before hand dealt]
        betting.bet()
        new_game.deal(new_game.user)
        new_game.deal(new_game.dealer)
    # game.new_game.deck_list()
        while True:
            # [if player score == 21 / if split, at least one hand == 21; blackjack]
            if ('Score' in new_game.user and new_game.user['Score'] == 21) or \
                    ('Score' not in new_game.user and
                        (new_game.user['Score 1'] == 21 or
                            new_game.user['Score 2'] == 21)):
                print("Blackjack!")
                win_lose.win()
                win_lose.total_wins += 1
                break

            # [if player score > 21 / if split, at least one hand is > 21; bust]
            elif ('Score' in new_game.user and
                  new_game.user['Score'] > 21) or \
                    ('Score' not in new_game.user and
                        (new_game.user['Score 1'] > 21 or new_game.user['Score 2'] > 21)):
                print('Bust!')
                win_lose.lose()
                win_lose.total_losses += 1
                break

            # [if player score is < 21 / if split, both hands must be < 21 to hit or stand]
            elif ('Score' in new_game.user and new_game.user['Score'] < 21) or \
                    ('Score' not in new_game.user and
                        (new_game.user['Score 1'] < 21 and
                         new_game.user['Score 2'] < 21)):
                # [ask player for bet after hand dealt / after player chooses to hit]
                betting.bet()
                option = hit_stand.hit_stand()

                if option == '1':
                    continue

                # [if player hits, and player score is > 21 / if split, at least one hand is > 21; bust]
                elif ((option == '2') and
                      ('Score' in new_game.user and
                        new_game.dealer['Score'] > new_game.user['Score'] and
                        new_game.dealer['Score'] <= 21) or
                        ('Score' not in new_game.user and
                            (new_game.dealer['Score'] > new_game.user['Score 1'] or
                             new_game.dealer['Score'] > new_game.user['Score 2'] and
                             new_game.dealer['Score'] <= 21))):
                    win_lose.lose()
                    win_lose.total_losses += 1
                    break

                # [if player stands, and player score is <= 21 / if split, at least one hand is <= 21, And dealer hand is less than player hand(s); win]
                elif ((option == '2') and
                      ('Score' in new_game.user and
                       new_game.dealer['Score'] <= new_game.user['Score']) or
                      ('Score' in new_game.user and
                          new_game.dealer['Score'] > 21) or
                      ('Score' not in new_game.user and
                          (new_game.dealer['Score'] <= new_game.user['Score 1'] or
                              new_game.dealer['Score'] <= new_game.user['Score 2']))):
                    win_lose.win()
                    win_lose.total_wins += 1
                    break

                else:
                    print('Invalid Option')
        # [ask player to play again or quit]
        again = input(
            '\nPlay again?\n1) Yes\n2) No\n').strip()
        if again == '1':
            continue
        elif again == '2':
            break
        else:
            print('Invalid Option')

    # [upon exitting game, update leaderboard scores]
    if new_game.exit == False:
        update.insert(new_game.user['Email'])


main()
