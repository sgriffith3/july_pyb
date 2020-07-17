import random

class DeckofCards:

    def __init__(self):
        cards = []
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for n in nums:
            for suit in ['spades', 'diamonds', 'clubs', 'hearts']:
                card = f"{n} of {suit}"
                cards.append(card)
        self.cards = cards

    def pick_one(self):
        one = random.choice(self.cards)
        self.cards.remove(one)
        return one

deck = DeckofCards()

print(len(deck.cards))
print(deck.pick_one())

print(len(deck.cards))
