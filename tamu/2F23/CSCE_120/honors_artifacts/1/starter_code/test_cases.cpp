#include <iostream>
#include "book.h"
#include "library.h"

using namespace std;

void testBookClass() {
    Book book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565");

    // Test constructor and getter methods
    assert(book.getTitle() == "The Great Gatsby");
    assert(book.getAuthor() == "F. Scott Fitzgerald");
    assert(book.getISBN() == "9780743273565");
    assert(book.getIsBorrowed() == false);

    // Test borrowBook and returnBook methods
    book.borrowBook();
    assert(book.getIsBorrowed() == true);
    book.returnBook();
    assert(book.getIsBorrowed() == false);

    cout << "All Book class tests passed!" << endl;
}

void testLibraryClass() {
    Library library;
    Book book1("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565");

    // Test adding and searching for a book
    library.addBook(book1);
    assert(library.searchBook("The Great Gatsby") != nullptr);
    assert(library.searchBook("Unknown Book") == nullptr);

    // Test borrowing and returning books
    assert(library.borrowBook("9780743273565") == true);  // Book exists and is available
    assert(library.borrowBook("9780743273565") == false); // Book exists but is borrowed
    assert(library.borrowBook("1234567890123") == false); // Book doesn't exist

    assert(library.returnBook("9780743273565") == true);  // Book was borrowed
    assert(library.returnBook("9780743273565") == false); // Book was not borrowed

    cout << "All Library class tests passed!" << endl;
}

int main() {
    testBookClass();
    testLibraryClass();

    cout << "All tests passed successfully!" << endl;
    return 0;
}
