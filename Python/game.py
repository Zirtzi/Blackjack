from variables import *

deck = Deck()
deck.shuffle()
deck.deal_rigged_order()
deal(deck)
show_hand(player_hand)
show_hand(dealer_hand)
play_hand(deck)