from variables_alpha_2 import *

# Initialization of deck as well as shuffle
for i in range(1):
    # Initialization of deck as well as shuffle
    deck = Deck()
    deck.shuffle()
    # Show the deck before the hands are dealt
    # deck.deal_cards()

    # Deal and show hands of player
    deal_hand(deck)
    play_game(deck)
    # player_hand.clear()
    # dealer_hand.clear()