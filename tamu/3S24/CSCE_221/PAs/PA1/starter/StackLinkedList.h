#ifndef STACK_LinkedList_H
#define STACK_LinkedList_H
#include "AbstractStack.h"

template <typename T>
class Node {
public:
    T data;
    Node<T>* next;
};

template <typename T>
class StackLinkedList : public AbstractStack<T>{
private:
    Node<T>* head;
    int length;
public:
    StackLinkedList();

    ~StackLinkedList();

    StackLinkedList(const StackLinkedList& other);

    StackLinkedList& operator=(const StackLinkedList& other);

    bool isEmpty();

    int size();

    T& top();

    T pop();

    void push(const T& e);

};

// Your implementation here
template <typename T>
StackLinkedList<T>::StackLinkedList(){
}

template <typename T>
StackLinkedList<T>::~StackLinkedList(){
}

template <typename T>
StackLinkedList<T>::StackLinkedList(const StackLinkedList& other) {
}

template <typename T>
StackLinkedList<T>& StackLinkedList<T>::operator=(const StackLinkedList& other) {
    return *this;
}

template <typename T>
bool StackLinkedList<T>::isEmpty(){
    return true;
}

template <typename T>
int StackLinkedList<T>::size(){
    return -1;
}

template <typename T>
T& StackLinkedList<T>::top(){
    static int temp = -1;
    return temp;
}

template <typename T>
T StackLinkedList<T>::pop(){
    return -1;
}

template <typename T>
void StackLinkedList<T>::push(const T& e){
}


#endif