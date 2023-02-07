from variables import *

# Initialization of deck as well as shuffle
counter = 0
for i in range(1000):
    counter += 1
    # Initialization of deck as well as shuffle
    deck = Deck()
    deck.shuffle()

    # Printing the deck one time as a safety way to make sure cards are being dealt in the right order
    deck.deal_cards()
    print(f"Current deck dealing # - {counter}")

    # Deal and show hands of player
    init_deal(deck, player_hand, dealer_hand)
    player_hand.clear()
    dealer_hand.clear()
