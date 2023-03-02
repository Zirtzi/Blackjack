# ----- ----- ----- ----- ----- ----- ----- ----- ----- Imports ----- ----- ----- ----- ----- ----- ----- ----- ----- #
import random, time

# ----- ----- ----- ----- ----- ----- ----- ----- ----- Arrays ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Creating suits and ranks for cards
Suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# ----- ----- ----- ----- ----- ----- ----- ----- Variables / Booleans ----- ----- ----- ----- ----- ----- ----- ----- #
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
        self.returned_cards = []
        self.rigged_cards = []

    # Draw method
    def Draw(self):
        if len(self.rigged_cards) == 0:
            return self.cards.pop()
        elif len(self.rigged_cards) > 0:
            return self.rigged_cards.pop()
        else:
            pass

    # Deal random cards method
    def Deal_Cards(self):
        print("\n" "Here are the cards from a shuffled deck:")
        card_dealt_number = 1
        self.returned_cards = []
        rigged_deck = False
        if len(self.rigged_cards) > 0:
            rigged_deck = True
        else:
            pass
        if rigged_deck == False:
            for i in range(len(self.cards)):
                card_drawn = self.Draw()
                self.returned_cards.append(card_drawn)
                print(f"Card dealt number: {card_dealt_number} - {card_drawn}")
                card_dealt_number += 1
            self.cards = self.returned_cards
            self.cards.reverse()
            print(len(self.cards), " Cards remaining from shuffled deck" "\n")
        elif rigged_deck:
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

# Player Hand class
class Player_Hand:
    # Constructor
    def __init__(self, name=None):
        self.cards = []
        self.name = name
        self.hand_value = 0

    # Add card to hand
    def Add_Card_To_Hand(self, card):
        self.cards.append(card)
        ace_count = sum(card.rank == "Ace" for card in self.cards)
        for current_card in self.cards:
            if value_check("==", ace_count, 1):
                if check_rank_of_card(current_card, "Ace"):
                    current_card.card_value = 11
                else:
                    pass
            elif value_check(">", ace_count, 1):
                if check_rank_of_card(current_card, "Ace"):
                    current_card.card_value = 1
                else:
                    pass
            else:
                pass
            ace_count -= 1
        self.hand_value = sum(card.Value_of_Card() for card in self.cards)
        for current_card in self.cards:
            if value_check(">", self.hand_value, 21):
                if check_rank_of_card(current_card, "Ace"):
                    current_card.card_value = 1
                else:
                    pass
            else:
                pass
        self.hand_value = sum(card.Value_of_Card() for card in self.cards)
        return int(self.hand_value)

    def Hit_Hand(self, deck):
        card_drawn = deck.Draw()
        self.Add_Card_To_Hand(card_drawn)
        return Player_Hand

    # Show hand method
    def Show_Hand(self):
         print(f"{self.name}'s current hand: [{' , '.join(str(card) for card in self.cards)}]"
               f" Hand Total: \033[1;31;40m{self.hand_value}\033[0m")

# Dealer Hand Class
class Dealer_Hand:
    # Constructor
    def __init__(self):
        self.cards = []
        self.hand_value = 0

    # Add card to hand method
    def Add_Card_To_Hand(self, card):
        self.cards.append(card)
        ace_count = sum(card.rank == "Ace" for card in self.cards)
        for current_card in self.cards:
            if value_check("==", ace_count, 1):
                if check_rank_of_card(current_card, "Ace"):
                    current_card.card_value = 11
                else:
                    pass
            elif value_check(">", ace_count, 1):
                if check_rank_of_card(current_card, "Ace"):
                    current_card.card_value = 1
                else:
                    pass
            else:
                pass
            ace_count -= 1
        self.hand_value = sum(card.Value_of_Card() for card in self.cards)
        for current_card in self.cards:
            if value_check(">", self.hand_value, 21):
                if check_rank_of_card(current_card, "Ace"):
                    current_card.card_value = 1
                else:
                    pass
            else:
                pass
        self.hand_value = sum(card.Value_of_Card() for card in self.cards)
        return int(self.hand_value), self.cards

    def Hit_Hand(self, deck):
        card_drawn = deck.Draw()
        self.Add_Card_To_Hand(card_drawn)
        return Dealer_Hand

    def Show_Hand(self, display = None):
        if display is None:
            print(f"Dealer's current hand: [Hidden, {self.cards[1]}]"
                  f" Hand Total: \033[1;31;40m{self.cards[1].card_value}\033[0m" )
        elif display is not None:
            print(f"Dealer's current hand: [{' , '.join(str(card) for card in self.cards)}]"
                  f" Hand Total: \033[1;31;40m{self.hand_value}\033[0m")

# ----- ----- ----- ----- ----- ----- ----- Game Methods ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #
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
def deal_hand(deck, dealer_hand, player_hand):
    for turn in range(4):
        if (turn % 2) == 0:
            player_hand.Hit_Hand(deck)
        elif (turn % 2) == 1:
            dealer_hand.Hit_Hand(deck)
    print("\n")
    player_hand.Show_Hand()
    dealer_hand.Show_Hand()
    return player_hand, dealer_hand

# Dealer logic method
def dealer_logic(deck, dealer_hand, player_hand):
    Dealer_Total = dealer_hand.hand_value
    Player_Total = player_hand.hand_value
    if value_check("<=", Player_Total, 21):
        while value_check("<", Dealer_Total, 17):
            dealer_hand.Hit_Hand(deck)
            Dealer_Total = dealer_hand.hand_value
            time.sleep(1)
            print(f"Dealer hits, current hand: {dealer_hand.cards} with a current total"
                  f" of \033[1;31;40m{Dealer_Total}\033[0m")
    elif value_check(">", Player_Total, 21):
        time.sleep(1)
        print("\n" f"Player has busted with a final value of \033[1;31;40m{Player_Total}\033[0m."
              f" \033[1;31;40mPlayer loses\033[0m.")
        time.sleep(1)
        player_hand.Show_Hand()
        time.sleep(1)
        dealer_hand.Show_Hand(1)
    else:
        pass
    print("\n")
    if value_check("<=", Player_Total, 21):
        if value_check("==", Dealer_Total, Player_Total):
            time.sleep(1)
            print(f"Both players have the same final value of \033[1;31;40m{Player_Total}\033[0m."
                  f" It is \033[1;31;40ma push\033[0m. Here are the final hands:")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        elif value_check(">", Dealer_Total, Player_Total) and value_check("<=", Dealer_Total, 21):
            time.sleep(1)
            print(f"Dealer has a greater final value of \033[1;31;40m{Dealer_Total}\033[0m."
                  f" \033[1;31;40mPlayer loses\033[0m. Here are the final hands:")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        elif value_check("<", Dealer_Total, Player_Total):
            time.sleep(1)
            print(f"Player has a greater final value of \033[1;31;40m{Player_Total}\033[0m."
                  f" \033[1;31;40mPlayer wins\033[0m. Here are the final hands:")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        elif value_check(">", Dealer_Total, 21):
            time.sleep(1)
            print(f"Dealer has busted with a final value of \033[1;31;40m{Dealer_Total}\033[0m."
                  f" \033[1;31;40mPlayer wins\033[0m. Here are the final hands:")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        else:
            pass

# Dealer play method
def dealer_play(deck , dealer_hand, player_hand):
    Dealer_Total = dealer_hand.hand_value
    player_totals = []
    all_over_21 = True
    if isinstance(player_hand, Player_Hand):
        player_totals.append(player_hand.hand_value)
    elif isinstance(player_hand, list):
        for current_hand in player_hand:
            player_totals.append(current_hand.hand_value)
    else:
        raise ValueError(f"This is an incorrect data type: ", type(player_hand))
    for current_total in player_totals:
        if value_check("<=", current_total, 21):
            all_over_21 = False
            break
    if value_check("<", Dealer_Total, 17):
        print("\n" "The dealer will now play their hand.")
        dealer_hand.Show_Hand(1)
    elif value_check(">=", Dealer_Total, 17) and value_check("<=", Dealer_Total, 21):
        print("\n" "The dealer does not need to play their hand with a final value of"
              f" \033[1;31;40m{Dealer_Total}\033[0m.")
        dealer_hand.Show_Hand(1)
    elif value_check(">", Dealer_Total, 21):
        print("\n" f"The dealer has busted with a final value of \033[1;31;40m{Dealer_Total}\033[0m.")
    else:
        pass
    if all_over_21:
        print("\n" "The player has busted on all hands therefore the dealer has won both hands."
              " Here are the final hands:")
        if isinstance(player_hand, list):
            for current_hand in player_hand:
                current_hand.Show_Hand()
        elif isinstance(player_hand, Player_Hand):
            player_hand.Show_Hand()
        else:
            pass
        dealer_hand.Show_Hand(1)
    elif all_over_21 == False:
        if Player_Split_Aces == True or Player_Split_Hand == True:
            for current_hand in player_hand:
                dealer_logic(deck, dealer_hand, current_hand)
        elif Player_Split_Aces != True and Player_Split_Hand != True:
            dealer_logic(deck, dealer_hand, player_hand)
    else:
        pass

# Hit, Stay, Double Down method
def hit_stay_double_down(deck, dealer_hand, player_hand):
    Player_Total = player_hand.hand_value
    has_hit = False
    response = ""
    while response not in ["h", "s", "d"] and value_check("<", Player_Total, 21):
        if not has_hit:
            time.sleep(1)
            print("\n" "Your current hand is:")
            time.sleep(1)
            player_hand.Show_Hand()
            response = input("\n" f"Would you like to hit, stay, or double down on your current hand?"
                             f" \033[1;32;40m(h/s/d)\033[0m: ")
            print("\n")
        elif has_hit:
            time.sleep(1)
            print("\n" "Your current hand is:")
            time.sleep(1)
            player_hand.Show_Hand()
            response = input("\n" f"Would you like to hit or stay? \033[1;32;40m(h/s)\033[0m: ")
            print("\n")
        if response.lower() == "h":
            has_hit = True
            player_hand.Hit_Hand(deck)
            Player_Total = player_hand.hand_value
            if value_check(">", Player_Total, 21):
                time.sleep(1)
                print(f"Player has busted with a final value of \033[1;31;40m{Player_Total}\033[0m."
                      f" Here is the player's final hand:")
                time.sleep(1)
                player_hand.Show_Hand()
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    dealer_hand.Show_Hand()
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    dealer_hand.Show_Hand(1)
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
                player_hand.Show_Hand()
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    dealer_hand.Show_Hand()
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    dealer_hand.Show_Hand(1)
                else:
                    pass
            response = ""
        elif response.lower() == "s":
            Player_Total = player_hand.hand_value
            time.sleep(1)
            print(f"Player has chosen to stay with a final value of \033[1;31;40m{Player_Total}\033[0m."
                  f" Here is the final hand:")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            if Player_Split_Aces == True or Player_Split_Hand == True:
                dealer_hand.Show_Hand()
            elif Player_Split_Aces != True and Player_Split_Hand != True:
                dealer_hand.Show_Hand(1)
            else:
                pass
        elif response.lower() == "d":
            player_hand.Hit_Hand(deck)
            Player_Total = player_hand.hand_value
            if value_check(">", Player_Total, 21):
                time.sleep(1)
                print(f"Player has doubled down and busted with a final value of \033[1;31;40m{Player_Total}\033[0m.")
                time.sleep(1)
                player_hand.Show_Hand()
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    dealer_hand.Show_Hand()
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    dealer_hand.Show_Hand(1)
                else:
                    pass
            elif value_check("<=", Player_Total, 21):
                time.sleep(1)
                print(f"Player has doubled down and has a final value of \033[1;31;40m{Player_Total}\033[0m.")
                time.sleep(1)
                player_hand.Show_Hand()
                time.sleep(1)
                if Player_Split_Aces == True or Player_Split_Hand == True:
                    dealer_hand.Show_Hand()
                elif Player_Split_Aces != True and Player_Split_Hand != True:
                    dealer_hand.Show_Hand(1)
                else:
                    pass
            else:
                pass
        else:
            print("\033[1;31;40mInvalid choice\033[0m." "\n")
            continue
    return player_hand

# Play hand method
def play_hand(deck, dealer_hand, player_hand):
    # Import global variables to be modified
    global Player_Split_Aces
    global Player_Split_Hand
    # Deal hand and start processing logic
    deal_hand(deck, dealer_hand, player_hand)
    if dealer_hand.cards[1].rank == "Ace":
        insurance_choice = ""
        while insurance_choice not in ["y", "n"]:
            insurance_choice = input("\n" f"The dealer is showing an \033[1;32;40m{dealer_hand.cards[1].rank}\033[0m,"
                                     f" would you like to buy insurance? \033[1;32;40m(y/n)\033[0m: ")
            if insurance_choice.lower() == "y":
                time.sleep(1)
                print("\n" "The player has chosen to buy insurance. We will now check for if the dealer"
                      " has blackjack.")
                if check_for_blackjack(dealer_hand.cards) and check_for_blackjack(player_hand.cards):
                    time.sleep(1)
                    print("\n" "Both players have blackjack, it is a \033[1;31;40mpush\033[0m."
                          " \033[1;31;40mPlayer wins insurance\033[0m.")
                    time.sleep(1)
                    player_hand.Show_Hand()
                    time.sleep(1)
                    dealer_hand.Show_Hand(1)
                    break
                elif check_for_blackjack(dealer_hand.cards) and check_for_blackjack(player_hand.cards) == False:
                    time.sleep(1)
                    print("\n" "The dealer has blackjack, \033[1;31;40mplayer wins insurance\033[0m"
                          " but loses the hand.")
                    time.sleep(1)
                    player_hand.Show_Hand()
                    time.sleep(1)
                    dealer_hand.Show_Hand(1)
                    break
                elif check_for_blackjack(dealer_hand.cards) == False and check_for_blackjack(player_hand.cards):
                    time.sleep(1)
                    print("\n" "The player has blackjack, the dealer does not."
                          " \033[1;31;40mPlayer loses insurance\033[0m but wins the hand.")
                    time.sleep(1)
                    player_hand.Show_Hand()
                    time.sleep(1)
                    dealer_hand.Show_Hand(1)
                    break
                elif check_for_blackjack(dealer_hand.cards) == False and check_for_blackjack(player_hand.cards) == False:
                    time.sleep(1)
                    print("\n" "Neither player has blackjack, \033[1;31;40mplayer loses insurance\033[0m."
                          " The hand will continue.")
                    player_hand_logic(deck, dealer_hand, player_hand)
            elif insurance_choice.lower() == "n":
                time.sleep(1)
                print("\n" "The player has chosen to not buy insurance. We will now check for if the dealer"
                      " has blackjack.")
                if check_for_blackjack(dealer_hand.cards) and check_for_blackjack(player_hand.cards):
                    time.sleep(1)
                    print("\n" "Both players have blackjack, it is a \033[1;31;40mpush\033[0m.")
                    time.sleep(1)
                    player_hand.Show_Hand()
                    time.sleep(1)
                    dealer_hand.Show_Hand(1)
                    break
                elif check_for_blackjack(dealer_hand.cards) and check_for_blackjack(player_hand.cards) == False:
                    time.sleep(1)
                    print("\n" "The dealer has blackjack, \033[1;31;40mplayer loses\033[0m.")
                    time.sleep(1)
                    player_hand.Show_Hand()
                    time.sleep(1)
                    dealer_hand.Show_Hand(1)
                    break
                elif check_for_blackjack(dealer_hand.cards) == False and check_for_blackjack(player_hand.cards):
                    time.sleep(1)
                    print("\n" "The player has blackjack, the dealer does not,"
                          " \033[1;31;40mplayer wins\033[0m.")
                    time.sleep(1)
                    player_hand.Show_Hand()
                    time.sleep(1)
                    dealer_hand.Show_Hand(1)
                    break
                elif check_for_blackjack(dealer_hand.cards) == False and check_for_blackjack(player_hand.cards) == False:
                    time.sleep(1)
                    print("\n" "Neither player has blackjack. The hand will continue.")
                    player_hand_logic(deck, dealer_hand, player_hand)
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m" "\n")
                continue
    if dealer_hand.cards[1].rank != "Ace":
        if check_for_blackjack(dealer_hand.cards) and check_for_blackjack(player_hand.cards):
            time.sleep(1)
            print("\n" "Both players have blackjack, it is a \033[1;31;40mpush\033[0m.")
            time.sleep(1)
            player_hand.Show_Hand
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        elif check_for_blackjack(dealer_hand.cards) and check_for_blackjack(player_hand.cards) == False:
            time.sleep(1)
            print("\n" "The dealer has blackjack, \033[1;31;40mplayer loses\033[0m.")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        elif check_for_blackjack(dealer_hand.cards) == False and check_for_blackjack(player_hand.cards):
            time.sleep(1)
            print("\n" "The player has blackjack, the dealer does not,"
                  " \033[1;31;40mplayer wins\033[0m.")
            time.sleep(1)
            player_hand.Show_Hand()
            time.sleep(1)
            dealer_hand.Show_Hand(1)
        elif check_for_blackjack(dealer_hand.cards) == False and check_for_blackjack(player_hand.cards) == False:
            player_hand_logic(deck, dealer_hand, player_hand)
    # Reset global variables
    if isinstance(player_hand, list):
        for current_hand in player_hand:
            current_hand.cards.clear()
            current_hand.hand_value = 0
    elif isinstance(player_hand, Player_Hand):
        player_hand.cards.clear()
        player_hand.hand_value = 0
    else:
        pass
    dealer_hand.cards.clear()
    dealer_hand.hand_value = 0
    Player_Split_Aces = None
    Player_Split_Hand = None
    if len(deck.cards) >= 13:
        print("\n" "Dealing new hand." "\n")
    else:
        print("\n")
    time.sleep(2)
    return [player_hand, dealer_hand, Player_Split_Aces, Player_Split_Hand]

# Player logic method
def player_hand_logic(deck, dealer_hand, player_hand):
    hands_of_player = player_same_rank_check(deck, player_hand)[0]
    if Player_Split_Aces == True:
        print("\n" "Here are the final hands of the player:")
        for current_hand in hands_of_player:
            time.sleep(1)
            current_hand.Show_Hand()
        dealer_play(deck, dealer_hand, hands_of_player)
    elif Player_Split_Hand == True:
        print("Here are the current hands of the player:")
        for current_hand in hands_of_player:
            time.sleep(1)
            current_hand.Show_Hand()
        hand_counter = 1
        for current_hand in hands_of_player:
            if hand_counter > 1:
                current_hand.Hit_Hand(deck)
            else:
                pass
            hit_stay_double_down(deck, dealer_hand, current_hand)
            hand_counter += 1
        print("\n" "The final hands of the player are:")
        for current_hand in hands_of_player:
            time.sleep(1)
            current_hand.Show_Hand()
        dealer_play(deck, dealer_hand, hands_of_player)
    elif Player_Split_Aces != True and Player_Split_Hand != True:
        hit_stay_double_down(deck, dealer_hand, hands_of_player)
        dealer_play(deck, dealer_hand, hands_of_player)
    else:
        pass

# Player same rank check method
def player_same_rank_check(deck, player_hand):
    global Player_Split_Aces
    global Player_Split_Hand
    if check_same_rank_in_hand(player_hand.cards, "Ace"):
        time.sleep(1)
        aces_response = ""
        while aces_response not in ["y", "n"]:
            aces_response = input("\n" f"You have two \033[1;32;40m{player_hand.cards[0].rank}\033[0m's in your hand."
                                  f" Would you like to split your hand? You may only split your hand once."
                                  f" \033[1;32;40m(y/n)\033[0m: ")
            if aces_response.lower() == "y":
                time.sleep(1)
                print("\n" f"You have chosen to split your \033[1;32;40m{player_hand.cards[0].rank}\033[0m's." "\n")
                player_hand_1 = Player_Hand(player_hand.name)
                player_hand_2 = Player_Hand(player_hand.name)
                player_hand_1.Add_Card_To_Hand(split_hand(player_hand)[1][0])
                player_hand_2.Add_Card_To_Hand(split_hand(player_hand)[0][0])
                player_hand_1.Hit_Hand(deck)
                player_hand_2.Hit_Hand(deck)
                Player_Split_Aces = True
                split_hands = [player_hand_1, player_hand_2]
                if check_same_rank_in_hand(player_hand_1.cards, "Ace"):
                    player_hand_1.cards[0].card_value = 11
                    player_hand_1.cards[1].card_value = 1
                else:
                    pass
                if check_same_rank_in_hand(player_hand_2.cards, "Ace"):
                    player_hand_2.cards[0].card_value = 11
                    player_hand_2.cards[1].card_value = 1
                else:
                    pass
                new_hand = split_hands
                break
            elif aces_response.lower() == "n":
                time.sleep(1)
                print("\n" f"You have chosen not to split your \033[1;32;40m{player_hand.cards[0].rank}\033[0m's." "\n")
                Player_Split_Aces = False
                new_hand = player_hand
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    elif check_same_rank_in_hand(player_hand.cards) and check_same_rank_in_hand(player_hand.cards, "Ace") == False:
        time.sleep(1)
        same_rank_response = ""
        while same_rank_response not in ["y", "n"]:
            same_rank_response = input("\n" f"You have the same rank of \033[1;32;40m{player_hand.cards[0].rank}\033[0m"
                                       f" in your hand. Would you like to split your hand? "
                                       f" \033[1;32;40m(y/n)\033[0m: ")
            if same_rank_response.lower() == "y":
                time.sleep(1)
                print("\n" f"You have chosen to split your \033[1;32;40m{player_hand.cards[0].rank}\033[0m's." "\n")
                player_hand_1 = Player_Hand(player_hand.name)
                player_hand_2 = Player_Hand(player_hand.name)
                player_hand_1.Add_Card_To_Hand(split_hand(player_hand)[1][0])
                player_hand_2.Add_Card_To_Hand(split_hand(player_hand)[0][0])
                player_hand_1.Hit_Hand(deck)
                Player_Split_Hand = True
                split_hands = []
                checking_hand = player_hand_1
                if check_same_rank_in_hand(checking_hand.cards):
                    time.sleep(1)
                    print(f"You have pulled the same rank of \033[1;32;40m{checking_hand.cards[1].rank}\033[0m again."
                          f" Here are your current hands:")
                    time.sleep(1)
                    checking_hand.Show_Hand()
                    time.sleep(1)
                    player_hand_2.Show_Hand()
                    split_counter = 1
                    while value_check("<=", split_counter, 3) and check_same_rank_in_hand(checking_hand.cards):
                        split_again_choice = ""
                        while split_again_choice not in ["y", "n"]:
                            split_again_choice = input("\n" f"Would you like to split your"
                                                       f" \033[1;32;40m{checking_hand.cards[1].rank}\033[0m's again?"
                                                       f" \033[1;32;40m(y/n)\033[0m: ")
                            if split_again_choice.lower() == "y":
                                split_counter += 1
                                print("\n" f"You have chosen to split your hand again."
                                      f" Total times split: \033[1;31;40m{split_counter}\033[0m")
                                new_player_hand_1 = Player_Hand(player_hand.name)
                                new_player_hand_2 = Player_Hand(player_hand.name)
                                new_player_hand_1.Add_Card_To_Hand(split_hand(checking_hand)[1][0])
                                new_player_hand_2.Add_Card_To_Hand(split_hand(checking_hand)[0][0])
                                split_hands.insert(0, new_player_hand_2)
                                new_player_hand_1.Hit_Hand(deck)
                                checking_hand = new_player_hand_1
                                break
                            elif split_again_choice.lower() == "n":
                                break
                            else:
                                print("\n" "\033[1;31;40mInvalid choice\033[0m.")
                                continue
                        if check_same_rank_in_hand(checking_hand.cards) and split_again_choice.lower() == "y":
                            if value_check("<", split_counter, 4):
                                print("\n" "Your current hands are:")
                                split_hands.insert(0, checking_hand)
                                split_hands.append(player_hand_2)
                                for current_hand in split_hands:
                                    time.sleep(1)
                                    current_hand.Show_Hand()
                                split_hands.remove(checking_hand)
                                split_hands.remove(player_hand_2)
                            elif value_check("==", split_counter, 4):
                                print("\n" f"You can no longer split your hands. Times split: "
                                      f" \033[1;31;40m{split_counter}\033[0m" "\n")
                                split_hands.insert(0, checking_hand)
                            else:
                                pass
                            continue
                        elif check_same_rank_in_hand(checking_hand.cards) == False or split_again_choice.lower() == "n":
                            if check_same_rank_in_hand(checking_hand.cards) == False:
                                print("\n" f"You did not pull the same rank of"
                                      f" \033[1;32;40m{checking_hand.cards[0].rank}\033[0m again. Total times split:"
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
                    split_hands.append(player_hand_2)
                elif check_same_rank_in_hand(checking_hand.cards) == False:
                    split_hands.insert(0, player_hand_1)
                    split_hands.append(player_hand_2)
                else:
                    pass
                new_hand = split_hands
                break
            elif same_rank_response.lower() == "n":
                time.sleep(1)
                print("\n" f"You have chosen not to split your \033[1;32;40m{player_hand.cards[0].rank}\033[0m's." "\n")
                Player_Split_Hand = False
                new_hand = player_hand
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    else:
        new_hand = player_hand
    return [new_hand, Player_Split_Aces, Player_Split_Hand]

# Split hand method
def split_hand(Hand):
    hands = []
    current_hand = []
    for card in Hand.cards:
        current_hand.append(card)
        if card.rank == Hand.cards[0].rank:
            hands.append(current_hand)
            current_hand = []
        else:
            pass
    if current_hand:
        hands.append(current_hand)
    return hands

# Value check method
def value_check(operator, fed_value, checking_value):
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