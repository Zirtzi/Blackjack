import random

# Creating suits and ranks for cards
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Card class,
# Contains the value of the card as well as a suit and rank when drawn
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_value(self):
        if self.rank == "Ace":
            self.ace_value = 11
            return self.ace_value
        elif self.rank == "2":
            self.value = 2
            return self.value
        elif self.rank == "3":
            self.value = 3
            return self.value
        elif self.rank == "4":
            self.value = 4
            return self.value
        elif self.rank == "5":
            self.value = 5
            return self.value
        elif self.rank == "6":
            self.value = 6
            return self.value
        elif self.rank == "7":
            self.value = 7
            return self.value
        elif self.rank == "8":
            self.value = 8
            return self.value
        elif self.rank == "9":
            self.value = 9
            return self.value
        elif self.rank in ["10", "Jack", "Queen", "King"]:
            self.value = 10
            return self.value

    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;34m{self.suit}\033[0m"

# Deck class,
# Provides a method to shuffle and draw a card
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# Initialization of deck as well as shuffle
deck = Deck()
deck.shuffle()

print("\n")
print("Here are the deck of cards:")

# Printing the deck one time as a safety way to make sure cards are being dealt in the right order
returned_cards = []
card_dealt_number = 1
for i in range(len(deck.cards)):
    card_drawn = deck.draw()
    returned_cards.append(card_drawn)
    print(f"Card Dealt Number - {card_dealt_number}: {card_drawn}, \033[1;31;40mwith a value\033[0m of \033[1;31;40m{card_drawn.card_value()}\033[0m")
    card_dealt_number += 1

# Putting the previous cards back into the deck in the same order
deck.cards = returned_cards
deck.cards.reverse()

# Initializtion of player and dealer as well as their card total
players = ["Player 1", "Dealer"]
player_total = 0
dealer_total = 0

# Dealing cards to players
player_hand = []
dealer_hand = []
for turn in range(4):
    player = players[turn % 2]
    card_drawn = deck.draw()
    if (turn % 2) == 0:
        player_hand.append(card_drawn)
    elif (turn % 2) == 1:
        dealer_hand.append(card_drawn)

# Adding values of the player hand
for card in player_hand:
    player_total += card.card_value()

# Adding values of the dealer hand
for card in dealer_hand:
    dealer_total += card.card_value()

# Checking for blackjack for player
player_has_ace = False
player_has_face = False
player_has_blackjack = False
for card in player_hand:
    if card.rank == "Ace":
        player_has_ace = True
    elif card.rank in ["10", "Jack", "Queen", "King"]:
        player_has_face = True
    if player_has_ace and player_has_face:
        player_has_blackjack = True
        break

# Checking for blackjack for dealer
dealer_has_ace = False
dealer_has_face = False
dealer_has_blackjack = False
for card in dealer_hand:
    if card.rank == "Ace":
        dealer_has_ace = True
    elif card.rank in ["10", "Jack", "Queen", "King"]:
        dealer_has_face = True
    if dealer_has_ace and dealer_has_face:
        dealer_has_blackjack = True
        break

# Showing the player and dealer's hand
print("\n")
print("Here are the players' hands:")
if player_has_blackjack == True and dealer_has_blackjack == True:
    print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40m{players[0]} has blackjack!\033[0m")
    print(f"{players[-1]}'s hand is: {dealer_hand} \033[1;31;40m{players[-1]} has blackjack!\033[0m")
    print(f"\033[1;31;40mIt is a draw!\033[0m")
elif player_has_blackjack == True and dealer_has_blackjack == False:
    print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40m{players[0]} has blackjack!\033[0m")
    print(f"{players[-1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}" + f"] \033[1;31;40mwith a current value\033[0m of: \033[1;31;40m{dealer_hand[-1].card_value()}\033[0m")
    print(f"\033[1;31;40m{players[0]} Wins!\033[0m")
elif player_has_blackjack == False and dealer_has_blackjack == False:
    print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40mwith a current value\033[0m of: \033[1;31;40m{player_total}\033[0m")
    print(f"{players[-1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}" + f"] \033[1;31;40mwith a current value\033[0m of: \033[1;31;40m{dealer_hand[-1].card_value()}\033[0m")
elif player_has_blackjack == False and dealer_has_blackjack == True:
    print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40mwith a current value\033[0m of: \033[1;31;40m{player_total}\033[0m")
    print(f"{players[-1]}'s hand is: {dealer_hand} \033[1;31;40m{players[-1]} has blackjack!\033[0m")
    print(f"\033[1;31;40m{players[-1]} Wins!\033[0m")
print("\n")