import random
from variables import *

class Card:
    def __init__(self, suit, rank, card_value=0):
        self.suit = suit
        self.rank = rank
        self.card_value = card_value

    def value_of_card(self):
        if self.rank == "Ace":
            return 11
        if self.rank == "2":
            return 2
        if self.rank == "3":
            return 3
        if self.rank == "4":
            return 4
        if self.rank == "5":
            return 5
        if self.rank == "6":
            return 6
        if self.rank == "7":
            return 7
        if self.rank == "8":
            return 8
        if self.rank == "9":
            return 9
        if self.rank in ["10", "Jack", "Queen", "King"]:
            return 10
        return self.card_value

    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;34m{self.suit}\033[0m with " \
               f"\033[1;33;40mcard value\033[0m of: " f"\033[1;31m{self.value_of_card()}\033[0m"

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
        print("\n")
        print("Here are the deck of cards:")
        card_dealt_number = 1
        returned_cards = []
        for i in range(len(self.cards)):
            card_drawn = self.draw()
            self.returned_cards.append(card_drawn)
            print(f"Card dealt number: {card_dealt_number} - {card_drawn}")
            card_dealt_number += 1
        # Put cards back into deck
        deck.cards = deck.returned_cards
        deck.cards.reverse()
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# Initialization of deck as well as shuffle
counter = 0
for i in range(100):
    counter += 1
    # Initialization of deck as well as shuffle
    deck = Deck()
    deck.shuffle()

    # Printing the deck one time as a safety way to make sure cards are being dealt in the right order
    deck.deal_cards()

    # Deal and show hands of player
    init_deal(deck, player_hand, dealer_hand)
    print(f"{players[0]} parameter check:"
          f" [\033[1;32;40mValue\033[0m = \033[1;31;40m{check_same_value(player_hand)}\033[0m, "
          f" \033[1;32;40mSuit\033[0m = \033[1;31;40m{check_same_suit(player_hand)}\033[0m,"
          f" \033[1;32;40mRank\033[0m = \033[1;31;40m{check_same_rank(player_hand)}\033[0m, "
          f" \033[1;32;40mBlackjack\033[0m = \033[1;31;40m{check_for_blackjack(player_hand)}\033[0m]")
    print(f"{players[-1]} parameter check:"
          f" [\033[1;32;40mValue\033[0m = \033[1;31;40m{check_same_value(dealer_hand)}\033[0m, "
          f" \033[1;32;40mSuit\033[0m = \033[1;31;40m{check_same_suit(dealer_hand)}\033[0m,"
          f" \033[1;32;40mRank\033[0m = \033[1;31;40m{check_same_rank(dealer_hand)}\033[0m, "
          f" \033[1;32;40mBlackjack\033[0m = \033[1;31;40m{check_for_blackjack(dealer_hand)}\033[0m]")
    player_hand.clear()
    dealer_hand.clear()