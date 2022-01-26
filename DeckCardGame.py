import random  # suffle player cards
import sys  # for acces command line arguments
from typing import List


class Card:
    # suits: list[str] = ['♦', '♥', '♣', '♠']
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']  # shapes - types pf cards
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # numbers of cards

    def __init__(self, suit, rank):
        """Default constructor"""
        self.suit = suit
        self.rank = rank

    # for making cards with numbers and symbols
    def __str__(self):
        """Returns a human-readable string representation"""
        return '%s %s' % (Card.suits[self.suit], Card.ranks[self.rank])

    # for overriding - less than!
    def __lt__(self, other):
        """overriding < operator"""
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2

    # for comparing btn cards
    def wincard(cards):
        """Get the highest winner card from list"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Deck:
    def __init__(self):
        """Initializes the deck with 52 cards"""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """return a string representation of the deck"""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        """overriding len operator"""
        return len(self.cards)

    def add_card(self, card):
        """Add a card to the deck"""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """removes and returns a card from the deck.
       And i is an index of the card to pop, by default, pops the last card!!
       """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()


class Hand(Deck):
    """represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.wincount = 0

    # to store and display player names
    def getlabel(self):
        return self.label

    # increase winner scores
    def roundwinner(self):
        self.wincount += 1

    # display winner scores-count
    def getwinncount(self):
        return self.wincount


    def __str__(self):
        return 'Card for '+ self.label + ' is '+Deck.__str__(self)