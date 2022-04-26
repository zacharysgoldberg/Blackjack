from app.src import game_class as game

############### Betting #################


def bet():
    while True:
        if game.new_game.user['Chips'] >= 5:
            option = input(
                '\nDo you wish to raise?\n1) Yes\n2) No\n').strip()
            if option == '1':
                # handling edge cases
                try:
                    user_bet = int(input('Enter amount to bet: '))
                    if user_bet <= game.new_game.user['Chips']:
                        game.new_game.user['Chips'] -= user_bet
                        game.new_game.deck.pot += user_bet * 2
                        print('Current pot:', game.new_game.deck.pot, '\n')
                        break

                    else:
                        print(
                            '\nAmount exceeds your chip count. Enter an eligible value\n')
                        continue
                except ValueError:
                    print('Only whole numbers are permitted')
            elif option == '2':
                break
        else:
            break
