#include <iostream>
#include "Headers/main.h"
using namespace std;

int main() {
    Deck deck(6);
    deck.Shuffle();
    deck.Deal_Cards();
    return 0;
}
