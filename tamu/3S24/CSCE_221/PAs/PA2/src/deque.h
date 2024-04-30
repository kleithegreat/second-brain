#ifndef DEQUE_H
#define DEQUE_H

#include "node.h"
#include <stdexcept>
using namespace std;

template <class Type>
class Deque {
private:
	int s;
	Node<Type>* firstNode;
	Node<Type>* lastNode;

public:
	Deque();
	Deque(const Deque& other); 
	Deque& operator=(const Deque& other); 
	~Deque();
	bool isEmpty();
	int size();
	Type first();
	Type last();
	void insertFirst(Type o);
	void insertLast(Type o);
	Type removeFirst();
	Type removeLast();
};

template <class Type>
Deque<Type>::Deque() {
	s = 0;
	firstNode = nullptr;
	lastNode = nullptr;
}

template <class Type>
Deque<Type>::~Deque() {
	while (firstNode != nullptr) {
		Node<Type>* temp = firstNode;
		firstNode = firstNode->getNext();
		delete temp;
	}

	lastNode = nullptr;
	s = 0;
}

template <class Type>
Deque<Type>::Deque(const Deque& other) {
	s = 0;
	firstNode = nullptr;
	lastNode = nullptr;

	Node<Type>* temp = other.firstNode;
	while (temp != nullptr) {
		insertLast(temp->getData());
		temp = temp->getNext();
	}
}

template <class Type>
Deque<Type>& Deque<Type>::operator=(const Deque& other) {
	if (this != &other) {
		while (!this->isEmpty()) {
			removeFirst();
		}

		Node<Type>* temp = other.firstNode;
		while (temp != nullptr) {
			insertLast(temp->getData());
			temp = temp->getNext();
		}
	}

	return *this;
}

template <class Type>
bool Deque<Type>::isEmpty() {
	return s == 0;
}

template <class Type>
int Deque<Type>::size() {
	return s;
}

template <class Type>
Type Deque<Type>::first() {
	if (firstNode == nullptr) {
		return Type();
	} else {
		return firstNode->getData();
	}
}

template <class Type>
Type Deque<Type>::last() {
	if (lastNode == nullptr) {
		return Type();
	} else {
		return lastNode->getData();
	}
}

template <class Type>
void Deque<Type>::insertFirst(Type o) {
	if (firstNode == nullptr) {
		firstNode = new Node<Type>(o);
		lastNode = firstNode;
	} else {
		Node<Type>* newNode = new Node<Type>(o, firstNode, nullptr);
		firstNode->setPrev(newNode);
		firstNode = newNode;
	}

	s++;
}

template <class Type>
void Deque<Type>::insertLast(Type o) {
	if (firstNode == nullptr) {
		firstNode = new Node<Type>(o);
		lastNode = firstNode;
	} else {
		Node<Type>* newNode = new Node<Type>(o, nullptr, lastNode);
		lastNode->setNext(newNode);
		lastNode = newNode;
	}

	s++;
}

template <class Type>
Type Deque<Type>::removeFirst() {
	if (firstNode == nullptr) {
		throw std::out_of_range("Deque is empty");
	}

	Node<Type>* temp = firstNode;
	Type data = firstNode->getData();

	firstNode = firstNode->getNext();
	if (firstNode == nullptr) {
		lastNode = nullptr;
	} else {
		firstNode->setPrev(nullptr);
	}

	delete temp;
	s--;
	return data;
}

template <class Type>
Type Deque<Type>::removeLast() {
	if (lastNode == nullptr) {
		throw std::out_of_range("Deque is empty");
	}

	Node<Type>* temp = lastNode;
	Type data = lastNode->getData();

	lastNode = lastNode->getPrev();
	if (lastNode == nullptr) {
		firstNode = nullptr;
	} else {
		lastNode->setNext(nullptr);
	}

	delete temp;
	s--;
	return data;
}

#endif
