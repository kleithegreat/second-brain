#include <iostream>
#include <string>
#include <limits>
#include "./string_calculator.h"

using std::cout;
using std::endl;
using std::cin;
using std::string;

string strip_spaces(const string& str) {
    string result;
    for (char c : str) {
        if (c != ' ') {
            result.push_back(c);
        }
    }
    return result;
}

int main() {
    cout << "String Calculator" << endl;
    cout << "\"q\" or \"quit\" or ctrl+d to exit" << endl;

    string input;

    while (true) {
        cout << ">> ";
        getline(cin, input);

        input = strip_spaces(input);

        if (cin.eof() || input == "q" || input == "quit") {
            cout << endl << "farvel!" << endl << endl;
            break;
        }

        size_t plusPos = input.find('+');
        size_t multiplyPos = input.find('*');

        string lhs, rhs, result;

        if (plusPos != string::npos) {
            lhs = trim_leading_zeros(input.substr(0, plusPos));
            rhs = trim_leading_zeros(input.substr(plusPos + 1));
            result = add(lhs, rhs);
        } else if (multiplyPos != string::npos) {
            lhs = trim_leading_zeros(input.substr(0, multiplyPos));
            rhs = trim_leading_zeros(input.substr(multiplyPos + 1));
            result = multiply(lhs, rhs);
        } else {
            cout << "Invalid operation. Please use '+' or '*'." << endl;
            continue;
        }

        cout << endl << "ans =" << endl << endl;
        cout << "    " << result << endl << endl;
    }

    return 0;
}
