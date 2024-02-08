#ifndef DEQUE_H
#define DEQUE_H

#include "node.h"
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

// Your implementation here 

template <class Type>
Deque<Type>::Deque() {
}

template <class Type>
Deque<Type>::~Deque() {
}

template <class Type>
Deque<Type>::Deque(const Deque& other) {
}

template <class Type>
Deque<Type>& Deque<Type>::operator=(const Deque& other) {
	return *this;
}

template <class Type>
bool Deque<Type>::isEmpty() {
	return false;
}

template <class Type>
int Deque<Type>::size() {
	return -1;
}

template <class Type>
Type Deque<Type>::first() {
	return Type();
}

template <class Type>
Type Deque<Type>::last() {
	return Type();
}

template <class Type>
void Deque<Type>::insertFirst(Type o) {
}

template <class Type>
void Deque<Type>::insertLast(Type o) {
}

template <class Type>
Type Deque<Type>::removeFirst() {
	return Type();
}

template <class Type>
Type Deque<Type>::removeLast() {
	return Type();
}

#endif
