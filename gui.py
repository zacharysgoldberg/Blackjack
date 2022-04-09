from tkinter import *
import random
import string
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Blackjack')
root.geometry('1200x800')
root.configure(background='green')

global player, dealer, player_frame_1, my_frame, dealer_frame

# Create frames for cards
my_frame = Frame(root, bg='green')
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="",
                          bd=0, bg='green', font=('Helvetica', 16))
dealer_frame.grid(padx=20, ipadx=20)

player_frame_1 = LabelFrame(my_frame, text="",
                            bd=0, bg='green', font=('Helvetica', 16))
player_frame_1.grid(ipadx=10, pady=5)

# Put cards in frame
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_2 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=10, padx=10)
dealer_label_2.grid(row=0, column=1, pady=10, padx=10)

player_label_1 = Label(player_frame_1, text='')
player_label_2 = Label(player_frame_1, text='')
player_label_1.grid(row=1, column=0, pady=10, padx=10)
player_label_2.grid(row=1, column=1, pady=10, padx=10)

# Button frame
button_frame = Frame(root, bg='green')
button_frame.pack(pady=10)


player = {'Name': 'Player', 'Score': 0, 'Hand': [], 'Chips': 100}
dealer = {'Name': 'Dealer', 'Score': 0, 'Hand': []}


# updating scores on lable


def update_score(player_dealer, player_dealer_n):
    # only showing score for face-up card if dealer
    if player_dealer['Name'] == 'Dealer':
        player_dealer_n['text'] = f"{player_dealer['Name']} Score: {player_dealer['Hand'][0]['Value']}"
    else:
        player_dealer_n['text'] = f"{player_dealer['Name']} Score: {player_dealer['Score']}"


def split_score():
    points1 = 0
    points2 = 0
    for i, v in player['Hand'][0].items():
        for index, j in enumerate(v):
            if j['Rank'] == 'Ace' and len(v) >= 2:
                j['Value'] = 1
            if i == 'Hand 1':
                points1 += j['Value']
            elif i == 'Hand 2':
                points2 += j['Value']
    player['Score 1'] = points1
    player['Score 2'] = points2

    # update scores


def score(player_dealer):
    points = 0
    for i, card in enumerate(player_dealer['Hand']):

        if card['Rank'] == 'Ace' and len(player_dealer['Hand']) > 2:
            card['Value'] = 1

        if player_dealer['Hand'][0]['Rank'] == 'Ace' and player_dealer['Hand'][1]['Rank'] == 'Ace':
            player_dealer['Hand'][0]['Value'] = 1

        points += card['Value']

    player_dealer['Score'] = points

    print('Score: ', player['Score'])


def resize_cards(card):
    # open image
    card_img = Image.open(card)
    # resize image
    card_img_resized = card_img.resize((100, 162))
    # output card
    global card_image
    card_image = ImageTk.PhotoImage(card_img_resized)
    return card_image


# Storing card images to keep them displayed
labels = {}

# Hit button counter
count = 1


def hit():
    global label, player_image, count
    count += 1
    # get player card
    card = deck.pop()
    player['Hand'].append(card)

    # # output card
    label = Label(player_frame_1, text='')
    label.grid(
        row=1, column=count, padx=10)
    card_image = resize_cards(
        f"images/cards/{player['Hand'][count]['Rank']}_of_{player['Hand'][count]['Suit']}.png")
    label.config(image=card_image)

    labels.update({label: card_image})

    score(player)
    update_score(player, player_frame_1)
    root.title(f"Blackjack: There are {len(deck)} cards left")


def stand():
    pass


def deck():
    global suits, ranks, deck, pot, count

    deck = []
    pot = 0

    deck.clear()

    suits = ['spades',
             'hearts',
             'diamonds',
             'clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Create a 52 card deck
    for rank in ranks:
        for suit in suits:
            value = 0
            if rank == 'Jack' or rank == 'Queen' or rank == 'King':
                value = 10
            elif rank == 'Ace':
                value = 11
            else:
                value = int(rank)
            deck.append({'Rank': rank, 'Suit': suit,
                        'Value': value})

    # Shuffle the deck
    random.shuffle(deck)

    count = 1

    clear_hand()

    deal()
    root.title(f"Blackjack: There are {len(deck)} cards left")


def clear_hand():
    player['Hand'].clear()
    dealer['Hand'].clear()
    for label in labels:
        label.destroy()


def yes_no(yes, no):

    if yes['text'] == 'Yes':
        no.grid_forget()
        split_hands = {'Hand 1': [],
                       'Hand 2': []
                       }
        split_hands['Hand 1'].append(
            player['Hand'][0])
        split_hands['Hand 2'].append(
            player['Hand'][1])
        player['Hand'].clear()
        player['Hand'].append(split_hands)

        del player['Score']
        player.update({
            'Score 1': 0,
            'Score 2': 0
        })

        for index, el in player['Hand'][0].items():
            card = deck.pop()
            el.append(card)

        split_score()

        dealer_frame.grid(row=0, column=0, columnspan=2)

        player_frame_1['text'] = f"{player['Name']} Score: {player['Score 1']}"
        player_frame_2 = LabelFrame(my_frame, text=f"{player['Name']} Score: {player['Score 2']}",
                                    bd=0, bg='green', font=('Helvetica', 16))
        player_frame_2.grid(row=1, column=1, ipadx=10, pady=5)

        player_card_2 = resize_cards(
            f"images/cards/{player['Hand'][0]['Hand 1'][1]['Rank']}_of_{player['Hand'][0]['Hand 1'][1]['Suit']}.png")
        player_label_2.config(image=player_card_2)

        player_label_3 = Label(player_frame_2, text='')
        player_label_3.grid(row=1, column=2, pady=10, padx=10)

        player_label_4 = Label(player_frame_2, text='')
        player_label_4.grid(row=1, column=3, pady=10, padx=10)

        player_card_3 = resize_cards(
            f"images/cards/{player['Hand'][0]['Hand 2'][0]['Rank']}_of_{player['Hand'][0]['Hand 2'][0]['Suit']}.png")
        player_label_3.config(image=player_card_3)
        # print('Player card 3: ', player['Hand'][0]['Hand 2'][0])

        player_card_4 = resize_cards(
            f"images/cards/{player['Hand'][0]['Hand 2'][1]['Rank']}_of_{player['Hand'][0]['Hand 2'][1]['Suit']}.png")
        player_label_4.config(image=player_card_4)
        # print('Player card 4: ', player['Hand'][0]['Hand 2'][1])

    elif yes['text'] == 'No':
        no.grid_forget()
        answer.config(text='')

    yes.grid_forget()


def split():

    hit_button['state'], deal_button['state'], bet_button['state'] = DISABLED, DISABLED, DISABLED

    answer.config(text='Do you wish to split hands?')

    yes_button = Button(button_frame, text='Yes',
                        font=('Helvetica', 14), command=lambda: yes_no(yes_button, no_button))
    yes_button.grid(row=3, column=0, padx=5, sticky='nsew')

    no_button = Button(button_frame, text='No',
                       font=('Helvetica', 14), command=lambda: yes_no(no_button, yes_button))
    no_button.grid(row=3, column=1, padx=5, sticky='nsew')


def deal():

    clear_hand()

    global player, dealer, count

    count = 1

    dealer_label_1.config(image='')
    dealer_label_2.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')

    # Dealing cards to dealer and player hands
    for i in range(2):
        player_card = deck.pop()
        dealer_card = deck.pop()
        player['Hand'].append(player_card)
        dealer['Hand'].append(dealer_card)

    global dealer_card_1, dealer_card_2, player_card_1, player_card_2
    # dealer_card_1 = resize_cards(f"images/cards/{dealer[0]['Card']}.png")
    dealer_card_1 = resize_cards(f"images/cards/Face_down.png")
    dealer_card_2 = resize_cards(
        f"images/cards/{dealer['Hand'][0]['Rank']}_of_{dealer['Hand'][0]['Suit']}.png")
    dealer_label_1.config(image=dealer_card_1)
    dealer_label_2.config(image=dealer_card_2)

    player_card_1 = resize_cards(
        f"images/cards/{player['Hand'][0]['Rank']}_of_{player['Hand'][0]['Suit']}.png")
    player_card_2 = resize_cards(
        f"images/cards/{player['Hand'][1]['Rank']}_of_{player['Hand'][1]['Suit']}.png")
    player_label_1.config(image=player_card_1)
    player_label_2.config(image=player_card_2)

    score(player)
    update_score(player, player_frame_1)
    update_score(dealer, dealer_frame)

    if player['Hand'][0]['Rank'] == player['Hand'][1]['Rank']:
        split()

    root.title(f"Blackjack: There are {len(deck)} cards left")


def bet():
    global pot

    # handling edge cases
    try:
        bet = int(bet_box.get())
        answer.config(text=f'Betting ${bet}')
        if bet <= player['Chips']:
            player['Chips'] -= bet
            pot += bet * 2
            print('Current pot:', pot, '\n')

        else:
            answer.config(
                text='Amount exceeds your chip count')

    except ValueError:
        answer.config(text='Only whole numbers are permitted')


hit_button = Button(button_frame, text='Hit',
                    font=('Helvetica', 14), command=hit)
hit_button.grid(row=0, column=0, padx=5, sticky='nsew')

stand_button = Button(button_frame, text='Stand',
                      font=('Helvetica', 14), command=stand)
stand_button.grid(row=0, column=1, padx=5)

shuffle_button = Button(button_frame, text='Shuffle deck',
                        font=('Helvetica', 14), command=deck)
shuffle_button.grid(row=2, column=0, pady=5, columnspan=2)

# Display relevant messages to player
answer = Label(root, text='', font=('Helvetica', 14), bg='green')
answer.pack(padx=5)


deal_button = Button(button_frame, text='Deal',
                     font=('Helvetica', 14), command=deal)
deal_button.grid(row=1, column=0, padx=5)

# Betting
bet_button = Button(button_frame, text='Bet',
                    font=('Helvetica', 14), command=bet)
bet_button.grid(row=1, column=1, pady=5, padx=5, sticky='nsew')

bet_box = Entry(button_frame, width=10)
bet_box.grid(row=1, column=2, pady=5, sticky='nsew')

deck()

root.mainloop()
