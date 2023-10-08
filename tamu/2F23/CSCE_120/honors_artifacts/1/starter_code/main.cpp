#include <iostream>
#include "book.h"
#include "library.h"

using namespace std;

void displayMenu() {
    cout << "\nLibrary System Menu:\n";
    cout << "1. Add a book\n";
    cout << "2. Borrow a book\n";
    cout << "3. Return a book\n";
    cout << "4. Search for a book\n";
    cout << "5. Exit\n";
    cout << "Enter your choice: ";
}

int main() {
    Library library;
    int choice;

    do {
        displayMenu();
        cin >> choice;

        string title, author, ISBN;
        Book* book;

        switch (choice) {
            case 1:
                cout << "Enter book title: ";
                cin.ignore();
                getline(cin, title);
                cout << "Enter book author: ";
                getline(cin, author);
                cout << "Enter book ISBN: ";
                cin >> ISBN;
                library.addBook(Book(title, author, ISBN));
                cout << "Book added successfully!\n";
                break;

            case 2:
                cout << "Enter ISBN of the book to borrow: ";
                cin >> ISBN;
                if (library.borrowBook(ISBN)) {
                    cout << "Book borrowed successfully!\n";
                } else {
                    cout << "Failed to borrow the book.\n";
                }
                break;

            case 3:
                cout << "Enter ISBN of the book to return: ";
                cin >> ISBN;
                if (library.returnBook(ISBN)) {
                    cout << "Book returned successfully!\n";
                } else {
                    cout << "Failed to return the book.\n";
                }
                break;

            case 4:
                cout << "Enter title of the book to search: ";
                cin.ignore();
                getline(cin, title);
                book = library.searchBook(title);
                if (book) {
                    cout << "Book found: " << book->getTitle() << " by " << book->getAuthor() << "\n";
                } else {
                    cout << "Book not found.\n";
                }
                break;

            case 5:
                cout << "Exiting the program.\n";
                break;

            default:
                cout << "Invalid choice. Please try again.\n";
                break;
        }

    } while (choice != 5);

    return 0;
}
