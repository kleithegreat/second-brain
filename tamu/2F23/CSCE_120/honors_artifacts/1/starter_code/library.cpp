#include "library.h"

// Method to add a book to the library
void Library::addBook(const Book &book) {
    books.push_back(book);
}

// Method to borrow a book based on its ISBN
bool Library::borrowBook(const std::string &ISBN) {
    for (Book &book : books) {
        if (book.getISBN() == ISBN && !book.getIsBorrowed()) {
            book.borrowBook();
            return true;
        }
    }
    return false;  // Book not found or already borrowed
}

// Method to return a book based on its ISBN
bool Library::returnBook(const std::string &ISBN) {
    for (Book &book : books) {
        if (book.getISBN() == ISBN && book.getIsBorrowed()) {
            book.returnBook();
            return true;
        }
    }
    return false;  // Book not found or not borrowed
}

// Method to search for a book by its title
Book* Library::searchBook(const std::string &title) {
    for (Book &book : books) {
        if (book.getTitle() == title) {
            return &book;
        }
    }
    return nullptr;  // Book not found
}
