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
        static const unsigned int npos = std::numeric_limits<unsigned int>::max();
        MyString(); // default
        MyString(const MyString& mystr); // copy
        MyString(const char* s); // from c-string
        ~MyString();
        void resize(unsigned int n);
        unsigned int capacity() const;
        unsigned int size() const;
        unsigned int length() const;
        const char* data() const;
        bool empty() const;
        const char& front() const;
        const char& at(unsigned int pos) const;
        void clear();
        friend std::ostream& operator<< (std::ostream& os, const MyString& mystr);
        MyString& operator= (const MyString& str);
        MyString& operator= (const char* s);
        MyString& operator= (const char c);
        MyString& operator+= (const MyString& str);
        MyString& operator+= (const char* s);
        MyString& operator+= (const char c);
        unsigned int find(const MyString& mystr, unsigned int pos = 0) const;
        unsigned int find(const char* s, unsigned int pos = 0) const;
        unsigned int find(const char* s, unsigned int pos, unsigned int n) const;
        unsigned int find(const char c, unsigned int pos = 0) const;
};

#endif