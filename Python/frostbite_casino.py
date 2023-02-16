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
    if isinstance(hand, list):
        total = 0
        for card in hand:
            total += card.value_of_card()
    else:
        total = hand.value_of_card()
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
        if isinstance(hand, list) and isinstance(hand[0], list):
            counter = 1
            for current_hand in hand:
                if counter == 1:
                    place_holder = "First"
                elif counter == 2:
                    place_holder = "Second"
                elif counter == 3:
                    place_holder = "Third"
                elif counter ==4:
                    place_holder = "Fourth"
                print(f"{players[0]}'s {place_holder} hand is: {current_hand} with \033[1;33;40mtotal "
                      f"value\033[0m of: \033[1;31;40m{add_player_total(current_hand)}\033[0m")
                counter += 1
        else:
            print(f"{players[0]}'s hand is: {hand} with \033[1;33;40mtotal "
                  f"value\033[0m of: \033[1;31;40m{add_player_total(hand)}\033[0m")
    elif hand == dealer_hand and display is None:
        print(f"{players[-1]}'s hand is: [Hidden, " + f"{hand[-1]}] with \033[1;33;40mtotal value\033[0m of: "
              f"\033[1;31;40m{add_player_total(hand) - hand[0].value_of_card()}\033[0m")
    elif hand == dealer_hand and display is not None:
        print(f"{players[1]}'s hand is: {hand} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(hand)}\033[0m")

# Hit method
def player_hit(deck, hand):
    hand_total = sum([card.value_of_card() for card in hand])
    card_drawn = deck.draw()
    hand.append(card_drawn)

# Dealer hit method
def dealer_hit(deck, hand, dealer_hand_total, player_hand_total):
    print("The dealer will now play their hand.")
    while dealer_hand_total < 17:
        card_drawn = deck.draw()
        dealer_hand.append(card_drawn)
        dealer_hand_total = add_player_total(dealer_hand)
        print(f"Dealer hits, current hand: {dealer_hand} with \033[1;33;40mtotal value\033[0m"
              f" of: \033[1;31;40m{dealer_hand_total}\033[0m.")
    if dealer_hand_total >= 17 and dealer_hand_total <= 21:
        if dealer_hand_total == player_hand_total:
            print("\n")
            print(f"Each player has the same final value of {player_hand_total}. Final hands are: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
        elif dealer_hand_total > player_hand_total:
            print("\n")
            print(f"The dealer has a greater final value {dealer_hand_total}, the dealer wins. Final hands are: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
        elif dealer_hand_total < player_hand_total:
            print("\n")
            print(f"The player has a greater final value of {player_hand_total}, player wins. Final hands are: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
    elif dealer_hand_total > 21:
        print("\n")
        print(f"The dealer has broken with a value of {dealer_hand_total}, player wins. Final hands are: ")
        display_hand(hand)
        display_hand(dealer_hand, 1)

# Hit, stay, double down method
def hit_stay_double_down(deck, hand):
    player_hand_total = add_player_total(hand)
    dealer_hand_total = add_player_total(dealer_hand)
    has_hit = False
    response = ""
    while response not in ["h", "s", "d"] and player_hand_total < 21:
        if not has_hit:
            print("\n")
            response = input("Would you like to hit, stay, or double down? (h/s/d): ")
            print("\n")
        elif has_hit:
            print("\n")
            response = input("Would you like to hit or stay? (h/s): ")
            while response.lower() not in ["h", "s"]:
                response = input("Invalid response. Would you like to hit or stay? (h/s): ")
            print("\n")
        if response.lower() == "h":
            has_hit = True
            player_hit(deck, hand)
            player_hand_total = add_player_total(hand)
            dealer_hand_total = add_player_total(dealer_hand)
            if player_hand_total > 21:
                print("Player has busted, the dealer wins. Final hands are: ")
                display_hand(hand)
                display_hand(dealer_hand, 1)
                break
            elif player_hand_total < 21:
                print(f"Player hits, current: {hand} with \033[1;33;40mtotal value\033[0m"
                      f" of: \033[1;31;40m{player_hand_total}\033[0m.")
                display_hand(dealer_hand)
            elif player_hand_total == 21:
                display_hand(hand)
                display_hand(dealer_hand, 1)
                print("\n")
                dealer_hit(deck, hand, dealer_hand_total, player_hand_total)
            response = ""
        elif response.lower() == "s":
            player_hand_total = add_player_total(hand)
            dealer_hand_total = add_player_total(dealer_hand)
            print(f"Player has chosen to stay with a final value of {player_hand_total}. Here are the final hands: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
            print("\n")
            dealer_hit(deck, hand, dealer_hand_total, player_hand_total)
        elif response.lower() == "d" and not has_hit:
            player_hit(deck, hand)
            player_hand_total = add_player_total(hand)
            dealer_hand_total = add_player_total(dealer_hand)
            if player_hand_total > 21:
                print(f"Player has busted with a final value of {player_hand_total}, dealer wins. Final hands are: ")
                display_hand(hand)
                display_hand(dealer_hand, 1)
            elif player_hand_total <= 21:
                print(f"Player has doubled down with a final value of {player_hand_total}. \n")
                display_hand(hand)
                display_hand(dealer_hand, 1)
                print("\n")
                dealer_hit(deck, hand, dealer_hand_total, player_hand_total)
        else:
            print("Invalid answer, please re-enter your choice:")
            continue

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
    hands = []
    current_hand = []
    for card in hand:
        current_hand.append(card)
        if card.rank == hand[0].rank:
            hands.append(current_hand)
            current_hand = []
    if current_hand:
        hands.append(current_hand)
    return [hands]

# Player same rank method
def player_same_rank_check():
    if check_same_rank(player_hand):
        if check_same_rank(player_hand, "Ace"):
            aces_response = ""
            while aces_response not in ["y", "n"]:
                aces_response = input("You have two Aces in your hand, would you like to split your hand? "
                                      "You may only split once. (y/n): ")
                if aces_response.lower() == "y":
                    print("\n" "You have chosen to split your Aces." "\n")
                    return split_hand(player_hand)[0]
                    break
                elif aces_response.lower() == "n":
                    print("\n" "You have chosen to not split your Aces." "\n")
                    new_player_hand = reassign_ace_value(player_hand)
                    return new_player_hand
                    break
                else:
                    print("\n" "Invalid choice." "\n")
                    continue
        else:
            same_rank_response = ""
            while same_rank_response not in ["y", "n"]:
                same_rank_response = input(f"You have the same rank of {player_hand[0].rank} in your hand, would you like "
                                           f"to split your hand? (y/n): ")
                if same_rank_response.lower() == "y":
                    print("\n" f"You have chosen to split your {player_hand[0].rank}'s." "\n")
                    return split_hand(player_hand)[0]
                    break
                elif same_rank_response.lower() == "n":
                    print("\n" f"You have chosen to not split your {player_hand[0].rank}'s." "\n")
                    return player_hand
                    break
                else:
                    print("\n" "Invalid choice." "\n")
                    continue
    else:
        return player_hand

# Deal method
def deal(deck):
    for turn in range(4):
        card_drawn = deck.draw()
        if (turn % 2) == 0:
            player_hand.append(card_drawn)
        elif (turn % 2) == 1:
            dealer_hand.append(card_drawn)

# Hit method
def player_hit(deck, hand):
    # hand_total = sum([card.value_of_card() for card in hand])
    card_drawn = deck.draw()
    hand.append(card_drawn)

# Dealer hit method
def dealer_hit(deck, hand, dealer_hand_total, player_hand_total):
    print("The dealer will now play their hand.")
    while dealer_hand_total < 17:
        card_drawn = deck.draw()
        dealer_hand.append(card_drawn)
        dealer_hand_total = add_player_total(dealer_hand)
        print(f"Dealer hits, current hand: {dealer_hand} with \033[1;33;40mtotal value\033[0m"
              f" of: \033[1;31;40m{dealer_hand_total}\033[0m.")
    if dealer_hand_total >= 17 and dealer_hand_total <= 21:
        if dealer_hand_total == player_hand_total:
            print("\n" f"Each player has the same final value of {player_hand_total}. Final hands are: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
        elif dealer_hand_total > player_hand_total:
            print("\n" f"The dealer has a greater final value {dealer_hand_total}, the dealer wins. Final hands are: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
        elif dealer_hand_total < player_hand_total:
            print("\n" f"The player has a greater final value of {player_hand_total}, player wins. Final hands are: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
    elif dealer_hand_total > 21:
        print("\n" f"The dealer has broken with a value of {dealer_hand_total}, player wins. Final hands are: ")
        display_hand(hand)
        display_hand(dealer_hand, 1)

# Hit, stay, double down method
def hit_stay_double_down(deck, hand):
    player_hand_total = add_player_total(hand)
    has_hit = False
    response = ""
    while response not in ["h", "s", "d"] and player_hand_total < 21:
        if not has_hit:
            response = input("Would you like to hit, stay, or double down? (h/s/d): ")
            print("\n")
        elif has_hit:
            print("\n")
            response = input("Would you like to hit or stay? (h/s): ")
            print("\n")
        if response.lower() == "h":
            has_hit = True
            player_hit(deck, hand)
            player_hand_total = add_player_total(hand)
            dealer_hand_total = add_player_total(dealer_hand)
            if player_hand_total > 21:
                print("Player has busted, the dealer wins. Final hands are: ")
                display_hand(hand)
                display_hand(dealer_hand, 1)
                break
            elif player_hand_total < 21:
                print(f"Player hits, current: {hand} with \033[1;33;40mtotal value\033[0m"
                      f" of: \033[1;31;40m{player_hand_total}\033[0m.")
                display_hand(dealer_hand)
            elif player_hand_total == 21:
                display_hand(hand)
                display_hand(dealer_hand, 1)
                print("\n")
                dealer_hit(deck, hand, dealer_hand_total, player_hand_total)
            response = ""
        elif response.lower() == "s":
            player_hand_total = add_player_total(hand)
            dealer_hand_total = add_player_total(dealer_hand)
            print(f"Player has chosen to stay with a final value of {player_hand_total}. Here are the final hands: ")
            display_hand(hand)
            display_hand(dealer_hand, 1)
            print("\n")
            dealer_hit(deck, hand, dealer_hand_total, player_hand_total)
        elif response.lower() == "d" and not has_hit:
            player_hit(deck, hand)
            player_hand_total = add_player_total(hand)
            dealer_hand_total = add_player_total(dealer_hand)
            if player_hand_total > 21:
                print(f"Player has busted with a final value of {player_hand_total}, dealer wins. Final hands are: ")
                display_hand(hand)
                display_hand(dealer_hand, 1)
            elif player_hand_total <= 21:
                print(f"Player has doubled down with a final value of {player_hand_total}. \n")
                display_hand(hand)
                display_hand(dealer_hand, 1)
                print("\n")
                dealer_hit(deck, hand, dealer_hand_total, player_hand_total)
        else:
            print("Invalid choice." "\n")
            continue

# Deal hands method
def deal_hand(deck):
    deal(deck)
    print("\n" "Here are the initial hands of each player: ")
    display_hand(player_hand)
    display_hand(dealer_hand)
    print("\n")
    if dealer_showing_ace():
        choice = ""
        while choice.lower() not in ["y", "n"]:
            choice = input("The dealer is showing an Ace, would you like to buy insurance? (y/n): ")
            print("\n")
            if choice.lower() == "y":
                print("Player has chosen to buy insurance, we will now check for if the dealer has Blackjack: " "\n")
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
                    print("Neither player has Blackjack, player loses insurance." "\n")
                    if check_same_rank(dealer_hand, "Ace"):
                        reassign_ace_value(dealer_hand)
                    else:
                        continue
                    hit_stay_double_down(deck, player_same_rank_check())
            elif choice.lower() == "n":
                print("Player has chosen to not buy insurance. We will now check if the dealer has Blackjack: " "\n")
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
                    print("Neither player has Blackjack." "\n")
                    if check_same_rank(dealer_hand, "Ace"):
                        reassign_ace_value(dealer_hand)
                    else:
                        continue
                    hit_stay_double_down(deck, player_same_rank_check())
            else:
                print("Invalid choice." "\n")
    elif dealer_showing_ace() == False:
        if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
            print("Both players have Blackjack, it is a push.")
        elif check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand) == False:
            print("Dealer has Blackjack. Dealer wins.")
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
            print("Player has Blackjack. Player wins.")
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
            hit_stay_double_down(deck, player_same_rank_check())
    print("\n" "This hand has ended. On to the next!" "\n")