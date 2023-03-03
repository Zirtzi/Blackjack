from structure_beta_3 import *
deck = Deck()
deck.Shuffle()
dealer_hand = Dealer_Hand()
player_hand = Player_Hand("Player 1")
Player_Bank = player_bank(player_hand)
while len(deck.cards) >= 13 and Player_Bank > 0:
    Player_Bank = play_hand(deck, dealer_hand, player_hand)[-1]
    if len(deck.cards) >= 13 and Player_Bank > 0:
        print("\n" f"Shuffling a new hand. Player bank: \033[1;31;40m{Player_Bank}\033[0m with"
              f" \033[1;31;40m{len(deck.cards)}\033[0m cards remaining." "\n")
        time.sleep(1)
        continue
    elif len(deck.cards) < 13 and Player_Bank > 0:
        print("\n" "Shuffling a new deck. Player bank: \033[1;31;40m{Player_Bank}\033[0m with"
              " \033[1;31;40m{len(deck.cards)}\033[0m cards remaining." "\n")
        deck = Deck()
        deck.Shuffle()
        time.sleep(1)
        continue
    elif Player_Bank <= 0:
        print("\n" "You are out of money. You can no longer play." "\n")
        time.sleep(1)
        break
    else:
        continue