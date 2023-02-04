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

# ----- ----- ----- ----- ----- ----- ----- ----- Methods ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #
# Blackjack card value method
def blackjack_card_value(value):
    if value.rank == "Ace":
        value.ace_value = 11
        return value.ace_value
    elif value.rank == "2":
        value.value = 2
        return value.value
    elif value.rank == "3":
        value.value = 3
        return value.value
    elif value.rank == "4":
        value.value = 4
        return value.value
    elif value.rank == "5":
        value.value = 5
        return value.value
    elif value.rank == "6":
        value.value = 6
        return value.value
    elif value.rank == "7":
        value.value = 7
        return value.value
    elif value.rank == "8":
        value.value = 8
        return value.value
    elif value.rank == "9":
        value.value = 9
        return value.value
    elif value.rank in ["10", "Jack", "Queen", "King"]:
        value.value = 10
        return value.value

# Initial deal method
def init_deal(deck, hand_of_player, hand_of_dealer):
    for turn in range(4):
        card_drawn = deck.draw()
        if (turn % 2) == 0:
            hand_of_player.append(card_drawn)
        elif (turn % 2) == 1:
            hand_of_dealer.append(card_drawn)

# Adding values of players
def add_player_total(player):
    total = 0
    for card in player:
        total += card.card_value()
    return total

# Check rank of cards method
def check_for_rank(hand, checking_rank):
    result = False
    for card in hand:
        if card.rank in checking_rank:
            result = True
            break
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

# Check same value
def check_same_value(hand, value):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if blackjack_card_value(card_1) == value and blackjack_card_value(card_2) == value:
        result = True
    else:
        result = False
    return result

# Check same rank
def check_same_rank(hand, card_rank):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if card_1.rank == card_rank and card_2.rank == card_rank:
        result = True
    else:
        result = False
    return result

# Initial hand method
def init_hands():
    # Both players have Blackjack
    if check_for_blackjack(player_hand) == True and check_for_blackjack(dealer_hand) == True:
        print("\n")
        print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40m{players[0]} has blackjack!\033[0m")
        print(f"{players[-1]}'s hand is: {dealer_hand} \033[1;31;40m{players[-1]} has blackjack!\033[0m")
        print(f"\033[1;31;40mIt is a draw!\033[0m")
        print("\n")
    # Player 1 has Blackjack, dealer doesn't
    elif check_for_blackjack(player_hand) == True and check_for_blackjack(dealer_hand) == False:
        print("\n")
        print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40m{players[0]} has blackjack!\033[0m")
        print(f"{players[-1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}" + f"] "
              f"\033[1;31;40mwith a current value\033[0m of: "
              f"\033[1;31;40m{add_player_total(dealer_hand)-dealer_hand[0].card_value()}\033[0m")
        print(f"\033[1;31;40m{players[0]} Wins!\033[0m")
        print("\n")
    # Dealer has Blackjack, player 1 doesn't
    elif check_for_blackjack(player_hand) == False and check_for_blackjack(dealer_hand) == True:
        print("\n")
        print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40mwith a current value\033[0m of "
              f"\033[1;31;40m{add_player_total(player_hand)}\033[0m")
        print(f"{players[-1]}'s hand is: {dealer_hand} \033[1;31;40m{players[-1]} has blackjack!\033[0m")
        print(f"\033[1;31;40m{players[-1]} Wins!\033[0m")
        print("\n")
    # Both players do not have Blackjack
    elif check_for_blackjack(player_hand) == False and check_for_blackjack(dealer_hand) == False:
        print("\n")
        print(f"{players[0]}'s hand is: {player_hand} \033[1;31;40mwith a current value\033[0m of "
              f"\033[1;31;40m{add_player_total(player_hand)}\033[0m")
        print(f"{players[-1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}" + f"] "
              f"\033[1;31;40mwith a current value\033[0m of: "
              f"\033[1;31;40m{add_player_total(dealer_hand)-dealer_hand[0].card_value()}\033[0m")
        print("\n")