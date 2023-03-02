from structure_beta_3 import *

deck = Deck()
deck.Shuffle()
player_hand = Player_Hand("Player")
dealer_hand = Dealer_Hand()
while len(deck.cards) >= 13:
    print("Cards remaining: ", len(deck.cards))
    play_hand(deck, dealer_hand, player_hand)
    if len(deck.cards) < 13:
        print("\n" "A new deck is being shuffled")
        deck = Deck()
        deck.Shuffle()
        continue
    else:
        continue