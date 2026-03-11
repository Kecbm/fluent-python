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
