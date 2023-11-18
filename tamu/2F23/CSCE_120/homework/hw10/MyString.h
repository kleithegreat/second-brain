#ifndef MYSTRING_H
#define MYSTRING_H

#include <iostream>
#include <limits>

class MyString {
    private:
        unsigned int _size;
        unsigned int _capacity;
        char* chars;

    public:
        size_t npos = static_cast<size_t>(-1);
        MyString(); // default
        MyString(const MyString& mystr); // copy
        MyString(const char* s); // from c-string
        ~MyString();
        void resize(size_t n);
        size_t capacity() const;
        size_t size() const;
        size_t length() const;
        const char* data() const;
        bool empty() const;
        const char& front() const;
        const char& at(size_t pos) const;
        void clear();
        friend std::ostream& operator<< (std::ostream& os, const MyString& mystr);
        MyString& operator= (const MyString& str);
        MyString& operator= (const char* s);
        MyString& operator= (const char c);
        MyString& operator+= (const MyString& str);
        MyString& operator+= (const char* s);
        MyString& operator+= (const char c);
        size_t find(const MyString& mystr, size_t pos = 0) const;
        size_t find(const char* s, size_t pos = 0) const;
        size_t find(const char* s, size_t pos, size_t n) const;
        size_t find(const char c, size_t pos = 0) const;
};

bool operator== (const MyString& lhs, const MyString& rhs);
bool operator== (const char* lhs, const MyString& rhs);
bool operator== (const MyString& lhs, const char* rhs);
MyString operator+ (const MyString& lhs, const MyString& rhs);

#endif