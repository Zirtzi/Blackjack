#ifndef STAGE_1_ARRAYS_CLASSES_VARIABLES_H
#define STAGE_1_ARRAYS_CLASSES_VARIABLES_H
#include <string>
#include "Functions.h"
using namespace std;
// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- Arrays ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- //
// Suits and Ranks of cards
string Suits[4] = {color_text(35, "Clubs"), color_text(31, "Diamonds"),
                  color_text(31, "Hearts"), color_text(35, "Spades")};
string Ranks[13] = {color_text(32, "Ace"), color_text(32, "2"), color_text(32, "3"),
                  color_text(32, "4"), color_text(32, "5"), color_text(32, "6"),
                  color_text(32, "7"), color_text(32, "8"), color_text(32, "9"),
                  color_text(32, "10"), color_text(32, "Jack"), color_text(32, "Queen"),
                  color_text(32, "King")};

// Classes
class Card {
public:
    string rank;
    string suit;
    int card_value;
    Card(string rank, string suit) {
        if (rank == "Ace") {
            card_value = 11;
        }
        else if (rank == "Jack" || rank == "Queen" || rank == "King") {
            card_value = 10;
        }
        else {
            card_value = stoi(rank);
        }
    }
    int Value_of_Card() {
        return card_value;
    }
    void Set_New_Value(int new_value) {
        card_value = new_value;
    }
};


#endif //STAGE_1_ARRAYS_CLASSES_VARIABLES_H