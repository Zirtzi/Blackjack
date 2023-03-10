# ----- ----- ----- ----- ----- ----- ----- ----- ----- Imports ----- ----- ----- ----- ----- ----- ----- ----- ----- #
import random, time

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
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Ace", "Spades"),
            Card("Ace", "Spades"),
            Card("Ace", "Spades"),
            Card("Ace", "Spades"),
            Card("Ace", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("2", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
            Card("Jack", "Spades"),
        ]
        self.returned_cards = []

    def draw(self):
        return self.cards.pop()
        # return self.rigged_cards.pop()

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
        print(len(self.cards), " Cards remaining")
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
    if isinstance(hand, list) and all(isinstance(hands, list) for hands in hand):
        total = 0
        for sublist in hand:
            for card in sublist:
                total += card.value_of_card()
        return int(total)
    elif isinstance(hand, list):
        total = 0
        for card in hand:
            total += card.value_of_card()
        return int(total)
    else:
        raise ValueError("Hand is not a list.")

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

# Deal method
def deal(deck):
    for turn in range(4):
        if (turn % 2) == 0:
            hit(deck, player_hand)
        elif (turn % 2) == 1:
            hit(deck, dealer_hand)
    player_aces = sum(card.rank == "Ace" for card in player_hand)
    dealer_aces = sum(card.rank == "Ace" for card in dealer_hand)
    for card in player_hand:
        if player_aces == 1:
            if card.rank == "Ace":
                card.card_value = 11
            else:
                pass
        elif player_aces > 1:
            if card.rank == "Ace":
                card.card_value = 1
            else:
                pass
        player_aces -= 1
    for card in dealer_hand:
        if dealer_aces == 1:
            if card.rank == "Ace":
                card.card_value = 11
            else:
                pass
        elif dealer_aces > 1:
            if card.rank == "Ace":
                card.card_value = 1
            else:
                pass
        dealer_aces -= 1
    show_hand(player_hand)
    show_hand(dealer_hand)
    return [player_hand, dealer_hand]

# Dealer logic method
def dealer_logic(deck, hand):
    global dealer_total
    global dealer_hand
    dealer_total = add_card_total(dealer_hand)
    player_total = add_card_total(hand)
    if player_total <= 21:
        while dealer_total < 17:
            hit(deck, dealer_hand)
            dealer_total = add_card_total(dealer_hand)
            print(f"Dealer hits, current hand: {dealer_hand} with a current total"
                  f" of \033[1;31;40m{dealer_total}\033[0m")
    print("\n")
    if player_total > 21:
        print(f"Player has busted with a final value of {player_total}. Player loses. Here are the final hands:")
        show_hand(hand)
        show_hand(dealer_hand, 1)
    elif player_total <= 21:
        if dealer_total == player_total:
            print(f"Both players have the same final value of {player_total}. It is a push. Here are the final"
                  f" hands.")
            show_hand(hand)
            show_hand(dealer_hand, 1)
        elif dealer_total > player_total and dealer_total <= 21:
            print(f"Dealer has a greater final value of {dealer_total}. Player loses. Here are the final hands:")
            show_hand(hand)
            show_hand(dealer_hand, 1)
        elif dealer_total < player_total:
            print(f"Player has a greater final value of {player_total}. Player wins. Here are the final hands:")
            show_hand(hand)
            show_hand(dealer_hand, 1)
        elif dealer_total > 21:
            print(f"Dealer has busted with a final value of {dealer_total}. Player wins. Here are the final hands:")
            show_hand(hand)
            show_hand(dealer_hand, 1)
        else:
            pass

# Dealer play method
def dealer_play(deck ,hand):
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
        if current_total < 21:
            all_over_21 = False
            break
    print("\n" "The dealer will now play their hand.")
    if all_over_21:
        print("\n" "The player has on both hands therefore the dealer has won both hands. Here are the final hands:")
        for current_hand in hand:
            show_hand(current_hand)
        show_hand(dealer_hand,1)
    elif all_over_21 == False:
        if player_split_aces == True or player_split_hand == True:
            for current_hand in hand:
                dealer_logic(deck, current_hand)
        elif player_split_aces != True and player_split_hand != True:
            dealer_logic(deck, player_hand)
    else:
        pass

# Hit method
def hit(deck, hand):
    card_drawn = deck.draw()
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
    player_hand_total = add_card_total(hand)
    has_hit = False
    response = ""
    while response not in ["h", "s", "d"] and player_hand_total < 21:
        if not has_hit:
            print("\n" "Your current hand is:")
            show_hand(hand)
            response = input("\n" f"Would you like to hit, stay, or double down on your current hand? (h/s/d): ")
            print("\n")
        elif has_hit:
            print("\n" "Your current hand is:")
            show_hand(hand)
            response = input("\n" f"Would you like to hit or stay? (h/s): ")
            print("\n")
        if response.lower() == "h":
            has_hit = True
            hit(deck, hand)
            player_hand_total = add_card_total(hand)
            if player_hand_total > 21:
                print(f"Player has busted with a final value of \033[1;31;40m{player_hand_total}\033[0m.")
                show_hand(hand)
                break
            elif player_hand_total < 21:
                print(f"Player hits current hand.")
            elif player_hand_total == 21:
                print(f"Player has \033[1;31;40m{player_hand_total}\033[0m. No more cards will be accepted.")
                show_hand(hand)
            response = ""
        elif response.lower() == "s":
            player_hand_total = add_card_total(hand)
            print(f"Player has chosen to stay, current hand: {hand}"
                  f" with a current total of \033[1;31;40m{player_hand_total}\033[0m")
            show_hand(hand)
        elif response.lower() == "d" and not has_hit:
            hit(deck, hand)
            player_hand_total = add_card_total(hand)
            if player_hand_total > 21:
                print(f"Player has doubled down and busted, current hand: {hand}, with a current total of "
                      f"\033[1;31;40m{player_hand_total}\033[0m")
                show_hand(hand)
            elif player_hand_total <= 21:
                print(f"Player has doubled down, current hand: {hand}, with a current total"
                      f" of \033[1;31;40m{player_hand_total}\033[0m")
                show_hand(hand)
        else:
            print("\033[1;31;40mInvalid choice\033[0m." "\n")
            continue
    return [hand]

# Flurdbop Method
def play_hand(deck):
    global player_hand
    global dealer_hand
    global player_split_aces
    global player_split_hand
    deal(deck)
    if dealer_hand[1].rank == "Ace":
        insurance_choice = ""
        while insurance_choice not in ["y", "n"]:
            insurance_choice = input("\n" f"The dealer is showing an {dealer_hand[1].rank},"
                                     f" would you like to buy insurance? (y/n): ")
            if insurance_choice.lower() == "y":
                print("\n" "The player has chosen to buy insurance. We will now check for if the dealer"
                      " has blackjack.")
                if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
                    print("\n" "Both players have blackjack, it is a push. Player wins insurance.")
                    show_hand(player_hand)
                    show_hand(dealer_hand, 1)
                    break
                elif check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand) == False:
                    print("\n" "The dealer has blackjack, player wins insurance.")
                    show_hand(player_hand)
                    show_hand(dealer_hand, 1)
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
                    print("\n" "The player has blackjack, the dealer does not. Player loses insurance"
                          " but wins the hand.")
                    show_hand(player_hand)
                    show_hand(dealer_hand, 1)
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
                    print("\n" "Neither player has blackjack, player loses insurance. The hand will continue.")
                    show_hand(player_hand)
                    show_hand(dealer_hand)
                    player_hand_logic(deck)
            elif insurance_choice.lower() == "n":
                print("\n" "The player has chosen to not play insurance. We will now check for if the dealer"
                      " has blackjack.")
                if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
                    print("\n" "Both players have blackjack, it is a push.")
                    show_hand(player_hand)
                    show_hand(dealer_hand, 1)
                    break
                elif check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand) == False:
                    print("\n" "The dealer has blackjack, the player does not. Player loses.")
                    show_hand(player_hand)
                    show_hand(dealer_hand, 1)
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
                    print("\n" "The dealer does not have blackjack, but the player does. Player wins.")
                    show_hand(player_hand)
                    show_hand(dealer_hand, 1)
                    break
                elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
                    print("\n" "Neither player has blackjack. The hand will continue.")
                    show_hand(player_hand)
                    show_hand(dealer_hand)
                    player_hand_logic(deck)
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m" "\n")
                continue
    if dealer_hand[1].rank != "Ace":
        if check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand):
            print("\n" "Both players have blackjack. It is a push.")
            show_hand(player_hand)
            show_hand(dealer_hand, 1)
        elif check_for_blackjack(dealer_hand) and check_for_blackjack(player_hand) == False:
            print("\n" "The dealer has blackjack, the player does not. Player loses.")
            show_hand(player_hand)
            show_hand(dealer_hand, 1)
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand):
            print("\n" "The player has blackjack, the dealer does not. Player wins.")
            show_hand(player_hand)
            show_hand(dealer_hand, 1)
        elif check_for_blackjack(dealer_hand) == False and check_for_blackjack(player_hand) == False:
            player_hand_logic(deck)
        else:
            raise ValueError("A fatal error has occured.")
    player_hand.clear()
    dealer_hand.clear()
    player_split_aces = None
    player_split_hand = None

# Player hand logic
def player_hand_logic(deck):
    global player_hand
    player_hand = player_same_rank_check(deck)[0]
    if player_split_aces == True:
        print("\n" "Here are the final hands of the player:")
        for current_hand in player_hand:
            show_hand(current_hand)
        dealer_play(deck, player_hand)
    elif player_split_hand == True:
        print("Here are the current hands of the player:")
        for current_hand in player_hand:
            show_hand(current_hand)
        hand_counter = 1
        for current_hand in player_hand:
            if hand_counter > 1:
                hit(deck, current_hand)
            else:
                pass
            hit_stay_double_down(deck, current_hand)
            hand_counter += 1
        print("\n" "The final hands of the player are: ")
        for current_hand in player_hand:
            show_hand(current_hand)
        dealer_play(deck, player_hand)
    elif player_split_aces != True and player_split_hand != True:
        hit_stay_double_down(deck, player_hand)
        dealer_play(deck, player_hand)

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
                
                print("\n" f"You have chosen to split your {player_hand[0].rank}'s." "\n")
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
                break
            else:
                print("\n" "\033[1;31;40mInvalid choice\033[0m." "\n")
                continue
    elif check_same_rank(player_hand) and check_same_rank(player_hand, "Ace") == False:
        
        same_rank_response = ""
        while same_rank_response not in ["y", "n"]:
            same_rank_response = input("\n" f"You have the same rank of {player_hand[0].rank} in your hand. Would you like"
                                       f" to split your hand? (y/n): ")
            if same_rank_response.lower() == "y":
                
                print("\n" f"You have chosen to split your {player_hand[0].rank}'s." "\n")
                hand_1 = split_hand(player_hand)[0][1]
                hand_2 = split_hand(player_hand)[0][0]
                hit(deck, hand_1)
                player_split_hand = True
                split_hands = []
                checking_hand = hand_1
                if check_same_rank(checking_hand):
                    
                    print(f"You have pulled the same rank of {checking_hand[1].rank} again. Here are your current"
                          f" hands:")
                    show_hand(checking_hand)
                    show_hand(hand_2)
                    split_counter = 1
                    while split_counter <= 3 and check_same_rank(checking_hand):
                        
                        split_again_choice = ""
                        while split_again_choice not in ["y", "n"]:
                            split_again_choice = input("\n" f"Would you like to split your {checking_hand[1].rank}'s"
                                                       f" again? (y/n): ")
                            if split_again_choice.lower() == "y":
                                split_counter += 1
                                
                                print("\n" f"You have chosen to split your hand again."
                                      f" Total times split: {split_counter}")
                                new_hand_1 = split_hand(checking_hand)[0][1]
                                new_hand_2 = split_hand(checking_hand)[0][0]
                                split_hands.insert(0, new_hand_2)
                                hit(deck, new_hand_1)
                                checking_hand = new_hand_1
                                
                                break
                            elif split_again_choice.lower() == "n":
                                
                                break
                            else:
                                print("\n" "\033[1;31;40mInvalid choice\033[0m.")
                                continue
                        if check_same_rank(checking_hand) and split_again_choice.lower() == "y":
                            if split_counter < 4:
                                print("\n" "Your current hands are: ")
                                split_hands.insert(0, checking_hand)
                                split_hands.append(hand_2)
                                for current_hand in split_hands:
                                    show_hand(current_hand)
                                split_hands.remove(checking_hand)
                                split_hands.remove(hand_2)
                            elif split_counter == 4:
                                
                                print("\n" f"You can no longer split your hands. Times split: {split_counter}" "\n")
                                split_hands.insert(0, checking_hand)
                            else:
                                pass
                            continue
                        elif check_same_rank(checking_hand) == False or split_again_choice.lower() == "n":
                            if check_same_rank(checking_hand) == False:
                                
                                print("\n" f"You did not pull the same rank of {checking_hand[0].rank} again."
                                      f" Total times split: {split_counter}" "\n")
                            elif split_again_choice.lower() == "n":
                                
                                print("\n" f"You have chosen to not split your hand again."
                                      f" Total times split: {split_counter}" "\n")
                            else:
                                pass
                            split_hands.insert(0, checking_hand)
                            break
                        else:
                            raise ValueError("\033[1;31;40mA catastrophic error has occurred.\033[0m")
                            break
                    split_hands.append(hand_2)
                elif check_same_rank(checking_hand) == False:
                    split_hands.insert(0, hand_1)
                    split_hands.append(hand_2)
                else:
                    pass
                new_hand = split_hands
                
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

# Show hands of players method
def show_hand(hand, dealer_display = None):
    if hand != dealer_hand:
        if isinstance(hand, list) and isinstance(hand[0], list):
            for current_hand in hand:
                print(f"{players[0]}'s current hand is: {current_hand} with a"
                      f" current total of \033[1;31;40m{add_card_total(current_hand)}\033[0m")
        elif isinstance(hand, list) and not isinstance(hand[0], list):
            print(f"{players[0]}'s hand is: {hand} with a current total of \033[1;31;40m{add_card_total(hand)}\033[0m")
    elif hand == dealer_hand and dealer_display is None:
        print(f"{players[-1]}'s hand is: [Hidden, {hand[1]}] with a current total"
              f" of \033[1;31;40m{hand[1].card_value}\033[0m")
    elif hand == dealer_hand and dealer_display is not None:
        print(f"{players[-1]}'s hand is {hand} with a current total of \033[1;31;40m{add_card_total(hand)}\033[0m")

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