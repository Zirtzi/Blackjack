from variables import *

# Initialization of deck as well as shuffle
for i in range(1):
    # Initialization of deck as well as shuffle
    deck = Deck()
    deck.shuffle()
    deck.deal_cards()

    # Deal and show hands of player
    deal_hand(deck, player_hand, dealer_hand)
    play_game(deck, player_hand)
    player_hand.clear()
    dealer_hand.clear()