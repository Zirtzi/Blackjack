#ifndef STAGE_1_FUNCTIONS_H
#define STAGE_1_FUNCTIONS_H
#include <algorithm>
#include <cctype>
#include <chrono>
#include <cmath>
#include <iomanip>
#include <random>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <thread>
#include <typeinfo>
#include <vector>
#include "Classes_Variables.h"
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
// String to float conversion method
string float_validation(string entry) {
    string result = "";
    bool has_decimal = false;
    if (entry.front() != '-') {
        for (int i = 0; i < entry.length(); i++) {
            if (!isdigit(entry[i])) {
                if (entry[i] == '.' && !has_decimal) {
                    has_decimal = true;
                }
                else {
                    // Failed Non-Negative Value
                    result = "FNNV";
                    return result;
                }
            }
            else if (isdigit(entry[i])) {
                continue;
            }
            else {}
        }
    }
    else if (entry.front() == '-') {
        for (int i = 1; i < entry.length(); i++) {
            if (!isdigit(entry[i])) {
                if (entry[i] == '.' && !has_decimal) {
                    has_decimal = true;
                }
                else {
                    // Failed Negative Value 1
                    result = "FNV1";
                    return result;
                }
            }
            else if (isdigit(entry[i])) {
                continue;
            }
            else {}
        }
        // Failed Negative Value 2
        result = "FNV2";
        return result;
    }
    else {}
    result = "Passed";
    return result;
}
// Round values to string method
string round_to_string(float entry_value) {
    ostringstream oss;
    oss << fixed << setprecision(2) << entry_value;
    string return_string = oss.str();
    return return_string;
}
// Round wager / bank method
float round_wager_bank(float entry_value) {
    entry_value = round(entry_value * 100) / 100;
    return entry_value;
}
// Sleep method
void time_sleep(long sleep_time) {
    this_thread::sleep_for(chrono::seconds(sleep_time));
}
#endif //STAGE_1_FUNCTIONS_H
