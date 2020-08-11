import collections
from random import shuffle
from random import choice

# namedtuple
Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # print(ranks)
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        # print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def main():
    # beer_card = Card('7', 'diamonds')
    # print(beer_card)
    deck = FrenchDeck()
    shuffle(deck)
    print(deck[:5])

    # print(deck[0])
    # print(choice(deck))
    # for card in deck:
        # print(card)
        # print(card.rank)
        # print(card.suit)
    # for card in sorted(deck, key=spades_high):
    #     print(card)


if __name__ == "__main__":
    main()