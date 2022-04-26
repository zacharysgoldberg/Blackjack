import time
from app.src import score
from app.src import game_class as game

############## Displaying Cards ##################

# Display hands to user and hiding the dealer's second card (face-down)


def hide_one(player):
    if player['Name'] != 'Dealer':
        for i in player['Hand']:
            print('{} has {x} {y} of {z}'.format(player['Name'],
                                                 x='an' if i['Rank'] == '8' or i['Rank'] == 'Ace' else 'a', y=i['Rank'], z=i['Suit']))
        score.update_score(player)

    else:
        print("Dealer has {x} {y} of {z} \nDealer's second card is face-down".format(
            x='an' if player['Hand'][0]['Rank'] == '8' or player['Hand'][0]['Rank'] == 'Ace' else 'a', y=player['Hand'][0]['Rank'], z=player['Hand'][0]['Suit']))

# Displaying all cards to player


def face_up(player):
    time.sleep(1)
    for i in player['Hand']:
        print('{} has {x} {y} of {z}'.format(player['Name'],
                                             x='an' if i['Rank'] == '8' or i['Rank'] == 'Ace' else 'a', y=i['Rank'], z=i['Suit']))
    score.update_score(player)
