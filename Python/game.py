from variables import *

deck = Deck()
deck.shuffle()
deck.deal_rigged_order()
# deck.deal_cards()
deal(deck)
play_hand(deck)