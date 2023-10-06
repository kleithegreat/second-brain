#include "book.h"

// Constructor implementation
Book::Book(std::string title, std::string author, std::string ISBN) : 
    title(title), author(author), ISBN(ISBN), isBorrowed(false) {}

// Getter methods implementation
std::string Book::getTitle() const {
    return title;
}

std::string Book::getAuthor() const {
    return author;
}

std::string Book::getISBN() const {
    return ISBN;
}

bool Book::getIsBorrowed() const {
    return isBorrowed;
}

// Setter methods implementation
void Book::borrowBook() {
    isBorrowed = true;
}

void Book::returnBook() {
    isBorrowed = false;
}
