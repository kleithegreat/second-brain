#ifndef BOOK_H
#define BOOK_H

#include <string>

class Book {
private:
    std::string title;
    std::string author;
    std::string ISBN;
    bool isBorrowed;

public:
    // Constructor
    Book(std::string title, std::string author, std::string ISBN);

    // Getter methods
    std::string getTitle() const;
    std::string getAuthor() const;
    std::string getISBN() const;
    bool getIsBorrowed() const;

    // Setter methods
    void borrowBook();
    void returnBook();
};

#endif
