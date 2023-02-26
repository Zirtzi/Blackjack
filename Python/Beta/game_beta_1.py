from structure_beta_1 import *

deck = Deck()
deck.shuffle()
while len(deck.cards) >= 13:
    # deck.deal_rigged_order()
    deck.deal_cards()
    play_hand(deck)
    if len(deck.cards) <= 13:
        deck = Deck()
        deck.shuffle()