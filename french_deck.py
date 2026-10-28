"""
We have implemented the FrenchDeck class, which represents a standard deck of 52 playing cards. 
Each card is represented as a named tuple with a rank and a suit. The deck can be shuffled, and cards can be drawn from it.
The class also provides methods to get the number of remaining cards and to reset the deck to its original state.

The python Data Model is used to implement the __len__ and __getitem__ methods, 
allowing the deck to be treated like a sequence.
"""

class FrenchDeck:
    from collections import namedtuple
    import random

    Card = namedtuple('Card', ['rank', 'suit'])

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [self.Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self._original_cards = list(self._cards)

    def shuffle(self):
        """Shuffle the deck of cards."""
        self.random.shuffle(self._cards)

    def draw(self, num=1):
        """Draw a specified number of cards from the deck."""
        if num > len(self._cards):
            raise ValueError("Not enough cards left in the deck.")
        drawn_cards = self._cards[:num]
        self._cards = self._cards[num:]
        return drawn_cards

    def reset(self):
        """Reset the deck to its original state."""
        self._cards = list(self._original_cards)

    def __len__(self):
        """Return the number of remaining cards in the deck."""
        return len(self._cards)

    def __getitem__(self, position):
        """Allow indexing into the deck to get a specific card."""
        return self._cards[position]


# --- Professional Entry Point ---
def main() -> None:
    deck = FrenchDeck()
    print(f"Initial deck size: {len(deck)} cards")

    deck.shuffle()
    print("Deck shuffled.")

    drawn_cards = deck.draw(5)
    print(f"Drawn cards: {drawn_cards}")
    print(f"Remaining deck size: {len(deck)} cards")

    deck.reset()
    print(f"Deck reset. Current deck size: {len(deck)} cards")

if __name__ == '__main__':
    main()
