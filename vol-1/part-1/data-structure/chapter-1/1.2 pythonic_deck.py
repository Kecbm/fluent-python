import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


# Text representation for a card in a deck
beer_card = Card('7', 'diamonds')
print(f"{beer_card}") # Card(rank='7', suit='diamonds')


# Number of cards in a deck
deck = FrenchDeck()
print(f"{len(deck)}") # 52


# Read first and last cards
print(f"{deck[0]}") # Card(rank='2', suit='spades')
print(f"{deck[-1]}") # Card(rank='A', suit='hearts')


# Get a random card
from random import choice
print(f"{choice(deck)}") # Card(rank='Q', suit='hearts')
print(f"{choice(deck)}") # Card(rank='K', suit='hearts')
print(f"{choice(deck)}") # Card(rank='J', suit='spades')

# Three firsts cards
print(f"{deck[:3]}") # [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]

# Cards A's only
print(f"{deck[12::13]}") # [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# See all cards in the deck
for card in deck:
    print(f"{card}")
"""
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
Card(rank='5', suit='spades')
Card(rank='6', suit='spades')
Card(rank='7', suit='spades')
Card(rank='8', suit='spades')
Card(rank='9', suit='spades')
Card(rank='10', suit='spades')
Card(rank='J', suit='spades')
Card(rank='Q', suit='spades')
Card(rank='K', suit='spades')
Card(rank='A', suit='spades')
Card(rank='2', suit='diamonds')
Card(rank='3', suit='diamonds')
Card(rank='4', suit='diamonds')
Card(rank='5', suit='diamonds')
Card(rank='6', suit='diamonds')
Card(rank='7', suit='diamonds')
Card(rank='8', suit='diamonds')
Card(rank='9', suit='diamonds')
Card(rank='10', suit='diamonds')
Card(rank='J', suit='diamonds')
Card(rank='Q', suit='diamonds')
Card(rank='K', suit='diamonds')
Card(rank='A', suit='diamonds')
Card(rank='2', suit='clubs')
Card(rank='3', suit='clubs')
Card(rank='4', suit='clubs')
Card(rank='5', suit='clubs')
Card(rank='6', suit='clubs')
Card(rank='7', suit='clubs')
Card(rank='8', suit='clubs')
Card(rank='9', suit='clubs')
Card(rank='10', suit='clubs')
Card(rank='J', suit='clubs')
Card(rank='Q', suit='clubs')
Card(rank='K', suit='clubs')
Card(rank='A', suit='clubs')
Card(rank='2', suit='hearts')
Card(rank='3', suit='hearts')
Card(rank='4', suit='hearts')
Card(rank='5', suit='hearts')
Card(rank='6', suit='hearts')
Card(rank='7', suit='hearts')
Card(rank='8', suit='hearts')
Card(rank='9', suit='hearts')
Card(rank='10', suit='hearts')
Card(rank='J', suit='hearts')
Card(rank='Q', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='A', suit='hearts')
"""

# See all cards in deck with the reversed ordering
for card in reversed(deck):
    print(f"{card}")
"""
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
Card(rank='J', suit='hearts')
Card(rank='10', suit='hearts')
Card(rank='9', suit='hearts')
Card(rank='8', suit='hearts')
Card(rank='7', suit='hearts')
Card(rank='6', suit='hearts')
Card(rank='5', suit='hearts')
Card(rank='4', suit='hearts')
Card(rank='3', suit='hearts')
Card(rank='2', suit='hearts')
Card(rank='A', suit='clubs')
Card(rank='K', suit='clubs')
Card(rank='Q', suit='clubs')
Card(rank='J', suit='clubs')
Card(rank='10', suit='clubs')
Card(rank='9', suit='clubs')
Card(rank='8', suit='clubs')
Card(rank='7', suit='clubs')
Card(rank='6', suit='clubs')
Card(rank='5', suit='clubs')
Card(rank='4', suit='clubs')
Card(rank='3', suit='clubs')
Card(rank='2', suit='clubs')
Card(rank='A', suit='diamonds')
Card(rank='K', suit='diamonds')
Card(rank='Q', suit='diamonds')
Card(rank='J', suit='diamonds')
Card(rank='10', suit='diamonds')
Card(rank='9', suit='diamonds')
Card(rank='8', suit='diamonds')
Card(rank='7', suit='diamonds')
Card(rank='6', suit='diamonds')
Card(rank='5', suit='diamonds')
Card(rank='4', suit='diamonds')
Card(rank='3', suit='diamonds')
Card(rank='2', suit='diamonds')
Card(rank='A', suit='spades')
Card(rank='K', suit='spades')
Card(rank='Q', suit='spades')
Card(rank='J', suit='spades')
Card(rank='10', suit='spades')
Card(rank='9', suit='spades')
Card(rank='8', suit='spades')
Card(rank='7', suit='spades')
Card(rank='6', suit='spades')
Card(rank='5', suit='spades')
Card(rank='4', suit='spades')
Card(rank='3', suit='spades')
Card(rank='2', suit='spades')
"""

# Get a card in deck with the operator "in"
print(f"{Card('Q', 'hearts') in deck}") # True
print(f"{Card('7', 'beasts') in deck}") # False

# Ordering of the cards in the deck by type
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(f"{card}")

"""
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
Card(rank='2', suit='spades')
Card(rank='3', suit='clubs')
Card(rank='3', suit='diamonds')
Card(rank='3', suit='hearts')
Card(rank='3', suit='spades')
Card(rank='4', suit='clubs')
Card(rank='4', suit='diamonds')
Card(rank='4', suit='hearts')
Card(rank='4', suit='spades')
Card(rank='5', suit='clubs')
Card(rank='5', suit='diamonds')
Card(rank='5', suit='hearts')
Card(rank='5', suit='spades')
Card(rank='6', suit='clubs')
Card(rank='6', suit='diamonds')
Card(rank='6', suit='hearts')
Card(rank='6', suit='spades')
Card(rank='7', suit='clubs')
Card(rank='7', suit='diamonds')
Card(rank='7', suit='hearts')
Card(rank='7', suit='spades')
Card(rank='8', suit='clubs')
Card(rank='8', suit='diamonds')
Card(rank='8', suit='hearts')
Card(rank='8', suit='spades')
Card(rank='9', suit='clubs')
Card(rank='9', suit='diamonds')
Card(rank='9', suit='hearts')
Card(rank='9', suit='spades')
Card(rank='10', suit='clubs')
Card(rank='10', suit='diamonds')
Card(rank='10', suit='hearts')
Card(rank='10', suit='spades')
Card(rank='J', suit='clubs')
Card(rank='J', suit='diamonds')
Card(rank='J', suit='hearts')
Card(rank='J', suit='spades')
Card(rank='Q', suit='clubs')
Card(rank='Q', suit='diamonds')
Card(rank='Q', suit='hearts')
Card(rank='Q', suit='spades')
Card(rank='K', suit='clubs')
Card(rank='K', suit='diamonds')
Card(rank='K', suit='hearts')
Card(rank='K', suit='spades')
Card(rank='A', suit='clubs')
Card(rank='A', suit='diamonds')
Card(rank='A', suit='hearts')
Card(rank='A', suit='spades')
"""


