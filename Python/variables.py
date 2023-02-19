# ----- ----- ----- ----- ----- ----- ----- ----- ----- Imports ----- ----- ----- ----- ----- ----- ----- ----- ----- #
import random

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Arrays ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Creating suits and ranks for cards
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Players array
global players
players = ["Player 1", "Dealer"]

# Player hands
player_hand = []
dealer_hand = []

# ----- ----- ----- ----- ----- ----- ----- ----- Variables / Booleans ----- ----- ----- ----- ----- ----- ----- ----- #
# Player total (Blackjack count)
player_split_aces = None
player_split_hand = None
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
        self.rigged_cards = [
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
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Diamonds"),
        ]
        self.returned_cards = []

    def draw(self):
        # return self.cards.pop()
        return self.rigged_cards.pop()

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
        self.cards = self.returned_cards
        self.cards.reverse()
        print(len(self.cards))
        print("\n")

    def deal_rigged_order(self):
        print("\n")
        print("Here is the rigged deal of cards:")
        card_dealt_number = 1
        self.returned_cards = []
        for i in range(len(self.rigged_cards)):
            card_drawn = self.draw()
            self.returned_cards.append(card_drawn)
            print(f"Card dealt number: {card_dealt_number} - {card_drawn}")
            card_dealt_number += 1
        self.rigged_cards = self.returned_cards
        self.rigged_cards.reverse()
        print(f"{len(self.rigged_cards)} cards dealt.")
        print("\n")

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# ----- ----- ----- ----- ----- ----- ----- ----- Methods ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Add card total method
def add_card_total(hand):
    total = 0
    for sublist in hand:
        if isinstance(sublist, list):
            for card in sublist:
                total += card.value_of_card()
        else:
            total += sublist.value_of_card()
    return total

# Check for rank method
def check_for_rank(card, checking_rank):
    result = False
    if card.rank == checking_rank:
        result = True
    else:
        pass
    return result

# Check rank of cards method
def check_for_rank_in_hand(hand, checking_rank):
    result = False
    for card in hand:
        if check_for_rank(card, checking_rank):
            result = True
            break
    return result

# Check for same rank in hand
def check_same_rank(hand, checking_rank = None):
    result = True
    first_card_rank = hand[0].rank
    for card in hand[1:]:
        if card.rank != first_card_rank or (checking_rank is not None and card.rank != checking_rank):
            result = False
    return result

# Check for blackjack method
def check_for_blackjack(hand):
    result = False
    for card in hand:
        if card.card_value == 10:
            if check_for_rank_in_hand(hand, "Ace"):
                result = True
        else:
            continue
    return result

# Check for specific total
def check_for_total(hand, checking_total):
    global result
    result = False
    if add_card_total(hand) == checking_total:
        result = True
    else:
        result = False
    return result

# Deal method
def deal(deck):
    for turn in range(4):
        if (turn % 2) == 0:
            hit(deck, player_hand)
        elif (turn % 2 == 1):
            hit(deck, dealer_hand)
    if check_same_rank(player_hand, "Ace"):
        player_hand[0].card_value = 11
    if check_same_rank(dealer_hand, "Ace"):
        dealer_hand[1].card_value = 11
    return [player_hand, dealer_hand]

# Dealer play method
def dealer_play(deck, hands, dealer_hand_total):
    print("\n" "The dealer will now play their hand.")
    player_totals = []
    for current_hand in hands:
        player_totals.append(add_card_total(current_hand))
    all_over_21 = True
    for current_total in player_totals:
        if current_total <= 21:
            all_over_21 = False
            break
    if all_over_21:
        print("\n" "The player \033[1;33;40mhas busted\033[0m on both hands therefore the dealer has won both hands. "
              "Here are the \033[1;31;40mfinal hands\033[0m:")
        for current_hand in hands:
            show_hand(current_hand)
        show_hand(dealer_hand, 1)
    elif all_over_21 == False:
        while dealer_hand_total < 17:
            hit(deck, dealer_hand)
            dealer_hand_total = add_card_total(dealer_hand)
            print(f"Dealer hits, current hand: {dealer_hand} with \033[1;33;40mtotal value\033[0m"
                  f" of: \033[1;31;40m{dealer_hand_total}\033[0m.")
        hand_counter = 1
        for current_hand in hands:
            player_hand_total = add_card_total(current_hand)
            if player_hand_total > 21:
                print("\n" f"The player \033[1;33;40mhas busted\033[0m with a \033[1;31;40mfinal value\033[0m of "
                      f"\033[1;31;40m{player_hand_total}\033[0m. \033[1;31;40mPlayer has lost\033[0m hand "
                      f"\033[1;32;40m{hand_counter}\033[0m. Here are the \033[1;31;40mfinal"
                      f" hands\033[0m of the current hand:")
                show_hand(current_hand)
                show_hand(dealer_hand, 1)
            elif player_hand_total <= 21:
                if dealer_hand_total == player_hand_total:
                    print("\n" f"Both players have a \033[1;31;40mfinal value\033[0m of "
                          f"\033[1;31;40m{player_hand_total}\033[0m. Hand \033[1;32;40m{hand_counter}\033[0m"
                          f" is a push. Here are the \033[1;31;40mfinal hands\033[0m of the current hand:")
                    show_hand(current_hand)
                    show_hand(dealer_hand, 1)
                elif dealer_hand_total > player_hand_total and dealer_hand_total <= 21:
                    print("\n" f"The dealer \033[1;33;40mhas a greater\033[0m \033[1;31;40mfinal value\033[0m of"
                          f" \033[1;31;40m{dealer_hand_total}\033[0m. \033[1;31;40mPlayer has lost\033[0m hand"
                          f" \033[1;32;40m{hand_counter}\033[0m. Here are the \033[1;31;40mfinal"
                          f" hands\033[0m of the current hand:")
                    show_hand(current_hand)
                    show_hand(dealer_hand, 1)
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
                    show_hand(current_hand)
                    show_hand(dealer_hand, 1)
            hand_counter += 1

# Hit method
def hit(deck, hand):
    card_drawn = deck.draw()
    hand.append(card_drawn)
    if add_card_total(hand) > 21:
        for card in hand:
            if card.rank == "Ace":
                card.card_value = 1
    return [hand]

# Hit, Stay, Double Down method
def hit_stay_double_down(deck, hands):
    if player_split_aces != True:
        hand_counter = 1
        for current_hand in hands:
            if hand_counter == 1:
                place_holder = "First"
            elif hand_counter == 2:
                place_holder = "Second"
                hit(deck, current_hand)
            player_hand_total = add_card_total(current_hand)
            has_hit = False
            response = ""
            while response not in ["h", "s", "d"] and player_hand_total < 21:
                if not has_hit:
                    if hand_counter > 1:
                        print("\n" f"We are now on hand \033[1;32;40m{hand_counter}\033[0m." "\n" f"{players[0]}'s "
                              f"\033[1;33;40m{place_holder}\033[0m hand is: {current_hand} with "
                              f"\033[1;33;40mtotal value\033[0m of: \033[1;31;40m{add_card_total(current_hand)}\033[0m"
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
                    player_hand_total = add_card_total(current_hand)
                    if player_hand_total > 21:
                        print(f"Player \033[1;33;40mhas busted\033[0m on hand \033[1;32;40m{hand_counter}\033[0m with a"
                              f" \033[1;31;40mfinal value\033[0m of"
                              f" \033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                        show_hand(current_hand)
                        break
                    elif player_hand_total < 21:
                        print(
                            f"Player \033[1;33;40mhits\033[0m on hand \033[1;32;40m{hand_counter}\033[0m: {current_hand}"
                            f" with \033[1;33;40mtotal value\033[0m of: \033[1;31;40m{player_hand_total}\033[0m.")
                    elif player_hand_total == 21:
                        print(f"Player has \033[1;31;40m{player_hand_total}\033[0m. No more cards will be accepted.")
                        show_hand(current_hand)
                    response = ""
                elif response.lower() == "s":
                    player_hand_total = add_card_total(current_hand)
                    print(
                        f"Player has \033[1;33;40mchosen to stay\033[0m on hand \033[1;32;40m{hand_counter}\033[0m with "
                        f"a \033[1;31;40mfinal value\033[0m of"
                        f" \033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                    show_hand(current_hand)
                elif response.lower() == "d" and not has_hit:
                    hit(deck, current_hand)
                    player_hand_total = add_card_total(current_hand)
                    if player_hand_total > 21:
                        print(f"Player has \033[1;31;40mdoubled down\033[0m on hand "
                              f"\033[1;32;40m{hand_counter}\033[0m and busted with a \033[1;31;40mfinal value\033[0m of "
                              f"\033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                        show_hand(current_hand)
                    elif player_hand_total <= 21:
                        print(
                            f"Player has \033[1;31;40mdoubled down\033[0m on hand \033[1;32;40m{hand_counter}\033[0m with"
                            f" a \033[1;31;40mfinal value\033[0m of"
                            f" \033[1;31;40m{player_hand_total}\033[0m. Here is the \033[1;31;40mfinal hand\033[0m: ")
                        show_hand(current_hand)
                else:
                    print("\033[1;31;40mInvalid choice\033[0m." "\n")
                    continue
            hand_counter += 1
    else:
        pass
    print("\n" "Here are the \033[1;31;40mfinal hands\033[0m of the player: ")
    for current_hand in hands:
        show_hand(current_hand)
    dealer_hand_total = add_card_total(dealer_hand)
    dealer_play(deck, hands, dealer_hand_total)

# Player same rank method
def player_same_rank_check(deck):
    global player_split_aces
    global player_split_hand
    if check_same_rank(player_hand, "Ace"):
        aces_response = ""
        while (aces_response not in ["y", "n"]):
            aces_response = input("\n" f"You have two {player_hand[0].rank}'s in your hand. Would you like to split"
                                  f" your hand? You may only split your hand once. (y/n): ")
            if aces_response.lower() == "y":
                print("\n" f"You have chosen not to split your {player_hand[0].rank}'s." "\n")
                hand_1 = split_hand(player_hand)[0][0]
                hand_2 = split_hand(player_hand)[0][1]
                hit(deck, hand_1)
                hit(deck, hand_2)
                if check_same_rank(hand_1, "Ace"):
                    hand_1[0].card_value = 11
                    hand_1[1].card_value = 1
                else:
                    for card in hand_1:
                        if check_for_rank(card, "Ace"):
                            card.card_value = 11
                        else:
                            pass
                if check_same_rank(hand_2, "Ace"):
                    hand_2[0].card_value = 11
                    hand_2[1].card_value = 1
                else:
                    for card in hand_2:
                        if check_for_rank(card, "Ace"):
                            card.card_value = 11
                        else:
                            pass
                player_split_aces = True
                new_hand = [hand_1, hand_2]
                break
            elif aces_response.lower() == "n":
                print("\n" f"You have chosen not to split your {player_hand[0].rank}'s." "\n")
                player_split_aces = False
                new_hand = player_hand
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    elif check_same_rank(player_hand):
        same_rank_response = ""
        while same_rank_response not in ["y", "n"]:
            same_rank_response = input("\n" f"You have the same rank of {player_hand[0].rank} in your hand. Would you like"
                                       f" to split your hand? (y/n): ")
            if same_rank_response.lower() == "y":
                print("\n" f"You have chosen to split your {player_hand[0].rank}'s." "\n")
                hand_1 = split_hand(player_hand)[0][0]
                hand_2 = split_hand(player_hand)[0][1]
                hit(deck, hand_1)
                player_split_hand = True
                new_hand = [hand_1, hand_2]
                break
            elif same_rank_response.lower() == "n":
                print("\n" f"You have chosen not to split your {player_hand[0].rank}'s." "\n")
                player_split_hand = False
                new_hand = player_hand
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    else:
        new_hand = player_hand
    return [new_hand, player_split_aces, player_split_hand]

# Re-Assing Ace's value method
def reassign_ace_value(hand):
    for card in hand:
        if card.rank == "Ace" and card.card_value == 11:
            card.card_value = 1
            break
        else:
            pass
    return [hand]

# Show hands of players method
def show_hand(hand, dealer_display = None):
    if hand != dealer_hand:
        if isinstance(hand, list) and isinstance(hand[0], list):
            for current_hand in hand:
                print(f"{players[0]}'s current hand is: {current_hand} {add_card_total(current_hand)}")
        else:
            print(f"{players[0]}'s hand is: {hand} {add_card_total(hand)}")
    elif hand == dealer_hand and dealer_display is None:
        print(f"{players[-1]}'s hand is: [Hidden, {hand[1]}] {hand[1].card_value}")
    elif hand == dealer_hand and dealer_display is not None:
        print(f"{players[-1]}'s hand is {hand} {add_card_total(hand)}")

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