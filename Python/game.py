from frostbite_casino import *

for i in range(1):
    deck = Deck()
    deck.shuffle()
    deck.deal_cards()
    # player_hand.append(Card("10", "Diamonds"))
    # player_hand.append(Card("2", "Hearts"))
    # dealer_hand.append(Card("2", "Clubs"))
    # dealer_hand.append(Card("2", "Spades"))
    deal_hand(deck)