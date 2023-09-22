#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::cin;
using std::endl;

int rollDice();
int doGame(int,int);

int main() {
    int seed;
    while (!(cin >> seed)) {
        cin.clear();
        cin.ignore(10000, '\n');
    }
    srand(seed);
    
    int wallet = 1000;
    bool gameOver = false;

    while (!gameOver) {
        cout << "Enter amount to bet. You have $" << wallet << endl;
        std::string betStr;
        getline(cin, betStr);

        if (betStr.empty()) {
            continue;
        }

        int bet = 0;
        try {
            long long tempBet = std::stoll(betStr);
            if (tempBet > 2147483647 || tempBet <= 0) {
                throw std::out_of_range("Out of range");
            }
            bet = static_cast<int>(tempBet);
        } catch (const std::out_of_range& e) {
            cout << "Invalid bet amount." << endl;
            continue;
        } catch (const std::exception&) {
            cout << "Please enter a valid number." << endl;
            continue;
        }

        if (bet > wallet) {
            cout << "You don't have that much money." << endl;
            continue;
        }

        wallet = doGame(bet, wallet);

        if (wallet == 0) {
            cout << "You are penniless. Thanks for playing." << endl;
            gameOver = true;
        } else {
            while (true) {
                cout << "Play again? (y/n)" << endl;
                char c;
                cin >> c;
                cin.ignore();

                if (c == 'n') {
                    gameOver = true;
                    break;
                } else if (c == 'y') {
                    break;
                } else {
                    cout << "Invalid choice. Please enter 'y' or 'n'." << endl;
                }
            }
        }
    }
    cout << "You ended the game with $" << wallet << endl;
}

int rollDice() {
    return (rand() % 6 + 1) + (rand() % 6 + 1);
}

int doGame(int bet, int wallet) {
    int roll = rollDice();
    cout << "You rolled " << roll << endl;

    switch (roll) {
        case 7:
        case 11:
            cout << "You win!" << endl;
            wallet += bet;
            break;
        case 2:
        case 3:
        case 12:
            cout << "You lose." << endl;
            wallet -= bet;
            break;
        default:
            int point = roll;
            cout << "The point is " << point << endl;
            do {
                roll = rollDice();
                cout << "You rolled " << roll << endl;
                if (roll == 7) {
                    cout << "You lose." << endl;
                    wallet -= bet;
                    break;
                } else if (roll == point) {
                    cout << "That matches the point!" << " You win!" << endl;
                    wallet += bet;
                    break;
                }
            } while (true);
    }
    return wallet;
}
