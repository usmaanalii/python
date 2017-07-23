import collections
from random import choice
from math import hypot

# Example 1.1 - A deck as a sequence of cards
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

#
beer_card = Card('7', 'diamonds')
beer_card

#
deck = FrenchDeck()
len(deck)

#
deck[0]
deck[-1]

#
choice(deck)
choice(deck)
choice(deck)

#
deck[:3]
deck[12::13]  # pick the aces by starting on 12 and skipping 13 cards at a time

#
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

#
Card('Q', 'hearts') in deck
Card('7', 'beasts') in deck

#
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

# Example 1.2 - A Simple 2d vector class


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # string representation of the object
    # %r returns 1 not '1' since they are needed as integers
    def __repr__(self):
        return 'Vector (%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # TODO: How does abs(self) return 0.0 (I've checked that it does)
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.y
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
