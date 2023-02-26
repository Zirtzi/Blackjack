import random

suits = [ "Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;33m{self.suit}\033[0m"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

deck = Deck()
deck.shuffle()

for card in deck.cards:
    print(card)

print("\n")

while deck.cards:
    prompt = input("Would you like to draw a card? (y/n): ")
    if prompt == "Y" or prompt == "y":
        print(deck.draw())
        remaining = len(deck.cards)
        print(f"There are {remaining} cards left.")
        print("\n")
    elif prompt == "All":
        remaining = len(deck.cards)
        print("\n")
        while deck.cards:
            print(deck.draw())
        print("\n")
        print(f"You drew {remaining} cards from the deck.")
        print("You are out of cards.")
        break
    elif prompt == "N" or prompt == "n":
        print("You have chosen to break the loop. Goodbye :)")
        break
    else:
        print("\033[1;31;40mYou entered an incorrect value for your response. \nPlease try again.\033[0m")