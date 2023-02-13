import random
from variables_alpha_1 import *

# Card class,
# Contains the value of the card as well as a suit and rank when drawn
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_value(self):
        return blackjack_card_value(self)

    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;34m{self.suit}\033[0m"

# Deck class,
# Provides a method to shuffle and draw a card
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.returned_cards = []
        self.card_dealt_number = 1

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def deal_cards(self):
        card_dealt_number = 1
        returned_cards = []
        for i in range(len(self.cards)):
            card_drawn = self.draw()
            self.returned_cards.append(card_drawn)
            print(f"Card Dealt Number - {self.card_dealt_number}: {card_drawn},"
                  f" \033[1;31;40mwith a value\033[0m of \033[1;31;40m{card_drawn.card_value()}\033[0m")
            self.card_dealt_number += 1


    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# Initialization of deck as well as shuffle
for i in range(1):
    # Initialization of deck as well as shuffle
    deck = Deck()
    deck.shuffle()

    # Printing the deck one time as a safety way to make sure cards are being dealt in the right order
    print("\n")
    print("Here are the deck of cards:")
    deck.deal_cards()

    # Putting the previous cards back into the deck in the same order
    deck.cards = deck.returned_cards
    deck.cards.reverse()

    # Deal and show hands of player
    init_deal(deck, player_hand, dealer_hand)
    init_hands()
    player_hand.clear()
    dealer_hand.clear()