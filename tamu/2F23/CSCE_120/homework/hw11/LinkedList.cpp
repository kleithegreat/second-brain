# include <iostream>
# include <string>
# include "LinkedList.h"
# include "Node.h"

using std::string, std::ostream;

LinkedList::LinkedList() : head(nullptr), tail(nullptr) {}

LinkedList::~LinkedList() {
	Node* current = head;

	while (current != nullptr) {
		Node* next = current->next;
		delete current;
		current = next;
	}

	head = nullptr;
	tail = nullptr;
}

LinkedList::LinkedList(const LinkedList& source) : head(nullptr), tail(nullptr) {
	Node* current = source.head;
	while (current != nullptr) {
		insert(current->data.id, current->data.year, current->data.month, current->data.temperature);
		current = current->next;
	}
}

LinkedList& LinkedList::operator=(const LinkedList& source) {
	if (this == &source) {
		return *this;
	}

	this->clear();
	Node* current = source.head;

	while (current != nullptr) {
		this->insert(current->data.id, current->data.year, current->data.month, current->data.temperature);
		current = current->next;
	}

	return *this;
}

void LinkedList::insert(string location, int year, int month, double temperature) {
	Node* newNode = new Node(location, year, month, temperature);
	if (head == nullptr || *newNode < *head) {
		newNode->next = head;
		head = newNode;
		
		if (tail == nullptr) {
			tail = newNode;
		}
	} else {
		Node* current = head;

		while (current->next != nullptr && !(*newNode < *current->next)) {
			current = current->next;
		}

		newNode->next = current->next;
		current->next = newNode;

		if (tail == current) {
			tail = newNode;
		}
	}
}

void LinkedList::clear() {
	Node* current = head;

	while (current != nullptr) {
		Node* next = current->next;
		delete current;
		current = next;
	}

	head = nullptr;
	tail = nullptr;
}

Node* LinkedList::getHead() const {
	return head;
}

string LinkedList::print() const {
    string outputString;
    Node* current = head;

    while (current != nullptr) {
        outputString += current->data.id + " " 
                        + std::to_string(current->data.year) + " " 
                        + std::to_string(current->data.month) + " ";

        string tempStr = std::to_string(current->data.temperature);

        size_t decimalPos = tempStr.find('.');
        if (decimalPos != string::npos) {
            size_t end = tempStr.length() - 1;
            while (end > decimalPos && tempStr[end] == '0') {
                end--;
            }

            if (end == decimalPos) {
                end--;
            }

            tempStr = tempStr.substr(0, end + 1);
        }

        outputString += tempStr + "\n";
        current = current->next;
    }

    return outputString;
}

ostream& operator<<(ostream& os, const LinkedList& ll) {
	os << ll.print();
	return os;
}
