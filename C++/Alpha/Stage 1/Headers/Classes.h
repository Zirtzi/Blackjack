#ifndef STAGE_1_CLASSES_H
#define STAGE_1_CLASSES_H
#include <algorithm>
#include <random>
#include <stack>
#include <string>
#include <typeinfo>
#include <vector>
#include "Functions.h"
using namespace std;
// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- Classes & Arrays ---- ---- ---- ---- ---- ---- ---- ---- ---- //
string Suits[4] = {"Clubs", "Diamonds", "Hearts", "Spades"};
string Ranks[13] = {"Ace", "2", "3", "4", "5", "6", "7", "8",
                    "9", "10", "Jack", "Queen", "King"};
// Card class
class Card {
public:
    // Public variables
    string rank;
    string suit;
    string display_card_value;
    int card_value;
    // Constructor
    Card(string rank, string suit) {
        if (rank == Ranks[0]) {
            this->rank = color_text(32, Ranks[0]);
            card_value = 11;
            this->display_card_value = color_text(33, to_string(card_value));
        }
        else if (rank == Ranks[10] || rank == Ranks[11] || rank == Ranks[12]) {
            if (rank == Ranks[10]) {
                this->rank = color_text(32, Ranks[10]);
            }
            else if (rank == Ranks[11]) {
                this->rank = color_text(32, Ranks[11]);
            }
            else if (rank == Ranks[12]) {
                this->rank = color_text(32, Ranks[12]);
            }
            else {}
            card_value = 10;
            this->display_card_value = color_text(33, to_string(card_value));
        }
        else {
            for (int i = 1; i <= 9; i++) {
                if (rank == Ranks[i]) {
                    this->rank = color_text(32, Ranks[i]);
                    card_value = stoi(rank);
                }
                else {}
            }
            this->display_card_value = color_text(33, to_string(card_value));

        }
        if (suit == Suits[0] || suit == Suits[3]) {
            this->suit = color_text(35, suit);
        }
        else if (suit == Suits[1] || suit == Suits[2]) {
            this->suit = color_text(31, suit);
        }
    }
    // Value of card method
    int Value_of_Card() {
        return card_value;
    }
    // Change value of card method
    void Set_New_Value(int new_value) {
        card_value = new_value;
    }
    // Representation method
    friend ostream & operator << (ostream & os, const Card & card) {
        os << "[" << card.rank << " of " << card.suit << "]" << " Card Value : " << card.display_card_value;
        return os;
    }
};

// Deck Class
class Deck {
public:
    // Public variables
    vector<Card> cards;
    vector<Card> returned_cards;
    vector<Card> rigged_cards;
    int num_of_decks;
    // Constructor
    Deck(int decks) {
        this->num_of_decks = decks;
        for (int i = 1; i <= decks; i++) {
            for (const auto & rank : Ranks) {
                for (const auto & suit : Suits) {
                    this->cards.push_back(Card(rank, suit));
                }
            }
        }
    }
    // Shuffle method
    void Shuffle() {
        random_device rd;
        std::mt19937 g(rd());
        shuffle(this->cards.begin(), this->cards.end(), g);
    }
    // Draw method
    Card Draw() {
        if (this->rigged_cards.empty()) {
            Card card_drawn = this->cards.back();
            this->cards.pop_back();
            return card_drawn;
        }
        else if (this->rigged_cards.size() > 0) {
            Card card_drawn = this->rigged_cards.back();
            this->rigged_cards.pop_back();
            return card_drawn;
        }
        else {}
    }
    // Deal cards method
    void Deal_Cards() {
        cout << "\n" "Here are the cards in the deck:" << endl << endl;
        bool rigged_deck = false;
        int card_dealt_number = 1;
        int num_of_cards = num_of_decks*52;
        int deck_counter = 1;
        string deck_place_holder;
        if (this->rigged_cards.size() > 0) {
            rigged_deck = true;
        }
        else {}
        if (rigged_deck == false) {
            for (int i = 1; i <= num_of_cards; i++) {
                if (i == 1) {
                    cout << "Dealing the deck(s):" "\n" << endl;
                }
                else {}
                Card drawn_card = Draw();
                this->returned_cards.push_back(drawn_card);
                cout << "Card dealt number: " << color_text(33, to_string(card_dealt_number)) <<
                 " - " << drawn_card << endl;
                if (card_dealt_number % 52 == 0) {
                    if (num_of_cards > 52) {
                        deck_place_holder = to_string(deck_counter);
                    }
                    else if (num_of_cards == 52) {
                        deck_place_holder = "";
                    }
                    else {}
                    cout << "\n" << "End of deck " << color_text(33, deck_place_holder) << "\n" << endl;
                    deck_counter += 1;
                }
                card_dealt_number += 1;
            }
            this->cards = this->returned_cards;
            reverse(this->cards.begin(), this->cards.end());
            cout << color_text(33, to_string(this->cards.size())) << " cards in "
            << color_text(33, to_string(num_of_decks)) << " deck(s)." << endl;
        }
        else if (rigged_deck == true) {
            int num_of_rigged_cards = this->rigged_cards.size();
            for (int i = 1; i <= num_of_rigged_cards; i++) {
                if (i == 1) {
                    cout << "Dealing rigged deck:" "\n" << endl;
                }
                else {}
                Card drawn_card = Draw();
                this->returned_cards.push_back(drawn_card);
                cout << "Card dealt number: " << color_text(33, to_string(card_dealt_number))
                << " - " << drawn_card << endl;
                card_dealt_number += 1;
            }
            this->rigged_cards = this->returned_cards;
            reverse(this->rigged_cards.begin(), this->rigged_cards.end());
            cout << "\n" << color_text(33, to_string(this->rigged_cards.size()))
            << " cards in rigged deck." << endl;
        }
        else {}
    }
    // Representation method
    friend ostream & operator << (ostream & os, const Deck & deck) {
        os << "\n" "Deck of " << color_text(33, to_string(deck.cards.size())) << " cards and "
        << color_text(33, to_string(deck.num_of_decks)) << " deck(s)." << endl;
        return os;
    }
};

// Hand Class
class Hand{
public:
    // Public variables
    vector<Card> cards;
    string name;
    int hand_value;
    float hand_wager;
    // Constructor
    Hand(string name = "") {
        this->hand_value = 0;
        this->hand_wager = 0;
    }
    // Add cards to hand method
    void Add_Card_To_Hand(Card card) {
        this->cards.push_back(card);
    }
    // Add hand total method
    int Add_Hand_Total() {
        int ace_count = 0;
        int running_hand_value = 0;
        for (const Card & current_card : this->cards) {
            if (current_card.rank == color_text(32, "Ace")) {
                ace_count += 1;
            }
            else {}
        }
        for (Card & current_card : this->cards) {
            if (ace_count == 1) {
                if (current_card.rank == color_text(32, "Ace")) {
                    current_card.Set_New_Value(11);
                }
                else {}
            }
            else if (ace_count > 1) {
                if (current_card.rank == color_text(32, "Ace")) {
                    current_card.Set_New_Value(1);
                }
                else {}
            }
            else {}
            running_hand_value += current_card.Value_of_Card();
            ace_count -= 1;
        }
        if (running_hand_value > 21) {
            running_hand_value = 0;
            for (Card & current_card : this->cards) {
                if (current_card.rank == color_text(32, "Ace")) {
                    current_card.Set_New_Value(1);
                    running_hand_value += current_card.Value_of_Card();
                }
                else {}
            }
        }
        else {}
        this->hand_value = running_hand_value;
        return this->hand_value;
    }
    // Hit hand method
    Hand Hit_Hand(Deck & deck) {
        Add_Card_To_Hand(deck.Draw());
        return Hand();
    }
};
#endif //STAGE_1_CLASSES_H