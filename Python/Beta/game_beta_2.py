from structure_beta_2 import *

# Play game
deck = Deck()
deck.Shuffle()
while value_check(">=", len(deck.cards), 13):
    deck.Deal_Cards()
    play_hand(deck)
    if value_check("<=", len(deck.cards), 13):
        deck = Deck()
        deck.Shuffle()
    elif value_check(">", len(deck.cards), 13):
        continue
    else:
        pass