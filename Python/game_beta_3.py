from structure_beta_3 import *

deck = Deck()
deck.Shuffle()
dealer_hand = Dealer_Hand()
player_hand = Player_Hand("Player 1")
Player_Bank = bank_prompt()
while value_check(">=", len(deck.cards), 13) and value_check(">", Player_Bank, 0):
    print(Player_Bank)
    if value_check(">=", len(deck.cards), 13) and value_check(">", Player_Bank, 0):
        print("Cards remaining: ", len(deck.cards), "\n")
        Player_Bank = play_hand(deck, dealer_hand, player_hand)[-1]
    elif value_check("<", len(deck.cards), 13) and value_check(">", Player_Bank, 0):
        print("\n" "A new deck is being shuffled")
        deck = Deck()
        deck.Shuffle()
        continue
    else:
        continue
    if value_check("<=", Player_Bank, 0):
        print("\n" "You have run out of money. You can no longer play.")
        break
    else:
        continue