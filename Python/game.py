from variables import *

for i in range(1):
    deck = Deck()
    deck.shuffle()
    deck.deal_cards()
    player_hand.append(Card("1", "Diamonds"))
    player_hand.append(Card("1", "Hearts"))
    dealer_hand.append(Card("Ace", "Clubs"))
    dealer_hand.append(Card("Ace", "Spades"))
    print("\n")
    display_hand(player_hand)
    display_hand(dealer_hand, 1)
    print("\n")
    parameter_check(player_hand)
    parameter_check(dealer_hand)
    print("\n")
    conditions_check()