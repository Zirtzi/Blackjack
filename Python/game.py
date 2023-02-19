from variables import *

deck = Deck()
deck.shuffle()
deck.deal_rigged_order()
deal(deck)
show_hand(player_hand)
show_hand(dealer_hand, 1)
hit_stay_double_down(deck, player_same_rank_check(deck)[0])