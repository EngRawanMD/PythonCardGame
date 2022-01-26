import sys  # for access command line arguments
from DeckCardGame import Deck
from DeckCardGame import Hand
from DeckCardGame import Card

def play(argv):
    deck = Deck()  # initialize deck
    hands = []
    for i in range(1, 5):
        player = 'Player %d' % i  # default player name
        if len(argv) > i:
            player = argv[i]  # get player name from command line parameter
        hands.append(Hand(player))  # add player

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())  # remove card from deck and add to hand

    print(hands[0])  # print first player card
    print('-----*******-----')
    print('-----WELCOME-----')
    print('-----*******-----')
    input("Lets start playing. Press any key to continue : ")  # wait for keypress

    # Game rounds
    for i in range(1, 14):
        cards = []  # collect card in a round
        floors = []  # get string representation for display in each round
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)  # collect individual card
            floors.append(hand.getlabel() + " : " + str(card))  # add string format for individual card

        winner_card = Card.wincard(cards)  # check for winner card
        winner_hand = hands[cards.index(winner_card)]  # find the winner hand from winner card
        winner_hand.roundwinner()  # add score for winner hand
        print("Round", i, ":-", ", ".join(floors), ", Winner :- ", winner_hand.getlabel(), ":", winner_card)
        input('Next Round:\n')  # wait for keypress to go for next round

    for hand in hands:  # display the individual hand score after the 13 rounds of play
        print("Score for", hand.getlabel(), "is", hand.getwincount())



# print('\u2666', '\u2665', '\u2663', '\u2660')

def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Play Again (Y/N)? : ")
    print("Bye Bye")


if __name__ == '__main__':
    main(sys.argv)
