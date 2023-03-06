#ifndef STAGE_1_FUNCTIONS_H
#define STAGE_1_FUNCTIONS_H
#include <string>
#include "Arrays_Classes_Variables.h"
using namespace std;
// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- Methods ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- //
// Color Text Method
string color_text(int a, string text) {
    string code;
    switch (a) {
        case 31:
            code = "\033[31m"; // Red Text
            break;
        case 32:
            code = "\033[32m"; // Green Text
            break;
        case 33:
            code = "\033[33m"; // Yellow Text
            break;
        case 34:
            code = "\033[34m"; // Blue Text
            break;
        case 35:
            code = "\033[35m"; // Purple Text
            break;
        case 36:
            code = "\033[36m"; // Cyan Text
            break;
        case 37:
            code = "\033[37m"; // White Text
            break;
        default:
            code = "\033[0m"; // Default Text
            break;
    }
    return code + text + "\033[0m";
}
#endif //STAGE_1_FUNCTIONS_H
