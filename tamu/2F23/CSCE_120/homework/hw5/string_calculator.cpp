#include <iostream>
#include <string>
#include "./string_calculator.h"
#include <sstream>
#include <limits>

using std::cout;
using std::endl;
using std::string;

unsigned int digit_to_decimal(char digit) {
    if (digit < '0' || digit > '9') {
        throw std::invalid_argument("Invalid digit");
    }
    return digit - '0';
}

char decimal_to_digit(unsigned int decimal) {
    if (decimal > 9) {
        throw std::invalid_argument("Invalid decimal");
    }
    return '0' + decimal;
}

string trim_leading_zeros(string num) {
    size_t index = 0;
    while (index < num.length() && num[index] == '0') {
        index++;
    }
    return (index == num.length()) ? "0" : num.substr(index);
}

string add(string lhs, string rhs) {
    string result;
    int carry = 0;
    int lhsIndex = lhs.size() - 1;
    int rhsIndex = rhs.size() - 1;

    while (lhsIndex >= 0 || rhsIndex >= 0 || carry > 0) {
        int lhsVal = lhsIndex >= 0 ? lhs[lhsIndex] - '0' : 0;
        int rhsVal = rhsIndex >= 0 ? rhs[rhsIndex] - '0' : 0;

        int sum = lhsVal + rhsVal + carry;
        result = decimal_to_digit(sum % 10) + result;

        carry = sum / 10;

        lhsIndex--;
        rhsIndex--;
    }

    return trim_leading_zeros(result);
}

string multiply(string lhs, string rhs) {
    if (lhs.empty() || rhs.empty()) return "0";

    int lhsSize = lhs.size();
    int rhsSize = rhs.size();
    string result(lhsSize + rhsSize, '0');

    for (int i = lhsSize - 1; i >= 0; i--) {
    int carry = 0;
    for (int j = rhsSize - 1; j >= 0; j--) {
        int temp = (result[i + j + 1] - '0') + (lhs[i] - '0') * (rhs[j] - '0') + carry;
        carry = temp / 10;
        result[i + j + 1] = '0' + temp % 10;
    }
    int pos = i;
    while (carry > 0) {
        int current = result[pos] - '0' + carry;
        result[pos] = '0' + current % 10;
        carry = current / 10;
        pos--;
    }
}


    return trim_leading_zeros(result);
}
