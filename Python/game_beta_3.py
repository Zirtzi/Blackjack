from structure_beta_3 import *

deck = Deck()
deck.Deal_Rigged_Cards()
player_hand = Hand("Player")
player_hand.Add_Card_To_Hand(Card("Ace", "Spades"))
player_hand.Add_Card_To_Hand(Card("Ace", "Spades"))
player_hand.Show_Hand()