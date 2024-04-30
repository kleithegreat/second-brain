#ifndef SKIPLIST_H
#define SKIPLIST_H

#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

class Node {
public:
    int key;
    std::vector<Node*> forward;

    Node(int key, int level) : key(key), forward(level + 1, nullptr) {}
};

class SkipList {
private: 
    double P;
    int MAXLVL;
    Node* header;
    int level;

public:
    SkipList(int max_lvl, double p);
    ~SkipList();
    int randomLevel();
    void insertElement(int key);
    void deleteElement(int search_key);
    bool searchElement(int key);
    void displayList();
};


SkipList::SkipList(int max_lvl, double p) : MAXLVL(max_lvl), P(p), level(0) {
    header = new Node(-1, MAXLVL);
}

SkipList::~SkipList() {
    Node* current = header->forward[0];
    while (current != nullptr) {
        Node* temp = current;
        current = current->forward[0];
        delete temp;
    }
    delete header;
}

int SkipList::randomLevel() {
    int level = 0;
    while (rand() / double(RAND_MAX) < P && level < MAXLVL) {
        level++;
    }
    return level;
}

void SkipList::insertElement(int key) {
    std::vector<Node*> update(MAXLVL + 1);
    Node* current = header;

    for (int i = level; i >= 0; i--) {
        while (current->forward[i] != nullptr && current->forward[i]->key < key)
            current = current->forward[i];
        update[i] = current;
    }

    current = current->forward[0];

    if (current == nullptr || current->key != key) {
        int rlevel = randomLevel();

        if (rlevel > level) {
            for (int i = level + 1; i <= rlevel; i++)
                update[i] = header;
            level = rlevel;
        }

        Node* n = new Node(key, rlevel);

        for (int i = 0; i <= rlevel; i++) {
            n->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = n;
        }
    }
}

void SkipList::deleteElement(int search_key) {
    std::vector<Node*> update(MAXLVL + 1);
    Node* current = header;

    for (int i = level; i >= 0; i--) {
        while (current->forward[i] != nullptr && current->forward[i]->key < search_key)
            current = current->forward[i];
        update[i] = current;
    }

    current = current->forward[0];

    if (current != nullptr && current->key == search_key) {
        for (int i = 0; i <= level; i++) {
            if (update[i]->forward[i] != current)
                break;
            update[i]->forward[i] = current->forward[i];
        }

        while (level > 0 && header->forward[level] == nullptr)
            level--;

        delete current;
    }
}

bool SkipList::searchElement(int key) {
    Node* current = header;

    for (int i = level; i >= 0; i--) {
        while (current->forward[i] != nullptr && current->forward[i]->key < key) {
            current = current->forward[i];
        }
    }

    current = current->forward[0];

    return current != nullptr && current->key == key;
}

void SkipList::displayList() {
    std::cout << "\n*****Skip List******" << std::endl;
    Node* head = header;
    for (int lvl = 0; lvl <= level; lvl++) {
        std::cout << "Level " << lvl << ": ";
        Node* node = head->forward[lvl];
        while (node != nullptr) {
            std::cout << node->key << " ";
            node = node->forward[lvl];
        }
        std::cout << std::endl;
    }
}

#endif