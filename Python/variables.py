# ----- ----- ----- ----- ----- ----- ----- ----- ----- Imports ----- ----- ----- ----- ----- ----- ----- ----- ----- #
import random

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Arrays ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Creating suits and ranks for cards
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Players array
players = ["Player 1", "Dealer"]

# Player hands
player_hand = []
dealer_hand = []

# ----- ----- ----- ----- ----- ----- ----- ----- Variables / Booleans ----- ----- ----- ----- ----- ----- ----- ----- #
# Player total (Blackjack count)
player_total = 0
dealer_total = 0

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Classes ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Card Class
class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.card_value = 11 if rank == "Ace" else 10 if rank in ["10", "Jack", "Queen", "King"] else int(rank)

    def value_of_card(self):
        return self.card_value

    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;34m{self.suit}\033[0m with " \
               f"\033[1;33;40mcard value\033[0m of: " f"\033[1;31m{self.value_of_card()}\033[0m"

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
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
        self.cards = self.returned_cards
        self.cards.reverse()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# ----- ----- ----- ----- ----- ----- ----- ----- Methods ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Adding values of players
def add_player_total(hand):
    if hand == dealer_hand:
        total = dealer_total
        for card in hand:
            total += card.value_of_card()
    else:
        total = player_total
        for card in hand:
            total += card.value_of_card()
    return total

# Check rank of cards method
def check_for_rank(hand, checking_rank):
    result = False
    for card in hand:
        if card.rank in checking_rank:
            result = True
            break
    return result

# Check suit of cards method
def check_for_suit(hand, checking_suit):
    result = False
    for card in hand:
        if card.suit in checking_suit:
            result = True
            break
    return result

# Check for specific total
def check_for_total(hand, checking_total):
    result = False
    if add_player_total(hand) == checking_total:
        result = True
    else:
        result = False
    return result

# Check same rank method
def check_same_rank(hand, checking_rank = None):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if checking_rank is None:
        if card_1.rank == card_2.rank:
            result = True
    else:
        if card_1.rank == card_2.rank == checking_rank:
            result = True
    return result

# Check for same suit method
def check_same_suit(hand, checking_suit = None):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if checking_suit is None:
        if card_1.suit == card_2.suit:
            result = True
    else:
        if card_1.suit == card_2.suit == checking_suit:
            result = True
    return result

# Check same value method
def check_same_value(hand, checking_value = None):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if checking_value is None:
        if card_1.value_of_card() == card_2.value_of_card():
            result = True
    else:
        if card_1.value_of_card() == card_2.value_of_card() == checking_value:
            result = True
    return result

# Check for blackjack method
def check_for_blackjack(hand):
    result = False
    for card in hand:
        if check_for_rank(hand, "Ace") and check_for_rank(hand, ["10", "Jack", "Queen", "King"]):
            result = True
        else:
            break
    return result

# Parameter check method
def parameter_check(hand):
    if hand == player_hand:
        player_value = 0
        print(f"{players[player_value]} parameter check:"
              f" [\033[1;32;40mValue\033[0m = \033[1;31;40m{check_same_value(hand)}\033[0m, "
              f" \033[1;32;40mSuit\033[0m = \033[1;31;40m{check_same_suit(hand)}\033[0m,"
              f" \033[1;32;40mRank\033[0m = \033[1;31;40m{check_same_rank(hand)}\033[0m, "
              f" \033[1;32;40mBlackjack\033[0m = \033[1;31;40m{check_for_blackjack(hand)}\033[0m]")
    elif hand == dealer_hand:
        player_value = 1
        print(f"{players[player_value]} parameter check:"
              f" [\033[1;32;40mValue\033[0m = \033[1;31;40m{check_same_value(hand)}\033[0m, "
              f" \033[1;32;40mSuit\033[0m = \033[1;31;40m{check_same_suit(hand)}\033[0m,"
              f" \033[1;32;40mRank\033[0m = \033[1;31;40m{check_same_rank(hand)}\033[0m, "
              f" \033[1;32;40mBlackjack\033[0m = \033[1;31;40m{check_for_blackjack(hand)}\033[0m]")

# Display hand method
def display_hand(hand, display = None):
    if hand != dealer_hand:
        print(f"{players[0]}'s hand is: {hand} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(hand)}\033[0m")
    elif hand == dealer_hand and display is None:
        print(f"{players[-1]}'s hand is: [Hidden, " + f"{hand[-1]}] with \033[1;33;40mtotal value\033[0m of: "
              f"\033[1;31;40m{add_player_total(hand) - hand[0].value_of_card()}\033[0m")
    elif hand == dealer_hand and display is not None:
        print(f"{players[1]}'s hand is: {hand} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(hand)}\033[0m")

# Dealer showing Ace
def dealer_showing_ace():
    result = False
    if dealer_hand[1].rank == "Ace":
        result = True
    else:
        result = False
    return result

# Re-Assing Ace's value method
def reassign_ace_value(hand):
    hand[0].card_value = 1
    hand[1].card_value = 11
    return hand

# Split hand method
def split_hand(hand):
    hand_1 = hand[0]
    hand_2 = hand[1]
    return hand_1, hand_2

# Select hand method
def select_hand(hand, choice):
    hands = split_hand(hand)
    return [hands[choice]]

# Conditions check method
def conditions_check():
    if dealer_showing_ace():
        choice = ""
        while choice.lower() not in ["y", "n"]:
            choice = input("The dealer is showing an Ace, would you like to buy insurance? (y/n): ")
            print("\n")
            if choice.lower() == "y":
                print("Player has chosen to buy insurance, we will now check for if the dealer has Blackjack: ")
                print("\n")
                if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
                    print("Both players have Blackjack, it is a push. Player wins insurance.")
                    break
                elif check_for_blackjack(dealer_hand) == True and check_for_blackjack(player_hand) == False:
                    print("Dealer has Blackjack, player wins insurance.")
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == True:
                    print("Dealer doesn't have Blackjack, player has Blackjack. Player loses insurance.")
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
                    print("Neither player has Blackjack, player loses insurance.")
                    print("\n")
                    if check_same_rank(dealer_hand, "Ace"):
                        reassign_ace_value(dealer_hand)
                    else:
                        continue
            elif choice.lower() == "n":
                print("Player has chosen to not buy insurance. We will now check if the dealer has Blackjack: ")
                print("\n")
                if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
                    print("Both players have Blackjack, it is a push.")
                    break
                elif check_for_blackjack(dealer_hand) == True and check_for_blackjack(player_hand) == False:
                    print("Dealer has Blackjack. Dealer wins.")
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == True:
                    print("Dealer doesn't have Blackjack, player has Blackjack. Player wins.")
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
                    print("Neither player has Blackjack.")
                    print("\n")
                    if check_same_rank(dealer_hand, "Ace"):
                        reassign_ace_value(dealer_hand)
                    else:
                        continue
            elif choice.lower() not in ["y", "n"]:
                print("Invalid choice.")
                print("\n")
    elif dealer_showing_ace() == False:
        if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
            print("Both players have Blackjack, it is a push.")
        elif check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand) == False:
            print("Dealer has Blackjack.")
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
            print("Player has Blackjack. Player wins.")
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
            print("Neither player has Blackjack.")