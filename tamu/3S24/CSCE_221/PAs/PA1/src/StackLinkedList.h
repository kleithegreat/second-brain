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
    head = nullptr;
    length = 0;
}

template <typename T>
StackLinkedList<T>::~StackLinkedList(){
    Node<T>* temp = head;
    while (temp != nullptr){
        Node<T>* next = temp->next;
        delete temp;
        temp = next;
    }

    head = nullptr;
    length = 0;
}

template <typename T>
StackLinkedList<T>::StackLinkedList(const StackLinkedList& other) {
    head = nullptr;
    length = 0;

    Node<T>* temp = other.head;
    Node<T>* last = nullptr;

    while (temp != nullptr){
        Node<T>* newNode = new Node<T>;
        newNode->data = temp->data;
        newNode->next = nullptr;

        if (last == nullptr){
            head = newNode;
        } else {
            last->next = newNode;
        }

        last = newNode;
        temp = temp->next;

        length++;
    }
}

template <typename T>
StackLinkedList<T>& StackLinkedList<T>::operator=(const StackLinkedList& other) {
    if (this != &other){
        Node<T>* temp = head;
        while (temp != nullptr){
            Node<T>* next = temp->next;
            delete temp;
            temp = next;
        }

        head = nullptr;
        length = 0;

        temp = other.head;
        Node<T>* last = nullptr;

        while (temp != nullptr){
            Node<T>* newNode = new Node<T>;
            newNode->data = temp->data;
            newNode->next = nullptr;

            if (last == nullptr){
                head = newNode;
            } else {
                last->next = newNode;
            }

            last = newNode;
            temp = temp->next;

            length++;
        }
    }

    return *this;
}

template <typename T>
bool StackLinkedList<T>::isEmpty(){
    return head == nullptr;
}

template <typename T>
int StackLinkedList<T>::size(){
    return length;
}

template <typename T>
T& StackLinkedList<T>::top(){
    if (this->isEmpty()) {
        throw std::out_of_range("Stack is empty");
    }

    return head->data;
}

template <typename T>
T StackLinkedList<T>::pop(){
    if (this->isEmpty()) {
        throw std::out_of_range("Stack is empty");
    }

    T temp = head->data;
    Node<T>* next = head->next;
    delete head;
    head = next;
    length--;
    return temp;
}

template <typename T>
void StackLinkedList<T>::push(const T& e){
    Node<T>* newNode = new Node<T>;
    newNode->data = e;
    newNode->next = head;
    head = newNode;
    length++;
}


#endif