import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;34m{self.suit}\033[0m"

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

print("\n")
print("Here are the deck of cards:")

returned_cards = []
card_dealt_number = 1
for i in range(len(deck.cards)):
    card_drawn = deck.draw()
    returned_cards.append(card_drawn)
    print(f"Card Dealt Number - {card_dealt_number}: {card_drawn}")
    card_dealt_number += 1

deck.cards = returned_cards
deck.cards.reverse()
players = ["Player 1", "Dealer"]

print("\n")
print("Here is the initial dealing of cards:")
player_hand = []
dealer_hand = []
for turn in range(4):
    player = players[turn % 2]
    card_drawn = deck.draw()
    if (turn % 2) == 0:
        player_hand.append(card_drawn)
    elif (turn % 2) == 1:
        dealer_hand.append(card_drawn)

print("\n")
print("Here are the players' hands:")
print(f"{players[0]}'s hand is: {player_hand}")
print(f"{players[1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}" + "]")

print("\n")
initial_prompt = "h"
while initial_prompt.lower() == "h":
    initial_prompt = input("Would you like to hit or stay? (h/s) ")
    if initial_prompt.lower() == "h":
        player_hand.append(deck.draw())
        print("\n")
        print("The hands of each player are:")
        print(f"{players[0]}'s hand is: {player_hand}")
        print(f"{players[1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}" + "]")
        print("\n")
    elif initial_prompt.lower() == "s":
        print("\n")
        print("The hands of each player are:")
        print(f"{players[0]}'s final hand is: {player_hand}")
        print(f"{players[1]}'s hand is: {dealer_hand}")
        break
    else:
        print("\n")
        print("\033[1;31;40mYou entered an incorrect value for your response. Please try again.\033[0m")