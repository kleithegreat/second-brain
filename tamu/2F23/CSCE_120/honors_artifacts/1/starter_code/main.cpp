#include <iostream>
#include "book.h"
#include "library.h"

using namespace std;

int main() {
    Library library;

    // Sample books for testing
    Book book1("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565");
    Book book2("To Kill a Mockingbird", "Harper Lee", "9780061120084");
    Book book3("1984", "George Orwell", "9780451524935");

    // Adding books to the library
    library.addBook(book1);
    library.addBook(book2);
    library.addBook(book3);

    // Sample interface for interaction
    cout << "Books added to the library!" << endl;
    cout << "Borrowing 'The Great Gatsby'..." << endl;
    if (library.borrowBook("9780743273565")) {
        cout << "'The Great Gatsby' borrowed successfully!" << endl;
    } else {
        cout << "Failed to borrow 'The Great Gatsby'." << endl;
    }

    cout << "Searching for '1984'..." << endl;
    Book* searchedBook = library.searchBook("1984");
    if (searchedBook) {
        cout << "'1984' by " << searchedBook->getAuthor() << " found in the library!" << endl;
    } else {
        cout << "'1984' not found in the library." << endl;
    }

    return 0;
}
