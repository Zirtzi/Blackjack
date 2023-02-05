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
# Adding values of players
def add_player_total(player):
    total = 0
    for card in player:
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

# Check same rank method
def check_same_rank(hand):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if card_1.rank == card_2.rank:
        result = True
    else:
        result = False
    return result


# Check for same suit method
def check_same_suit(hand):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if card_1.suit == card_2.suit:
        result = True
    else:
        result = False
    return result

# Check same value method
def check_same_value(hand):
    result = False
    card_1 = hand[0]
    card_2 = hand[-1]
    if card_1.value_of_card() == card_2.value_of_card():
        result = True
    else:
        result = False
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

# Initial deal method
def init_deal(deck, hand_of_player, hand_of_dealer):
    for turn in range(4):
        card_drawn = deck.draw()
        if (turn % 2) == 0:
            hand_of_player.append(card_drawn)
        elif (turn % 2) == 1:
            hand_of_dealer.append(card_drawn)
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
        print(f"{players[-1]}'s hand is: {dealer_hand} with \033[1;33;40mtotal value\033[0m of: "
              f"\033[1;31;40m{add_player_total(dealer_hand)}\033[0m")
        print(f"\033[1;31;40m{players[0]} Wins!\033[0m")
        print("\n")
    # Dealer has Blackjack, player 1 doesn't
    elif check_for_blackjack(player_hand) == False and check_for_blackjack(dealer_hand) == True:
        print("\n")
        print(f"{players[0]}'s hand is: {player_hand} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(player_hand)}\033[0m")
        print(f"{players[-1]}'s hand is: {dealer_hand} \033[1;31;40m{players[-1]} has blackjack!\033[0m")
        print(f"\033[1;31;40m{players[-1]} Wins!\033[0m")
        print("\n")
    # Both players do not have Blackjack
    elif check_for_blackjack(player_hand) == False and check_for_blackjack(dealer_hand) == False:
        print("\n")
        print(f"{players[0]}'s hand is: {player_hand} with \033[1;33;40mtotal "
              f"value\033[0m of: \033[1;31;40m{add_player_total(player_hand)}\033[0m")
        print(f"{players[-1]}'s hand is: [Hidden, " + f"{dealer_hand[-1]}] with \033[1;33;40mtotal value\033[0m of: "
              f"\033[1;31;40m{add_player_total(dealer_hand)-dealer_hand[0].value_of_card()}\033[0m")
        print("\n")
