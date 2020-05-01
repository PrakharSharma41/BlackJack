# link to download card images:

import random
try:
    import tkinter      # for python 3
except ImportError:
    import Tkinter as tkinter   # for python 2


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_card = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    # for each suit retreive the image of the cards
    for suit in suits:
        # first the number card 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file = name)
            card_images.append((card, image, ))

        # next the face_cards
        for card in face_card:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))    # as each face card has value 10


def _deal_card(frame):
    # pop the next card of the top of the deck
    if result_text.get() != "Player Wins!!" and result_text.get() != "Dealer Wins!!"and result_text.get() != "Draw!!":
        next_card = deck.pop(0)
        # add it back to pack
        deck.append(next_card)
        # add the image to label and display label
        tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')  # as each  item of list is tuple thus next_card[1]
        # now return card's face value
        return next_card


def score_hand(hand):
    # calculate total score of all cards in list
    # only one ace can have value 11,  and this will reduce to 1 if hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value  == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust,  check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    global dealer_score
    global player_score
    # global dealer_hand
    # global player_hand
    if result_text.get() != "Player Wins!!" and result_text.get() != "Dealer Wins!!"and result_text.get() != "Draw!!":
        dealer_score = score_hand(dealer_hand)    # for first card which is drawn at start of game

        while 0 < dealer_score < 17:      # dealer should grab card automatically if his score is less than 17
            dealer_hand.append(_deal_card(dealer_card_frame))
            dealer_score = score_hand(dealer_hand)
            dealer_score_label.set(dealer_score)

        player_score = score_hand(player_hand)
        if player_score>21:
            result_text.set("Dealer Wins!!")
        elif dealer_score>21 or dealer_score < player_score:
            result_text.set("Player Wins!!")
        elif dealer_score>player_score:
            result_text.set("Dealer Wins!!")
        else:
            result_text.set("Draw!!")


def deal_player():
    global dealer_score
    global player_score
    #method1
    if result_text.get() != "Player Wins!!" and result_text.get() != "Dealer Wins!!" and result_text.get() != "Draw!!":
        player_hand.append(_deal_card(player_card_frame))
        player_score = score_hand(player_hand)
        player_score_label.set(player_score)
        dealer_score = score_hand(dealer_hand)

        if player_score >= 21:

            if len(dealer_hand) == 1:
                while 0< dealer_score<17:      # dealer should grab card automatically if his score is less than 17
                    dealer_hand.append(_deal_card(dealer_card_frame))
                    dealer_score = score_hand(dealer_hand)
                    dealer_score_label.set(dealer_score)
                if player_score>21:
                    result_text.set("Dealer Wins!!")
                elif dealer_score>21 or dealer_score<player_score:
                    result_text.set("Player Wins!!")
                elif dealer_score>player_score:
                    result_text.set("Dealer Wins!!")
                else:
                    result_text.set("Draw!!")

            else:
                result_text.set("Dealer Wins!!")

    # print(locals())

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background = "green")
    dealer_card_frame.grid(row = 0, column = 1, sticky = 'ew', rowspan = 2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background = "green")
    player_card_frame.grid(row = 2, column = 1, sticky = 'ew', rowspan = 2)

    result_text.set("Game in Process")

    #  create list to store dealers and players hand
    dealer_hand = []     # global variable
    player_hand = []
    initial_deal()


def initial_deal():    # whenever a new gam starts dealer has 1 card and player has 2 cards
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()

# __name__  =  "__main__"    # should not be written as it gives error

mainWindow = tkinter.Tk()
# set up screen and frames for dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")


mainWindow.configure(background = '#116466')

result_text = tkinter.StringVar()     # value holder for string variable
result_text.set("Game in Progress")  # contains result of game

result = tkinter.Label(mainWindow, textvariable = result_text,  background = "blanched almond",  font = ("MS Sans Serif",  15,  "bold"))
result.grid(row = 0, column = 0, columnspan = 3)

# creating card frame to hold player and dealer card
card_frame = tkinter.Frame(mainWindow, relief = "sunken", borderwidth = 2, background = "green")
card_frame.grid(row = 1, column = 0, sticky = 'ew', columnspan = 3, rowspan = 2)

dealer_score_label = tkinter.IntVar()    # variable for holding dealer score
tkinter.Label(card_frame,  text="Dealer", background = "green", fg = "white", relief = "sunken", borderwidth = 2, font = ("System", 10, "bold")).grid(row = 0, column = 0, sticky = 'n')
tkinter.Label(card_frame,  textvariable=dealer_score_label, background = "green", fg = "white", relief = "sunken", borderwidth = 2, font = "System").grid(row = 1, column = 0, sticky = 'n')


# embedded frame to hold dealer card images
dealer_card_frame = tkinter.Frame(card_frame, background = "green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)


player_score_label = tkinter.IntVar()    # variable for holding player score
tkinter.Label(card_frame, text="Player", background="green", fg="white", relief="sunken", borderwidth=2, font=("System", 10, "bold")).grid(row=2, column=0, sticky='n')
tkinter.Label(card_frame,  textvariable=player_score_label,  background="green", fg="white", relief="sunken", borderwidth=2, font="System").grid(row=3, column=0, sticky = 'n')


# embedded frame to hold player card images
player_card_frame = tkinter.Frame(card_frame,  background="green")
player_card_frame.grid(row=2,  column=1,  sticky='ew',  rowspan=2)

# creating buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3,  column=0,  columnspan=3,  sticky='w')

dealer_button = tkinter.Button(button_frame, text="Stand",  command=deal_dealer,  font="System",  bg="blanched almond",  borderwidth=4)
dealer_button.grid(row=0,  column=0)

player_button = tkinter.Button(button_frame,  text="Hit",  command=deal_player,  font="System",  bg="blanched almond", borderwidth=4)
player_button.grid(row=0,  column=1)

new_game_button = tkinter.Button(button_frame,  text="New Game",  command=new_game,  font="System",  bg="blanched almond",  borderwidth=4)
new_game_button.grid(row=0,  column=2)

shuffle_button = tkinter.Button(button_frame,  text="Shuffle",  command=shuffle,  font="System",  bg="blanched almond", borderwidth=4)
shuffle_button.grid(row=0,  column=3)

exit_button = tkinter.Button(button_frame,  text="Exit",  command=mainWindow.destroy,  font="System",  bg="blanched almond",  borderwidth=4)
exit_button.grid(row=0,  column=4)

# load cards with image and their value as tuple in list
cards = []
load_images(cards)
# print(cards)

# create a new deck of cards and shuffle
deck = list(cards)
shuffle()

# create list to store dealers and players hand
dealer_hand = []     # cards with dealer
player_hand = []     # cards with player

if __name__ == '__main__':
    play()
