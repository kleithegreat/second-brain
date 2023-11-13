#include <iostream>
#include <limits>
#include "MyString.h"

MyString::MyString() : chars(nullptr), _size(0), _capacity(0) {}

MyString::MyString(const MyString& mystr) {
    _size = mystr._size;
    _capacity = mystr._capacity;
    chars = new char[_capacity];
    for (int i = 0; i < _size; i++) {
        chars[i] = mystr.chars[i];
    }
}

MyString::MyString(const char* s) {
    _size = 0;
    while(s[_size] != '\0') {
        _size++;
    }
    _capacity = _size + 1;
    chars = new char[_capacity];
    for (int i = 0; i < _size; i++) {
        chars[i] = s[i];
    }
}

MyString::~MyString() {
    delete[] chars;
}

void MyString::resize(unsigned int n) {
    if (n > _capacity) {
        _capacity = n + 1;
        char* newChars = new char[_capacity];
        if (chars != nullptr) {
            for (int i = 0; i < _size; i++) {
                newChars[i] = chars[i];
            }
            delete[] chars;
        }
        chars = newChars;
    }
    _size = n;
    chars[_size] = '\0';
}

unsigned int MyString::capacity() const {
    return _capacity;
}

unsigned int MyString::size() const {
    return _size;
}

unsigned int MyString::length() const {
    return _size;
}

const char* MyString::data() const {
    return chars;
}

bool MyString::empty() const {
    return _size == 0;
}

const char& MyString::front() const {
    if (empty()) throw std::out_of_range("String is empty");
    return chars[0];
}

const char& MyString::at(unsigned int pos) const {
    if (pos >= _size) throw std::out_of_range("Index out of bounds");
    return chars[pos];
}

void MyString::clear() {
    _size = 0;
    chars[0] = '\0';
}

ostream& operator<< (ostream& os, const MyString& mystr) {
    os << mystr.chars;
    return os;
}

MyString& MyString::operator= (const MyString& str) {
    if (this != &str) {
        delete[] chars;
        _size = str._size;
        _capacity = str._capacity;
        chars = new char[_capacity];
        for (int i = 0; i < _size; i++) {
            chars[i] = str.chars[i];
        }
    }
    return *this;
}

MyString& MyString::operator= (const char* s) {
    delete[] chars;
    _size = 0;
    while(s[_size] != '\0') {
        _size++;
    }
    _capacity = _size + 1;
    chars = new char[_capacity];
    for (int i = 0; i < _size; i++) {
        chars[i] = s[i];
    }
    return *this;
}

MyString& MyString::operator= (const char c) {
    delete[] chars;
    _size = 1;
    _capacity = 2;
    chars = new char[_capacity];
    chars[0] = c;
    chars[1] = '\0';
    return *this;
}

MyString& MyString::operator+= (const MyString& str) {
    unsigned int new_size = _size + str._size;
    if (new_size >= _capacity) {
        resize(new_size);
    }

    for (unsigned int i = 0; i < str._size; ++i) {
        chars[_size + i] = str.chars[i];
    }

    _size = new_size;
    chars[_size] = '\0';
    return *this;
}

MyString& MyString::operator+= (const char* s) {
    unsigned int s_length = 0;
    while (s[s_length] != '\0') {
        s_length++;
    }

    unsigned int new_size = _size + s_length;
    if (new_size >= _capacity) {
        resize(new_size);
    }

    for (unsigned int i = 0; i < s_length; ++i) {
        chars[_size + i] = s[i];
    }

    _size = new_size;
    chars[_size] = '\0';
    return *this;
}

MyString& MyString::operator+= (const char c) {
    if (_size + 1 >= _capacity) {
        resize(_size + 1);
    }

    chars[_size] = c;
    _size++;
    chars[_size] = '\0';
    return *this;
}

unsigned int MyString::find(const MyString& mystr, unsigned int pos) const {
    return find(mystr.chars, pos);
}

unsigned int MyString::find(const char* s, unsigned int pos) const {
    for (unsigned int i = pos; i < _size; ++i) {
        bool found = true;
        for (unsigned int j = 0; s[j] != '\0'; ++j) {
            if (i + j >= _size || chars[i + j] != s[j]) {
                found = false;
                break;
            }
        }
        if (found) {
            return i;
        }
    }
    return std::numeric_limits<unsigned int>::max();
}

unsigned int MyString::find(const char* s, unsigned int pos, unsigned int n) const {
    for (unsigned int i = pos; i < _size; ++i) {
        bool found = true;
        for (unsigned int j = 0; j < n; ++j) {
            if (i + j >= _size || chars[i + j] != s[j]) {
                found = false;
                break;
            }
        }
        if (found) {
            return i;
        }
    }
    return std::numeric_limits<unsigned int>::max();
}

unsigned int MyString::find(const char c, unsigned int pos) const {
    for (unsigned int i = pos; i < _size; ++i) {
        if (chars[i] == c) {
            return i;
        }
    }
    return std::numeric_limits<unsigned int>::max();
}
