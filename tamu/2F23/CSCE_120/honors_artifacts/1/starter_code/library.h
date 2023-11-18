#ifndef LIBRARY_H
#define LIBRARY_H

#include <vector>
#include "book.h"

class Library {
private:
    std::vector<Book> books;

public:
    // Method to add a book to the library
    void addBook(const Book &book);

    // Method to borrow a book based on its ISBN
    bool borrowBook(const std::string &ISBN);

    // Method to return a book based on its ISBN
    bool returnBook(const std::string &ISBN);

    // Method to search for a book by its title
    Book* searchBook(const std::string &title);
};

#endif
