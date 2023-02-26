# ----- ----- ----- ----- ----- ----- ----- ----- ----- Imports ----- ----- ----- ----- ----- ----- ----- ----- ----- #
import random, time

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Arrays ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Creating suits and ranks for cards
Suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Players array
Players = ["Player 1", "Dealer"]

# Player hands
Player_Hand = []
Dealer_Hand = []

# ----- ----- ----- ----- ----- ----- ----- ----- Variables / Booleans ----- ----- ----- ----- ----- ----- ----- ----- #
# Player total (Game Total)
Player_Total = 0
Dealer_Total = 0

# Split hand booleans
Player_Split_Aces = None
Player_Split_Hand = None

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Classes ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Card Class
class Card:
    # Constructor
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        if rank == "Ace":
            self.card_value = 11
        elif rank in ["10", "Jack", "Queen", "King"]:
            self.card_value = 10
        else:
            self.card_value = int(rank)

    # Value of card method
    def Value_of_Card(self):
        return self.card_value

    # Representation method
    def __repr__(self):
        return f"\033[1;32m{self.rank}\033[0m of \033[1;34m{self.suit}\033[0m"

# Deck class
class Deck:
    # Constructor
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Ranks for suit in Suits]
        self.rigged_cards = []
        self.returned_cards = []

    # Draw method
    def Draw(self):
        return self.cards.pop()
        # return self.rigged_cards.pop()

    # Deal random cards method
    def Deal_Cards(self):
        print("\n" "Here are the cards from a shuffled deck:")
        card_dealt_number = 1
        self.returned_cards = []
        for i in range(len(self.cards)):
            card_drawn = self.Draw()
            self.returned_cards.append(card_drawn)
            print(f"Card dealt number: {card_dealt_number} - {card_drawn}")
            card_dealt_number += 1
        self.cards = self.returned_cards
        self.cards.reverse()
        print(len(self.cards), " Cards remaining from shuffled deck" "\n")
        time.sleep(1)

    # Deal rigged cards method
    def Deal_Rigged_Cards(self):
        print("\n" "Here are the cards from a rigged deck:")
        card_dealt_number = 1
        self.returned_cards = []
        for i in range(len(self.rigged_cards)):
            card_drawn = self.Draw()
            self.returned_cards.append(card_drawn)
            print(f"Card dealt number: {card_dealt_number} - {card_drawn}")
            card_dealt_number += 1
        self.rigged_cards = self.returned_cards
        self.rigged_cards.reverse()
        print(len(self.rigged_cards), " Cards remaining from rigged deck" "\n")
        time.sleep(1)

    # Shuffle method
    def Shuffle(self):
        random.shuffle(self.cards)

    # Representation method
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# ----- ----- ----- ----- ----- ----- ----- Game Methods ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Add card total method
def add_card_total(hand):
    if isinstance(hand, list) and all(isinstance(hands, list) for hands in hand):
        total = 0
        for subhand in hand:
            for card in subhand:
                total += card.Value_of_Card()
        return int(total)
    elif isinstance(hand, list) and not all(isinstance(hands, list) for hands in hand):
        total = 0
        for card in hand:
            total += card.Value_of_Card()
        return int(total)
    else:
        raise ValueError("\033[1;31;40mHand is not a list.\033[0m")

# Check for rank of card method
def check_rank_of_card(card, checking_rank):
    result = False
    if card.rank == checking_rank:
        result = True
    else:
        pass
    return result

# Check for rank in hand method
def check_rank_in_hand(hand, checking_rank):
    result = False
    for card in hand:
        if check_rank_of_card(card, checking_rank):
            result = True
            break
    return result

# Check for same rank in hand
def check_same_rank_in_hand(hand, checking_rank = None):
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
            if check_rank_in_hand(hand, "Ace"):
                result = True
        else:
            continue
    return result

# Deal hand method
def deal_hand(deck):
    for turn in range(4):
        if (turn % 2) == 0:
            hit_hand(deck, Player_Hand)
        elif (turn % 2) == 1:
            hit_hand(deck, Dealer_Hand)
    player_aces_count = sum(card.rank == "Ace" for card in Player_Hand)
    dealer_aces_count = sum(card.rank == "Ace" for card in Dealer_Hand)
    for card in Player_Hand:
        if player_aces_count == 1:
            if check_rank_of_card(card, "Ace"):
                card.card_value = 11
            else:
                pass
        elif player_aces_count > 1:
            if check_rank_of_card(card, "Ace"):
                card.card_value = 1
            else:
                pass
        player_aces_count -= 1
    for card in Dealer_Hand:
        if dealer_aces_count == 1:
            if check_rank_of_card(card, "Ace"):
                card.card_value = 11
            else:
                pass
        elif dealer_aces_count > 1:
            if check_rank_of_card(card, "Ace"):
                card.card_value = 1
            else:
                pass
        dealer_aces_count -= 1
    show_hand(Player_Hand)
    show_hand(Dealer_Hand)
    return [Player_Hand, Dealer_Hand]

# Dealer logic method
def dealer_logic(deck, hand):
    global Dealer_Total
    global Player_Total
    Dealer_Total = add_card_total(Dealer_Hand)
    Player_Total = add_card_total(hand)
    if value_check("<=", Player_Total, 21):
        while value_check("<", Dealer_Total, 17):
            hit_hand(deck, Dealer_Hand)
            Dealer_Total = add_card_total(Dealer_Hand)
            time.sleep(1)
            print(f"Dealer hits, current hand: {Dealer_Hand} with a current total"
                  f" of \033[1;31;40m{Dealer_Total}\033[0m")
    elif value_check(">", Player_Total, 21):
        time.sleep(1)
        print("\n" f"Player has busted with a final value of \033[1;31;40m{Player_Total}\033[0m."
              f" \033[1;31;40mPlayer loses\033[0m.")
        time.sleep(1)
        show_hand(hand)
        time.sleep(1)
        show_hand(Dealer_Hand, 1)
    else:
        pass
    print("\n")
    if value_check("<=", Player_Total, 21):
        if value_check("==", Dealer_Total, Player_Total):
            time.sleep(1)
            print(f"Both players have the same final value of \033[1;31;40m{Player_Total}\033[0m."
                  f" It is \033[1;31;40ma push\033[0m. Here are the final hands:")
            time.sleep(1)
            show_hand(hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        elif value_check(">", Dealer_Total, Player_Total) and value_check("<=", Dealer_Total, 21):
            time.sleep(1)
            print(f"Dealer has a greater final value of \033[1;31;40m{Dealer_Total}\033[0m."
                  f" \033[1;31;40mPlayer loses\033[0m. Here are the final hands:")
            time.sleep(1)
            show_hand(hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        elif value_check("<", Dealer_Total, Player_Total):
            time.sleep(1)
            print(f"Player has a greater final value of \033[1;31;40m{Player_Total}\033[0m."
                  f" \033[1;31;40mPlayer wins\033[0m. Here are the final hands:")
            time.sleep(1)
            show_hand(hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        elif value_check(">", Dealer_Total, 21):
            time.sleep(1)
            print(f"Dealer has busted with a final value of \033[1;31;40m{Dealer_Total}\033[0m."
                  f" \033[1;31;40mPlayer wins\033[0m. Here are the final hands:")
            time.sleep(1)
            show_hand(hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        else:
            pass

# Dealer play method
def dealer_play(deck ,hand):
    global Dealer_Total
    global Player_Total
    player_totals = []
    all_over_21 = False
    if isinstance(hand, list) and not any(isinstance(hands, list) for hands in hand):
        player_totals.append(add_card_total(hand))
    elif isinstance(hand, list) and all(isinstance(hands, list) for hands in hand):
        for current_hand in hand:
            player_totals.append(add_card_total(current_hand))
    else:
        raise ValueError("This is an incorrect data type.")
    for current_total in player_totals:
        if value_check("<", current_total, 21):
            all_over_21 = False
            break
    if value_check("<=", Dealer_Total, 17):
        print("\n" "The dealer will now play their hand.")
        show_hand(Dealer_Hand, 1)
    elif value_check(">", Dealer_Total, 17) and value_check("<=", Dealer_Total, 21):
        print("\n" "The dealer does not need to play their hand with a final value of"
              f" \033[1;31;40m{Dealer_Total}\033[0m.")
        show_hand(Dealer_Hand, 1)
    elif value_check(">", Dealer_Total, 17):
        print("\n" f"The dealer has busted with a final value of \033[1;31;40m{Dealer_Total}\033[0m.")
    if all_over_21:
        print("\n" "The player has busted on both hands therefore the dealer has won both hands."
              " Here are the final hands:")
        for current_hand in hand:
            show_hand(current_hand)
        show_hand(Dealer_Hand, 1)
    elif all_over_21 == False:
        if Player_Split_Aces == True or Player_Split_Hand == True:
            for current_hand in hand:
                dealer_logic(deck, current_hand)
        elif Player_Split_Aces != True and Player_Split_Hand != True:
            dealer_logic(deck, Player_Hand)
    else:
        pass

# Hit hand method
def hit_hand(deck, hand):
    card_drawn = deck.Draw()
    hand.append(card_drawn)
    for card in hand:
        if card.rank == "Ace":
            card.card_value = 1
    hand_total = add_card_total(hand)
    for card in hand:
        if card.rank == "Ace":
            if hand_total <= 11:
                card.card_value = 11
                break
    return [hand]

# Hit, Stay, Double Down method
def hit_stay_double_down(deck, hand):
    global Player_Total
    Player_Total = add_card_total(hand)
    has_hit = False
    response = ""
    while response not in ["h", "s", "d"] and value_check("<", Player_Total, 21):
        if not has_hit:
            time.sleep(1)
            print("\n" "Your current hand is:")
            time.sleep(1)
            show_hand(hand)
            response = input("\n" f"Would you like to hit, stay, or double down on your current hand?"
                             f" \033[1;32;40m(h/s/d)\033[0m: ")
            print("\n")
        elif has_hit:
            time.sleep(1)
            print("\n" "Your current hand is:")
            time.sleep(1)
            show_hand(hand)
            response = input("\n" f"Would you like to hit or stay? \033[1;32;40m(h/s)\033[0m: ")
            print("\n")
        if response.lower() == "h":
            has_hit = True
            hit_hand(deck, hand)
            Player_Total = add_card_total(hand)
            if value_check(">", Player_Total, 21):
                time.sleep(1)
                print(f"Player has busted with a final value of \033[1;31;40m{Player_Total}\033[0m."
                      f" Here is the player's final hand:")
                time.sleep(1)
                show_hand(hand)
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    show_hand(Dealer_Hand)
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    show_hand(Dealer_Hand, 1)
                else:
                    pass
                break
            elif value_check("<", Player_Total, 21):
                time.sleep(1)
                print(f"Player hits current hand.")
            elif value_check("==", Player_Total, 21):
                time.sleep(1)
                print(f"Player has \033[1;31;40m{Player_Total}\033[0m. No more cards will be accepted.")
                time.sleep(1)
                show_hand(hand)
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    show_hand(Dealer_Hand)
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    show_hand(Dealer_Hand, 1)
                else:
                    pass
            response = ""
        elif response.lower() == "s":
            Player_Total = add_card_total(hand)
            time.sleep(1)
            print(f"Player has chosen to stay with a final value of \033[1;31;40m{Player_Total}\033[0m."
                  f" Here is the final hand:")
            time.sleep(1)
            show_hand(hand)
            time.sleep(1)
            if Player_Split_Aces == True or Player_Split_Hand == True:
                show_hand(Dealer_Hand)
            elif Player_Split_Aces != True and Player_Split_Hand != True:
                show_hand(Dealer_Hand, 1)
            else:
                pass
        elif response.lower() == "d":
            hit_hand(deck, hand)
            Player_Total = add_card_total(hand)
            if value_check(">", Player_Total, 21):
                time.sleep(1)
                print(f"Player has doubled down and busted with a final value of \033[1;31;40m{Player_Total}\033[0m.")
                time.sleep(1)
                show_hand(hand)
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    show_hand(Dealer_Hand)
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    show_hand(Dealer_Hand, 1)
                else:
                    pass
            elif value_check("<=", Player_Total, 21):
                time.sleep(1)
                print(f"Player has doubled down and has a final value of \033[1;31;40m{Player_Total}\033[0m.")
                time.sleep(1)
                show_hand(hand)
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    show_hand(Dealer_Hand)
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    show_hand(Dealer_Hand, 1)
                else:
                    pass
            else:
                pass
        else:
            print("\033[1;31;40mInvalid choice\033[0m." "\n")
            continue
    return [hand]

# Play hand method
def play_hand(deck):
    # Import global variables to be modified
    global Player_Hand
    global Dealer_Hand
    global Dealer_Total
    global Player_Total
    global Player_Split_Aces
    global Player_Split_Hand
    # Deal hand and start processing logic
    deal_hand(deck)
    if Dealer_Hand[1].rank == "Ace":
        insurance_choice = ""
        while insurance_choice not in ["y", "n"]:
            insurance_choice = input("\n" f"The dealer is showing an \033[1;32;40m{Dealer_Hand[1].rank}\033[0m,"
                                     f" would you like to buy insurance? \033[1;32;40m(y/n)\033[0m: ")
            if insurance_choice.lower() == "y":
                time.sleep(1)
                print("\n" "The player has chosen to buy insurance. We will now check for if the dealer"
                      " has blackjack.")
                if check_for_blackjack(Dealer_Hand) and check_for_blackjack(Player_Hand):
                    time.sleep(1)
                    print("\n" "Both players have blackjack, it is a \033[1;31;40mpush\033[0m."
                          " \033[1;31;40mPlayer wins insurance\033[0m.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand, 1)
                    break
                elif check_for_blackjack(Dealer_Hand) and check_for_blackjack(Player_Hand) == False:
                    time.sleep(1)
                    print("\n" "The dealer has blackjack, \033[1;31;40mplayer wins insurance\033[0m"
                          " but loses the hand.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand, 1)
                    break
                elif check_for_blackjack(Dealer_Hand) == False and check_for_blackjack(Player_Hand):
                    time.sleep(1)
                    print("\n" "The player has blackjack, the dealer does not."
                          " \033[1;31;40mPlayer loses insurance\033[0m but wins the hand.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand, 1)
                    break
                elif check_for_blackjack(Dealer_Hand) == False and check_for_blackjack(Player_Hand) == False:
                    time.sleep(1)
                    print("\n" "Neither player has blackjack, \033[1;31;40mplayer loses insurance\033[0m."
                          " The hand will continue.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand)
                    player_hand_logic(deck)
            elif insurance_choice.lower() == "n":
                time.sleep(1)
                print("\n" "The player has chosen to not buy insurance. We will now check for if the dealer"
                      " has blackjack.")
                if check_for_blackjack(Dealer_Hand) and check_for_blackjack(Player_Hand):
                    time.sleep(1)
                    print("\n" "Both players have blackjack, it is a \033[1;31;40mpush\033[0m.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand, 1)
                    break
                elif check_for_blackjack(Dealer_Hand) and check_for_blackjack(Player_Hand) == False:
                    time.sleep(1)
                    print("\n" "The dealer has blackjack, \033[1;31;40mplayer loses\033[0m.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand, 1)
                    break
                elif check_for_blackjack(Dealer_Hand) == False and check_for_blackjack(Player_Hand):
                    time.sleep(1)
                    print("\n" "The player has blackjack, the dealer does not,"
                          " \033[1;31;40mplayer wins\033[0m.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand, 1)
                    break
                elif check_for_blackjack(Dealer_Hand) == False and check_for_blackjack(Player_Hand) == False:
                    time.sleep(1)
                    print("\n" "Neither player has blackjack. The hand will continue.")
                    time.sleep(1)
                    show_hand(Player_Hand)
                    time.sleep(1)
                    show_hand(Dealer_Hand)
                    player_hand_logic(deck)
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m" "\n")
                continue
    if Dealer_Hand[1].rank != "Ace":
        if check_for_blackjack(Dealer_Hand) and check_for_blackjack(Player_Hand):
            time.sleep(1)
            print("\n" "Both players have blackjack, it is a \033[1;31;40mpush\033[0m.")
            time.sleep(1)
            show_hand(Player_Hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        elif check_for_blackjack(Dealer_Hand) and check_for_blackjack(Player_Hand) == False:
            time.sleep(1)
            print("\n" "The dealer has blackjack, \033[1;31;40mplayer loses\033[0m.")
            time.sleep(1)
            show_hand(Player_Hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        elif check_for_blackjack(Dealer_Hand) == False and check_for_blackjack(Player_Hand):
            time.sleep(1)
            print("\n" "The player has blackjack, the dealer does not,"
                  " \033[1;31;40mplayer wins\033[0m.")
            time.sleep(1)
            show_hand(Player_Hand)
            time.sleep(1)
            show_hand(Dealer_Hand, 1)
        elif check_for_blackjack(Dealer_Hand) == False and check_for_blackjack(Player_Hand) == False:
            player_hand_logic(deck)
    # Reset global variables
    Player_Hand.clear()
    Dealer_Hand.clear()
    Player_Split_Aces = None
    Player_Split_Hand = None
    Dealer_Total = 0
    Player_Total = 0
    time.sleep(2)
    return [Player_Hand, Dealer_Hand, Player_Split_Aces, Player_Split_Hand, Dealer_Total, Player_Total]

# Player logic method
def player_hand_logic(deck):
    global Player_Hand
    Player_Hand = player_same_rank_check(deck)[0]
    if Player_Split_Aces == True:
        print("\n" "Here are the final hands of the player:")
        for current_hand in Player_Hand:
            time.sleep(1)
            show_hand(current_hand)
        dealer_play(deck, Player_Hand)
    elif Player_Split_Hand == True:
        print("Here are the current hands of the player:")
        for current_hand in Player_Hand:
            time.sleep(1)
            show_hand(current_hand)
        hand_counter = 1
        for current_hand in Player_Hand:
            if hand_counter > 1:
                hit_hand(deck, current_hand)
            else:
                pass
            hit_stay_double_down(deck, current_hand)
            hand_counter += 1
        print("\n" "The final hands of the player are:")
        for current_hand in Player_Hand:
            time.sleep(1)
            show_hand(current_hand)
        dealer_play(deck, Player_Hand)
    elif Player_Split_Aces != True and Player_Split_Hand != True:
        hit_stay_double_down(deck, Player_Hand)
        dealer_play(deck, Player_Hand)
    else:
        pass

# Player same rank check method
def player_same_rank_check(deck):
    global Player_Split_Aces
    global Player_Split_Hand
    if check_same_rank_in_hand(Player_Hand, "Ace"):
        time.sleep(1)
        aces_response = ""
        while aces_response not in ["y", "n"]:
            aces_response = input("\n" f"You have two \033[1;32;40m{Player_Hand[0].rank}\033[0m's in your hand."
                                  f" Would you like to split your hand? You may only split your hand once."
                                  f" \033[1;32;40m(y/n)\033[0m: ")
            if aces_response.lower() == "y":
                time.sleep(1)
                print("\n" f"You have chosen to split your \033[1;32;40m{Player_Hand[0].rank}\033[0m's." "\n")
                hand_1 = split_hand(Player_Hand)[0][1]
                hand_2 = split_hand(Player_Hand)[0][0]
                hit_hand(deck, hand_1)
                hit_hand(deck, hand_2)
                if check_same_rank_in_hand(hand_1, "Ace"):
                    hand_1[0].card_value = 11
                    hand_1[1].card_value = 1
                else:
                    for card in hand_1:
                        if check_rank_of_card(card, "Ace"):
                            card.card_value = 1
                        else:
                            pass
                if check_same_rank_in_hand(hand_2, "Ace"):
                    hand_2[0].card_value = 11
                    hand_2[1].card_value = 1
                else:
                    for card in hand_2:
                        if check_rank_of_card(card, "Ace"):
                            card.card_value = 11
                        else:
                            pass
                Player_Split_Aces = True
                new_hand = [hand_1, hand_2]
                break
            elif aces_response.lower() == "n":
                time.sleep(1)
                print("\n" f"You have chosen not to split your \033[1;32;40m{Player_Hand[0].rank}\033[0m's." "\n")
                Player_Split_Aces = False
                new_hand = Player_Hand
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    elif check_same_rank_in_hand(Player_Hand) and check_same_rank_in_hand(Player_Hand, "Ace") == False:
        time.sleep(1)
        same_rank_response = ""
        while same_rank_response not in ["y", "n"]:
            same_rank_response = input("\n" f"You have the same rank of \033[1;32;40m{Player_Hand[0].rank}\033[0m"
                                       f" in your hand. Would you like to split your hand? "
                                       f" \033[1;32;40m(y/n)\033[0m: ")
            if same_rank_response.lower() == "y":
                time.sleep(1)
                print("\n" f"You have chosen to split your \033[1;32;40m{Player_Hand[0].rank}\033[0m's." "\n")
                hand_1 = split_hand(Player_Hand)[0][1]
                hand_2 = split_hand(Player_Hand)[0][0]
                hit_hand(deck, hand_1)
                Player_Split_Hand = True
                split_hands = []
                checking_hand = hand_1
                if check_same_rank_in_hand(checking_hand):
                    time.sleep(1)
                    print(f"You have pulled the same rank of \033[1;32;40m{checking_hand[1].rank}\033[0m again."
                          f" Here are your current hands:")
                    time.sleep(1)
                    show_hand(checking_hand)
                    time.sleep(1)
                    show_hand(hand_2)
                    split_counter = 1
                    while value_check("<=", split_counter, 3) and check_same_rank_in_hand(checking_hand):
                        split_again_choice = ""
                        while split_again_choice not in ["y", "n"]:
                            split_again_choice = input("\n" f"Would you like to split your"
                                                       f" \033[1;32;40m{checking_hand[1].rank}\033[0m's again?"
                                                       f" \033[1;32;40m(y/n)\033[0m: ")
                            if split_again_choice.lower() == "y":
                                split_counter += 1
                                print("\n" f"You have chosen to split your hand again."
                                      f" Total times split: \033[1;31;40m{split_counter}\033[0m")
                                new_hand_1 = split_hand(checking_hand)[0][1]
                                new_hand_2 = split_hand(checking_hand)[0][0]
                                split_hands.insert(0, new_hand_2)
                                hit_hand(deck, new_hand_1)
                                checking_hand = new_hand_1
                                break
                            elif split_again_choice.lower() == "n":
                                break
                            else:
                                print("\n" "\033[1;31;40mInvalid choice\033[0m.")
                                continue
                        if check_same_rank_in_hand(checking_hand) and split_again_choice.lower() == "y":
                            if value_check("<", split_counter, 4):
                                print("\n" "Your current hands are:")
                                split_hands.insert(0, checking_hand)
                                split_hands.append(hand_2)
                                for current_hand in split_hands:
                                    time.sleep(1)
                                    show_hand(current_hand)
                                split_hands.remove(checking_hand)
                                split_hands.remove(hand_2)
                            elif value_check("==", split_counter, 4):
                                print("\n" f"You can no longer split your hands. Times split: "
                                      f" \033[1;31;40m{split_counter}\033[0m" "\n")
                                split_hands.insert(0, checking_hand)
                            else:
                                pass
                            continue
                        elif check_same_rank_in_hand(checking_hand) == False or split_again_choice.lower() == "n":
                            if check_same_rank_in_hand(checking_hand) == False:
                                print("\n" f"You did not pull the same rank of"
                                      f" \033[1;32;40m{checking_hand[0].rank}\033[0m again. Total times split:"
                                      f" \033[1;31;40m{split_counter}\033[0m" "\n")
                            elif split_again_choice.lower() == "n":
                                print("\n" f"You have chosen to not split your hand again."
                                      f" Total times split: \033[1;31;40m{split_counter}\033[0m" "\n")
                            else:
                                pass
                            split_hands.insert(0, checking_hand)
                            break
                        else:
                            raise ValueError("\033[1;31;40mA catastrophic error has occurred.\033[0m")
                            break
                    split_hands.append(hand_2)
                elif check_same_rank_in_hand(checking_hand) == False:
                    split_hands.insert(0, hand_1)
                    split_hands.append(hand_2)
                else:
                    pass
                new_hand = split_hands
                break
            elif same_rank_response.lower() == "n":
                time.sleep(1)
                print("\n" f"You have chosen not to split your \033[1;32;40m{Player_Hand[0].rank}\033[0m's." "\n")
                Player_Split_Hand = False
                new_hand = Player_Hand
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    else:
        new_hand = Player_Hand
    return [new_hand, Player_Split_Aces, Player_Split_Hand]

# Show hand method
def show_hand(hand, dealer_display = None):
    if hand != Dealer_Hand:
        if isinstance(hand, list) and isinstance(hand[0], list):
            hand_counter = 1
            hand_number_place_holder = ""
            for current_hand in hand:
                if hand_counter == 1:
                    hand_number_place_holder = "first"
                elif hand_counter == 2:
                    hand_number_place_holder = "second"
                elif hand_counter == 3:
                    hand_number_place_holder = "third"
                elif hand_counter == 4:
                    hand_number_place_holder = "fourth"
                elif hand_counter == 5:
                    hand_number_place_holder = "fifth"
                else:
                    pass
                print(f"{Players[0]}'s {hand_number_place_holder} hand is: {current_hand}"
                      f" Current total: \033[1;31;40m{add_card_total(current_hand)}\033[0m")
                hand_counter += 1
        elif isinstance(hand, list) and isinstance(hand[0], Card):
            print(f"{Players[0]}'s hand is: {hand} Current total:"
                  f" \033[1;31;40m{add_card_total(hand)}\033[0m")
    elif hand == Dealer_Hand and dealer_display is None:
        print(f"{Players[-1]}'s hand is: [Hidden, {hand[1]}]"
              f" Current total: \033[1;31;40m{hand[1].card_value}\033[0m")
    elif hand == Dealer_Hand and dealer_display is not None:
        print(f"{Players[-1]}'s hand is: {hand}"
              f" Current total: \033[1;31;40m{add_card_total(hand)}\033[0m")
    else:
        raise ValueError("\033[1;31;40mInvalid hand.\033[0m")

# Split hand method
def split_hand(hand):
    hands = []
    current_hand = []
    for card in hand:
        current_hand.append(card)
        if card.rank == hand[0].rank:
            hands.append(current_hand)
            current_hand = []
        else:
            pass
    if current_hand:
        hands.append(current_hand)
    return [hands]

# Value check method
def value_check(operator, fed_value, checking_value):
    result = None
    if operator == "==":
        if fed_value == checking_value:
            result = True
        else:
            result = False
    elif operator == "<=":
        if fed_value <= checking_value:
            result = True
        else:
            result = False
    elif operator == ">=":
        if fed_value >= checking_value:
            result = True
        else:
            result = False
    elif operator == ">":
        if fed_value > checking_value:
            result = True
        else:
            result = False
    elif operator == "<":
        if fed_value < checking_value:
            result = True
        else:
            result = False
    else:
        raise ValueError("\033[1;31;40mInvalid operator.\033[0m")
        pass
    return result