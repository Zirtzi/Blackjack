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
        self.rigged_order = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("10", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
        ]
        self.returned_cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.rigged_order.pop()
        # return self.cards.pop()

    def deal_cards(self):
        print("\n")
        print("Here are the deck of cards:")
        card_dealt_number = 1
        self.returned_cards = []
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
    card_2 = hand[1]
    if checking_rank is None:
        if card_1.rank == card_2.rank:
            result = True
    elif checking_rank is not None:
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

# Deal method
def deal(deck):
    for turn in range(4):
        if (turn % 2) == 0:
            player_hand.append(deck.draw())
        elif (turn % 2 == 1):
            dealer_hand.append(deck.draw())
    return [player_hand, dealer_hand]

# Deal hands method
def deal_hand(deck):
    deal(deck)
    print("\n" "Here are the initial hands of each player: ")
    display_hand(player_hand)
    display_hand(dealer_hand)
    print("\n")
    parameter_check(player_hand)
    parameter_check(dealer_hand)
    print("\n")
    if dealer_showing_ace():
        choice = ""
        while choice.lower() not in ["y", "n"]:
            choice = input("The dealer is showing an Ace, would you like to buy insurance? \033[1;34;40m(y/n): \033[0m")
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
                    # hit_stay_double_down(deck, player_same_rank_check(deck))
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
                    # hit_stay_double_down(deck, player_same_rank_check(deck))
            else:
                print("\033[1;31;40mInvalid choice\033[0m." "\n")
    elif dealer_showing_ace() == False:
        if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
            print("Both players have Blackjack, it is a push.")
        elif check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand) == False:
            print("Dealer has Blackjack. Dealer wins.")
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
            print("Player has Blackjack. Player wins.")
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
            hit_stay_double_down(deck, player_same_rank_check(deck)[0])
    print("\n" "This hand has ended. On to the next!" "\n")

# Dealer play method
def dealer_play(deck, hands, dealer_hand_total):
    print("\n" "The dealer will now play their hand.")
    player_totals = []
    for current_hand in hands:
        player_totals.append(add_player_total(current_hand))
    all_over_21 = True
    for current_total in player_totals:
        if current_total <= 21:
            all_over_21 = False
            break
    if all_over_21:
        print("\n" "The player \033[1;33;40mhas busted\033[0m on both hands therefore the dealer has won both hands. "
              "Here are the \033[1;31;40mfinal hands\033[0m:")
        for current_hand in hands:
            display_hand(current_hand)
        display_hand(dealer_hand, 1)
    elif all_over_21 == False:
        while dealer_hand_total < 17:
            hit(deck, dealer_hand)
            dealer_hand_total = add_player_total(dealer_hand)
            print(f"Dealer hits, current hand: {dealer_hand} with \033[1;33;40mtotal value\033[0m"
                  f" of: \033[1;31;40m{dealer_hand_total}\033[0m.")
        hand_counter = 1
        for current_hand in hands:
            player_hand_total = add_player_total(current_hand)
            if player_hand_total > 21:
                print("\n" f"The player \033[1;33;40mhas busted\033[0m with a \033[1;31;40mfinal value\033[0m of "
                      f"\033[1;31;40m{player_hand_total}\033[0m. \033[1;31;40mPlayer has lost\033[0m hand "
                      f"\033[1;32;40m{hand_counter}\033[0m. Here are the \033[1;31;40mfinal"
                      f" hands\033[0m of the current hand:")
                display_hand(current_hand)
                display_hand(dealer_hand, 1)
            elif player_hand_total <= 21:
                if dealer_hand_total == player_hand_total:
                    print("\n" f"Both players have a \033[1;31;40mfinal value\033[0m of "
                          f"\033[1;31;40m{player_hand_total}\033[0m. Hand \033[1;32;40m{hand_counter}\033[0m"
                          f" is a push. Here are the \033[1;31;40mfinal hands\033[0m of the current hand:")
                    display_hand(current_hand)
                    display_hand(dealer_hand, 1)
                elif dealer_hand_total > player_hand_total and dealer_hand_total <= 21:
                    print("\n" f"The dealer \033[1;33;40mhas a greater\033[0m \033[1;31;40mfinal value\033[0m of"
                          f" \033[1;31;40m{dealer_hand_total}\033[0m. \033[1;31;40mPlayer has lost\033[0m hand"
                          f" \033[1;32;40m{hand_counter}\033[0m. Here are the \033[1;31;40mfinal"
                          f" hands\033[0m of the current hand:")
                    display_hand(current_hand)
                    display_hand(dealer_hand, 1)
                elif dealer_hand_total < player_hand_total or dealer_hand_total > 21:
                    if dealer_hand_total <= 21:
                        print("\n" f"The player \033[1;33;40mhas a greater\033[0m \033[1;31;40mfinal value\033[0m of"
                              f" \033[1;31;40m{player_hand_total}\033[0m. \033[1;31;40mPlayer has won\033[0m hand"
                              f" \033[1;32;40m{hand_counter}\033[0m. Here are the \033[1;31;40mfinal"
                              f" hands\033[0m of the current hand:")
                    elif dealer_hand_total > 21:
                        print("\n" f"The dealer \033[1;33;40mhas busted\033[0m with a"
                              f" \033[1;31;40mfinal value\033[0m of {dealer_hand_total}."
                              f" \033[1;31;40mPlayer has won\033[0m hand \033[1;32;40m{hand_counter}\033[0m."
                              f" Here are the \033[1;31;40mfinal hands\033[0m of the current hand:")
                    display_hand(current_hand)
                    display_hand(dealer_hand, 1)
            hand_counter += 1

# Dealer showing Ace
def dealer_showing_ace():
    result = False
    if dealer_hand[1].rank == "Ace":
        result = True
    else:
        result = False
    return result

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
                print(f"{players[0]}'s \033[1;33;40m{place_holder}\033[0m hand is: "
                      f"{current_hand} with \033[1;33;40mtotal value\033[0m of: "
                      f"\033[1;31;40m{add_player_total(current_hand)}\033[0m")
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
def hit(deck, hand):
    card_drawn = deck.draw()
    hand.append(card_drawn)
    if add_player_total(hand) > 21:
        for card in hand:
            if card.rank == "Ace":
                card.card_value = 1
    return [hand]

# Hit, Stay, Double Down method
def hit_stay_double_down(deck, hands):
    hand_counter = 1
    for current_hand in hands:
        if hand_counter == 1:
            place_holder = "First"
        elif hand_counter == 2:
            place_holder = "Second"
            hit(deck, current_hand)
        player_hand_total = add_player_total(current_hand)
        has_hit = False
        response = ""
        while response not in ["h", "s", "d"] and player_hand_total < 21:
            if not has_hit:
                if hand_counter > 1:
                    print("\n" f"We are now on hand \033[1;32;40m{hand_counter}\033[0m." "\n" f"{players[0]}'s "
                          f"\033[1;33;40m{place_holder}\033[0m hand is: {current_hand} with "
                          f"\033[1;33;40mtotal value\033[0m of: \033[1;31;40m{add_player_total(current_hand)}\033[0m"
                          f"\n")
                response = input(f"Would you like to \033[1;31;40mhit, stay, or double down\033[0m on the"
                                 f" \033[1;33;40m{place_holder}\033[0m hand? \033[1;34;40m(h/s/d):\033[0m ")
                print("\n")
            elif has_hit:
                print("\n")
                response = input(f"Would you like to \033[1;31;40mhit or stay\033[0m"
                                 f" on the \033[1;33;40m{place_holder}\033[0m hand?? \033[1;34;40m(h/s):\033[0m ")
                print("\n")
            if response.lower() == "h":
                has_hit = True
                hit(deck, current_hand)
                player_hand_total = add_player_total(current_hand)
                if player_hand_total > 21:
                    print(f"Player \033[1;33;40mhas busted\033[0m on hand \033[1;32;40m{hand_counter}\033[0m with a"
                          f" \033[1;31;40mfinal value\033[0m of"
                          f" \033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                    display_hand(current_hand)
                    break
                elif player_hand_total < 21:
                    print(
                        f"Player \033[1;33;40mhits\033[0m on hand \033[1;32;40m{hand_counter}\033[0m: {current_hand}"
                        f" with \033[1;33;40mtotal value\033[0m of: \033[1;31;40m{player_hand_total}\033[0m.")
                elif player_hand_total == 21:
                    print(f"Player has \033[1;31;40m{player_hand_total}\033[0m. No more cards will be accepted.")
                    display_hand(current_hand)
                response = ""
            elif response.lower() == "s":
                player_hand_total = add_player_total(current_hand)
                print(
                    f"Player has \033[1;33;40mchosen to stay\033[0m on hand \033[1;32;40m{hand_counter}\033[0m with "
                    f"a \033[1;31;40mfinal value\033[0m of"
                    f" \033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                display_hand(current_hand)
            elif response.lower() == "d" and not has_hit:
                hit(deck, current_hand)
                player_hand_total = add_player_total(current_hand)
                if player_hand_total > 21:
                    print(f"Player has \033[1;31;40mdoubled down\033[0m on hand "
                          f"\033[1;32;40m{hand_counter}\033[0m and busted with a \033[1;31;40mfinal value\033[0m of "
                          f"\033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                    display_hand(current_hand)
                elif player_hand_total <= 21:
                    print(
                        f"Player has \033[1;31;40mdoubled down\033[0m on hand \033[1;32;40m{hand_counter}\033[0m with"
                        f" a \033[1;31;40mfinal value\033[0m of"
                        f" \033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                    display_hand(current_hand)
            else:
                print("\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
        hand_counter += 1
    print("\n" "Here are the \033[1;31;40mfinal hands\033[0m of the player: ")
    for current_hand in hands:
        display_hand(current_hand)
    dealer_hand_total = add_player_total(dealer_hand)
    dealer_play(deck, hands, dealer_hand_total)

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

# Player same rank method
def player_same_rank_check(deck):
    global player_split_aces
    global player_split_hand
    player_split_aces = False
    player_split_hand = False
    if check_same_rank(player_hand, "Ace"):
        aces_response = ""
        while (aces_response not in ["y", "n"]) and player_split_aces == False:
            aces_response = input("You have two \033[1;32;40mAces\033[0m in your hand,"
                                  " would you like to \033[1;31;40msplit\033[0m your hand? "
                                  "You may only split \033[1;31;40monce\033[0m. \033[1;34;40m(y/n)\033[0m: ")
            if aces_response.lower() == "y":
                print("\n" "You have \033[1;31;40mchosen to split\033[0m your \033[1;32;40mAces\033[0m." "\n")
                hand_1 = split_hand(player_hand)[0][0]
                hand_2 = split_hand(player_hand)[0][1]
                hit(deck, hand_1)
                hit(deck, hand_2)
                if check_same_rank(hand_1, "Ace"):
                    reassign_ace_value(hand_1)
                if check_same_rank(hand_2, "Ace"):
                    reassign_ace_value(hand_2)
                display_hand([hand_1, hand_2])
                player_split_aces = True
                print("\n")
                return [[hand_1, hand_2], player_split_aces]
                break
            elif aces_response.lower() == "n":
                print("\n" "You have \033[1;31;40mchosen to not split\033[0m your \033[1;32;40mAces\033[0m." "\n")
                new_player_hand = reassign_ace_value(player_hand)
                display_hand(new_player_hand)
                print("\n")
                return [[new_player_hand], player_split_aces]
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    elif check_same_rank(player_hand):
        same_rank_response = ""
        while same_rank_response not in ["y", "n"]:
            same_rank_response = input(f"You have the \033[1;33;40msame rank\033[0m of "
                                       f"\033[1;32;40m{player_hand[0].rank}\033[0m in your hand,"
                                       f" would you like to \033[1;31;40msplit\033[0m your hand?"
                                       f" \033[1;34;40m(y/n):\033[0m ")
            if same_rank_response.lower() == "y":
                print("\n" f"You have \033[1;31;40mchosen to split\033[0m your"
                      f" \033[1;32;40m{player_hand[0].rank}\033[0m's." "\n")
                hand_1 = split_hand(player_hand)[0][0]
                hand_2 = split_hand(player_hand)[0][1]
                hit(deck, hand_1)
                display_hand([hand_1, hand_2])
                player_split_hand = True
                print("\n")
                return [[hand_1, hand_2], player_split_hand]
                break
            elif same_rank_response.lower() == "n":
                print("\n" f"You have \033[1;31;40mchosen to not split\033[0m your"
                      f" \033[1;32;40m{player_hand[0].rank}\033[0m's." "\n")
                display_hand(player_hand)
                print("\n")
                print(player_split_hand)
                return [[player_hand], player_split_hand]
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    else:
        return [[player_hand], player_split_hand]

# Re-Assing Ace's value method
def reassign_ace_value(hand):
    for card in hand:
        if card.rank == "Ace" and card.card_value == 11:
            card.card_value = 1
            break
        else:
            pass
    return [hand]
    # num_aces_with_value_11 = 0
    # for card in hand:
    #     if card.rank == "Ace":
    #         if num_aces_with_value_11 == 0:
    #             card.card_value = 11
    #             num_aces_with_value_11 += 1
    #         else:
    #             card.card_value = 1
    #     else:
    #         pass
    # return [hand]

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