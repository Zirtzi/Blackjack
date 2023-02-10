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

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Classes ----- ----- ----- ----- ----- ----- ----- ----- ----- #
class Card:
    def __init__(self, suit, rank, card_value = None):
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
        self.cards = self.returned_cards
        self.cards.reverse()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# ----- ----- ----- ----- ----- ----- ----- ----- Variables / Booleans ----- ----- ----- ----- ----- ----- ----- ----- #
# Player total (Blackjack count)
player_total = 0
dealer_total = 0

# ----- ----- ----- ----- ----- ----- ----- ----- Methods ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Adding values of players
def add_player_total(hand):
    if hand == player_hand:
        total = player_total
        for card in hand:
            total += card.value_of_card()
    elif hand == dealer_hand:
        total = dealer_total
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

# Player turn method
def display_hand(hand_of_player, display = None):
    if hand_of_player == player_hand:
        print(f"{players[0]}'s hand is: {hand_of_player} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(hand_of_player)}\033[0m")
    elif hand_of_player == dealer_hand and display is None:
        print(f"{players[-1]}'s hand is: [Hidden, " + f"{hand_of_player[-1]}] with \033[1;33;40mtotal value\033[0m of: "
              f"\033[1;31;40m{add_player_total(hand_of_player) - hand_of_player[0].value_of_card()}\033[0m")
    elif hand_of_player == dealer_hand and display is not None:
        print(f"{players[1]}'s hand is: {hand_of_player} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(hand_of_player)}\033[0m")

# Deal hands method
def deal_hand(deck, player, dealer):
    for turn in range(4):
        card_drawn = deck.draw()
        if (turn % 2) == 0:
            player.append(card_drawn)
        elif (turn % 2) == 1:
            dealer.append(card_drawn)
    print("\n")
    display_hand(player_hand)
    display_hand(dealer_hand)
    print("\n")
    parameter_check(player_hand)
    parameter_check(dealer_hand)

def hit(deck, hand):
    card_drawn = deck.draw()
    hand.append(card_drawn)

def stay(deck):
    return None

# Hit, Stay, Double Down Prompt method
def play_game(deck, hand):
    if hand == player_hand:
        response = ""
        player_hand_total = add_player_total(hand)
        while response not in ["h", "s", "d"] and player_hand_total < 21:
            print("\n")
            response = input("Would you like to hit, stay, or double down? (h/s/d): ")
            print("\n")
            if response.lower() == "h":
                hit(deck, hand)
                player_hand_total = add_player_total(hand)
                if player_hand_total < 21:
                    print("You chose to hit, current hands are: ")
                    display_hand(hand)
                    display_hand(dealer_hand)
                elif player_hand_total == 21:
                    print("You have 21! The current hands are: ")
                    display_hand(hand)
                    display_hand(dealer_hand)
                elif player_hand_total > 21:
                    print("You have busted. The dealer wins. The final hands are: ")
                    display_hand(hand)
                    display_hand(dealer_hand, 1)
                response = ""
            elif response.lower() == "s":
                display_hand(hand)
                display_hand(dealer_hand, "display")
            elif response.lower() == "d":
                card_drawn = deck.draw()
                hand.append(card_drawn)
                display_hand(hand)
                display_hand(dealer_hand, "display")
                player_hand_total = add_player_total(hand)
            else:
                print("Invalid answer, please re-enter your choice:")
                continue