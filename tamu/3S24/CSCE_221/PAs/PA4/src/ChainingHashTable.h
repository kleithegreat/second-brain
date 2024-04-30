#ifndef CHAINING_H
#define CHAINING_H

#include "AbstractHashTable.h"
#include <vector>
#include <list>


// Chaining hash table class
class ChainingHashTable: public AbstractHashTable {
    private:
    std::vector<std::list<HashEntry>> table;
    void resizeAndRehash();

    public: 
    ChainingHashTable();
    ~ChainingHashTable(); 
    void insert(std::string key, const int val); 
    int remove(std::string key); 
    int get(std::string key) const;
    bool contains(std::string key) const;
    std::string getName() const { return "Chaining"; };
};


///////////////////// TODO: FILL OUT THE FUNCTIONS /////////////////////

// constructor
ChainingHashTable::ChainingHashTable(): AbstractHashTable() {
    maxLoadFactor = 1;
    table = std::vector<std::list<HashEntry>>(capacity);
}

// destructor
ChainingHashTable::~ChainingHashTable() {
    maxLoadFactor = 0.9;
    table = std::vector<std::list<HashEntry>>(capacity);
}

// inserts the given string key
void ChainingHashTable::insert(std::string key, int val) {
	int index = hash(key);
    
    for (auto it = table[index].begin(); it != table[index].end(); it++) {
        if (it->key == key) {
            it->val = val;
            return;
        }
    }

    table[index].push_back(HashEntry(key, val));
    num_elements++;

    if (load_factor() > maxLoadFactor) {
        resizeAndRehash();
    }
}

// removes the given key from the hash table - if the key is not in the list, throw an error
int ChainingHashTable::remove(std::string key) {
    if (!contains(key)) {
        throw std::out_of_range("Key does not exist in the hash table");
    }

    int index = hash(key);

    for (auto it = table[index].begin(); it != table[index].end(); it++) {
        if (it->key == key) {
            int val = it->val;
            table[index].erase(it);
            num_elements--;
            return val;
        }
    }

    throw std::out_of_range("Key does not exist in the hash table");
}

// getter to obtain the value associated with the given key
int ChainingHashTable::get(std::string key) const {
    int index = hash(key);

    for (auto it = table[index].begin(); it != table[index].end(); it++) {
        if (it->key == key) {
            return it->val;
        }
    }

    throw std::out_of_range("Key does not exist in the hash table");
}

bool ChainingHashTable::contains(const std::string key) const {
    int index = hash(key);

    for (auto it = table[index].begin(); it != table[index].end(); it++) {
        if (it->key == key) {
            return true;
        }
    }

    return false;
}

void ChainingHashTable::resizeAndRehash() {
    int newCapacity = findNextPrime(2 * capacity);
    int oldCapacity = capacity;
    capacity = newCapacity;

    std::vector<std::list<HashEntry>> newTable(newCapacity);

    for (int i = 0; i < oldCapacity; i++) {
        for (auto it = table[i].begin(); it != table[i].end(); it++) {
            int index = hash(it->key);
            newTable[index].push_back(*it);
        }
    }

    table = newTable;    
}

#endif