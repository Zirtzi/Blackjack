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
#endif //STAGE_1_ARRAYS_CLASSES_VARIABLES_H