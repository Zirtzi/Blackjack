#include <iostream>
#include "Headers/main.h"
using namespace std;

int main() {
    for (int i = 0; i < size(Suits); i++) {
        cout << Suits[i];
        if (i < size(Suits) - 1) {
            cout << ", ";
        }
    }
    cout << endl << endl;
    for (int i = 0; i < size(Ranks); i++) {
        cout << Ranks[i];
        if (i < size(Ranks) - 1) {
            cout << ", ";
        }
    }
    cout << endl;
    return 0;
}
