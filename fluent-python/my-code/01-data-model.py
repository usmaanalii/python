import collections
from random import choice

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


beer_card = Card('7', 'diamonds')
beer_card

deck = FrenchDeck()
len(deck)

deck[0]
deck[-1]

choice(deck)
choice(deck)
choice(deck)

deck[:3]
deck[12::13]  # pick the aces by starting on 12 and skipping 13 cards at a time

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)
