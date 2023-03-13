#ifndef STAGE_1_STRUCTURE_H
#define STAGE_1_STRUCTURE_H
#include "Includes.h"
using namespace std;
// ---- ---- ---- ---- ---- ---- ---- ---- ---- ----  Arrays ---- ---- ---- ---- ---- ---- ---- ---- ---- ----  //
string Suits[4] = {"Clubs", "Diamonds", "Hearts", "Spades"};
string Ranks[13] = {"Ace", "2", "3", "4", "5", "6", "7", "8",
                    "9", "10", "Jack", "Queen", "King"};
// ---- ---- ---- ---- ---- ---- ---- ---- ----  Independent Methods ---- ---- ---- ---- ---- ---- ---- ---- //
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
// ---- ---- ---- ---- ---- ---- ---- ---- ---- ----  Classes ---- ---- ---- ---- ---- ---- ---- ---- ---- ----  //
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
        os << card.rank << " of " << card.suit;
        return os;
    }
};
// Deck Class
class Decks {
public:
    // Public variables
    vector<Card> cards;
    vector<Card> returned_cards;
    vector<Card> rigged_cards;
    int num_of_decks;
    // Constructor
    Decks(int decks) {
        this->num_of_decks = decks;
        for (int i = 1; i <= decks; i++) {
            for (const auto & rank : Ranks) {
                for (const auto & suit : Suits) {
                    this->cards.push_back(Card(rank, suit));
                }
            }
        }
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
    // Shuffle method
    void Shuffle() {
        random_device rd;
        std::mt19937 g(rd());
        shuffle(this->cards.begin(), this->cards.end(), g);
    }
    // Representation method
    friend ostream & operator << (ostream & os, const Decks & deck) {
        os << "\n" "Deck of " << color_text(33, to_string(deck.cards.size())) << " cards and "
        << color_text(33, to_string(deck.num_of_decks)) << " deck(s)." << endl;
        return os;
    }
};
// Hand Class
class Hand{
public:
    // Public variables
    struct Player {
        string name;
        float bank_total;
        int hand_cards_total;
        float hand_wager;
        vector<Card> cards;
    };
    Player current_player;
    // Constructor
    Hand(Player current_player) {
        this->current_player.name = "";
        this->current_player.bank_total = 0;
        this->current_player.hand_cards_total = 0;
        this->current_player.hand_wager = 0;
    }
    // Add cards to hand method
    void Add_Card_To_Hand(Card card) {
        this->current_player.cards.push_back(card);
    }
    // Add hand total method
    int Add_Hand_Total() {
        int ace_count = 0;
        int running_hand_value = 0;
        for (const Card & current_card : this->current_player.cards) {
            if (current_card.rank == color_text(32, "Ace")) {
                ace_count += 1;
            }
            else {}
        }
        for (Card & current_card : this->current_player.cards) {
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
            for (Card & current_card : this->current_player.cards) {
                if (current_card.rank == color_text(32, "Ace")) {
                    current_card.Set_New_Value(1);
                    running_hand_value += current_card.Value_of_Card();
                }
                else if (current_card.rank != color_text(32, "Ace")) {
                    running_hand_value += current_card.Value_of_Card();
                }
                else {}
            }
        }
        else {}
        this->current_player.hand_cards_total = running_hand_value;
        return this->current_player.hand_cards_total;
    }
    // Deposit method
    float Deposit() {
        current_player.bank_total = 0;
        while (current_player.bank_total == 0) {
            while (true) {
                try {
                    string deposit;
                    string try_result;
                    cout << "Please enter an amount you'd like to deposit into your bank: ";
                    getline(cin, deposit);
                    try_result = float_validation(deposit);
                    if (try_result == "FNNV") {
                        throw invalid_argument("\n"
                        + color_text(31, "Invalid entry") + " of " + color_text(31, deposit)
                        + ". Please re-enter your bank total." "\n");
                    }
                    else if (try_result == "FNV1") {
                        throw invalid_argument("\n"
                        + color_text(31, "Invalid entry") + " of " + color_text(31, deposit)
                        + ". Please re-enter your bank total." "\n");
                    }
                    else if (try_result == "FNV2") {
                        throw invalid_argument("\n"
                        + color_text(31, "Negative entry") + " of " + color_text(31, deposit)
                        + ". Please enter a positive value for a bank total." "\n");
                    }
                    else if (try_result == "Passed") {
                        current_player.bank_total = round_wager_bank(stof(deposit));
                        break;
                    }
                    else {}
                }
                catch (const invalid_argument & e) {
                    cout << e.what() << endl;
                }
                if (current_player.bank_total > 0) {
                    break;
                }
                else if (current_player.bank_total < 0) {
                    continue;
                }
            }
        }
        // time_sleep(1.0);
        string Bank_of_Player = round_to_string(current_player.bank_total);
        cout << "\n" << this->current_player.name << " has decided to start with: "
        << color_text(33, Bank_of_Player) << "\n" << endl;
        return current_player.bank_total;
    }
    // Hand name method
    string Hand_Name() {
        string hand_name;
        cout << "\n" "Enter a name for this hand: ";
        getline(cin, hand_name);
        cout << endl;
        this->current_player.name = color_text(34, hand_name);
        // time_sleep(1.0);
        return this->current_player.name;
    }
    // Hit hand method
    Hand Hit_Hand(Decks & deck) {
        Add_Card_To_Hand(deck.Draw());
        return Hand(current_player);
    }
    // Insurance method
    float Insurance(float wager) {
        string insurance_choice = "";
        bool insurance_decision = false;
        while (insurance_choice == "") {
            cout << endl << "Would you like to buy insurance? (y/n): ";
            getline(cin, insurance_choice);
            if (insurance_choice == "y") {
                insurance_decision = true;
            }
            else if (insurance_choice == "n") {
                break;
            }
            else {
                throw invalid_argument("\n"
                + color_text(31, "Invalid choice.") + " of " + color_text(31, insurance_choice)
                + ". Plese re-enter your insurance decision.");
            }
        }
        if (insurance_decision) {
            wager = round_wager_bank(0.5*wager);
            current_player.bank_total -= wager;
            return wager;
        }
        else if (!insurance_decision) {
            current_player.bank_total = current_player.bank_total;
            return wager;
        }
        else {}
    }
    // Place wager method
    float Place_Wager() {
        float wager = 0;
        while (wager == 0) {
            while (true) {
                try {
                    string input_wager;
                    string try_result;
                    // time_sleep(1.0);
                    cout << endl << "\n" "Please place a wager for this hand: ";
                    getline(cin, input_wager);
                    try_result = float_validation(input_wager);
                    if (try_result != "Passed") {
                        if (try_result == "FNNV" || try_result == "FNV1") {
                            // time_sleep(1.0);
                            throw invalid_argument("\n"
                            + color_text(31, "Invalid Wager") + " of " + color_text(31, input_wager)
                            + ". Please enter a number for your wager.");
                        }
                        else if (try_result == "FNV2") {
                            string string_wager = round_to_string(round_wager_bank(stof(input_wager)));
                            // time_sleep(1.0);
                            throw invalid_argument("\n"
                            + color_text(31, "Negative wager") + " of " + color_text(31, string_wager)
                            + ". Please enter a positive number for your wager.");
                        }
                        else {}
                    }
                    else if ((try_result == "Passed") && (stof(input_wager) > current_player.bank_total)) {
                        string string_wager = round_to_string(round_wager_bank(stof(input_wager)));
                        string string_PB = round_to_string(current_player.bank_total);
                        // time_sleep(1.0);
                        throw invalid_argument("\n"
                        + color_text(31, "Invalid wager") + " of " + color_text(31, string_wager)
                        + " due to wager being larger than bank total of "
                        + color_text(31, string_PB) + ". Please re-enter your wager.");
                    }
                    else {
                        wager = round_wager_bank(stof(input_wager));
                        break;
                    }
                }
                catch (const invalid_argument & e) {
                    cout << e.what() << endl;
                }
            }
        }
        // time_sleep(1.0);
        this->current_player.hand_wager = round_wager_bank(wager);
        current_player.bank_total -= this->current_player.hand_wager;
        return this->current_player.hand_wager;
    }
    // Show hand method
    void Show_Hand(string option = "", string dealer_show = "") {
        if (this->current_player.name != color_text(34, "Dealer")) {
            if (option == "") {
                option = "current";
                cout << this->current_player.name << "'s " << color_text(31, option) << " hand: [";
                for (int i = 0; i < this->current_player.cards.size(); i++) {
                    if (i == this->current_player.cards.size() - 1) {
                        cout << this->current_player.cards[i] << "]";
                    }
                    else {
                        cout << this->current_player.cards[i] << " , ";
                    }
                }
                Add_Hand_Total();
                string Rounded_Wager = round_to_string(this->current_player.hand_wager);
                string Bank_of_Player = round_to_string(current_player.bank_total);
                cout << color_text(36, " Hand Total") << ": "
                << color_text(36, to_string(this->current_player.hand_cards_total)) << " , "
                << color_text(31, "Hand Wager") << ": " << color_text(31, Rounded_Wager)
                << " , " << color_text(33, "Bank Total") << ": " << color_text(33, Bank_of_Player);
                // time_sleep(1.0);
            }
            else if (option != "") {
                cout << this->current_player.name << "'s " << color_text(31, option) << " hand: [";
                for (int i = 0; i < this->current_player.cards.size(); i++) {
                    if (i == this->current_player.cards.size() - 1) {
                        cout << this->current_player.cards[i] << "]";
                    }
                    else {
                        cout << this->current_player.cards[i] << " , ";
                    }
                }
                Add_Hand_Total();
                string Rounded_Wager = round_to_string(this->current_player.hand_wager);
                string Bank_of_Player = round_to_string(current_player.bank_total);
                cout << color_text(36, " Hand Total") << ": "
                << color_text(36, to_string(this->current_player.hand_cards_total)) << " , " <<
                color_text(31, "Hand Wager") << ": " << color_text(31, Rounded_Wager) << " , "
                << color_text(33, "Bank Total") << ": " << color_text(33, Bank_of_Player);
                // time_sleep(1.0);
            }
            else {}
        }
        else if (this->current_player.name == color_text(34, "Dealer")) {
            if (option == "") {
                if (dealer_show == "") {
                    option = "current";
                    cout << color_text(31, this->current_player.name) << "'s " << color_text(31, option)
                    << " hand: [Hidden, " << this->current_player.cards.back() << "]"
                    << color_text(36, " Hand Total") << ": "
                    << color_text(36, to_string(this->current_player.cards.back().card_value));
                    // time_sleep(1.0);
                }
                else if (dealer_show != "") {
                    option = "current";
                    cout << color_text(31, this->current_player.name) << "'s " << color_text(31, option)
                    << " hand: [";
                    for (int i = 0; i < this->current_player.cards.size(); i++) {
                        if (i == this->current_player.cards.size() - 1) {
                            cout << this->current_player.cards[i] << "]";
                        }
                        else {
                            cout << this->current_player.cards[i] << " , ";
                        }
                    }
                    Add_Hand_Total();
                    cout << color_text(36, " Hand Total") << ": "
                    << color_text(36, to_string(this->current_player.hand_cards_total));
                    // time_sleep(1.0);
                }
                else {}
            }
            else if (option != "") {
                if (dealer_show == "") {
                    cout << color_text(31, this->current_player.name) << "'s " << color_text(31, option)
                         << " hand: [Hidden, " << this->current_player.cards.back() << "]"
                         << color_text(36, " Hand Total") << ": "
                         << color_text(36, to_string(this->current_player.cards.back().card_value));
                    // time_sleep(1.0);
                }
                else if (dealer_show != "") {
                    cout << color_text(31, this->current_player.name) << "'s " << color_text(31, option)
                    << " hand: [";
                    for (int i = 0; i < this->current_player.cards.size(); i++) {
                        if (i == this->current_player.cards.size() - 1) {
                            cout << this->current_player.cards[i] << "]";
                        }
                        else {
                            cout << this->current_player.cards[i] << " , ";
                        }
                    }
                    Add_Hand_Total();
                    cout << color_text(36, " Hand Total") << ": "
                         << color_text(36, to_string(this->current_player.hand_cards_total));
                    // time_sleep(1.0);
                }
                else {}
            }
            else {}
        }
        else {}
    }
    // Update bank method
    float Update_Bank(string choice, float wager) {
        switch (choice[0]) {
            case 'W':
                current_player.bank_total += 2.0*wager;
                return current_player.bank_total;
            case 'L':
                return current_player.bank_total;
            case 'P':
                current_player.bank_total += wager;
                return current_player.bank_total;
            case 'B':
                current_player.bank_total += wager + 1.5*wager;
                return current_player.bank_total;
            default:
                current_player.bank_total += wager;
                return current_player.bank_total;
        }
    }
};
#endif //STAGE_1_STRUCTURE_H