#ifndef LINEARPROBING_H
#define LINEARPROBING_H

#include "AbstractHashTable.h"
#include <vector>

// Linear probing hash table class
class ProbingHashTable : public AbstractHashTable {
    private:
    std::vector<HashEntry> table;
    void resizeAndRehash();
    
    public: 
    ProbingHashTable();
    ~ProbingHashTable(); 
    int LinearProbe(string key) const;
    void insert(std::string key, int val); 
    int remove(std::string key); 
    int get(std::string key) const; 
    bool contains(std::string key) const;
};

///////////////////// TODO: FILL OUT THE FUNCTIONS /////////////////////

// constructor 
ProbingHashTable::ProbingHashTable(): AbstractHashTable() {
    maxLoadFactor = 0.5;
    table = std::vector<HashEntry>(capacity);
}

// destructor
ProbingHashTable::~ProbingHashTable() {

}

int ProbingHashTable::LinearProbe(string key) const {
    // if the key is already in the table, return the index
    // if the key is not in the table, return the index where the key should be inserted

    int index = hash(key);
    int originalIndex = index;

    int i = 0;
    while (i < capacity) {
        if (table[index].key == "" && !table[index].DELETED) {
            return index;
        }

        if (table[index].key == key && !table[index].DELETED) {
            return index;
        }

        index = (index + 1) % capacity;
        if (index == originalIndex) {
            return -1;
        }

        i++;
    }

    return -1;
}

// inserts the given string key
void ProbingHashTable::insert(std::string key, int val) {
    int index = LinearProbe(key);

    if (contains(key)) {
        table[index].val = val;
    } else {
        table[index] = HashEntry(key, val);
        num_elements++;
    }

    if (load_factor() > maxLoadFactor) {
        resizeAndRehash();
    }
}

// removes the given key from the hash table - if the key is not in the list, throw an error
int ProbingHashTable::remove(std::string key) {
    if (!contains(key)) {
        throw std::out_of_range("Key does not exist");
    }

    int index = LinearProbe(key);
    table[index].DELETED = true;
    table[index].key = "";
    num_elements--;

    return table[index].val;
}

// getter to obtain the value associated with the given key
int ProbingHashTable::get(std::string key) const {
    if (!contains(key)) {
        throw std::out_of_range("Key does not exist");
    }

    int index = LinearProbe(key);
    return table[index].val;
}

bool ProbingHashTable::contains(std::string key) const {
    if (table[LinearProbe(key)].key == key && !table[LinearProbe(key)].DELETED) {
        return true;
    }

    return false;
}

void ProbingHashTable::resizeAndRehash() {
    int oldCapacity = capacity;
    std::vector<HashEntry> oldTable = table;

    capacity = findNextPrime(capacity * 2);
    table = std::vector<HashEntry>(capacity);

    for (int i = 0; i < oldCapacity; i++) {
        if (oldTable[i].isFilled && !oldTable[i].DELETED && oldTable[i].key != "") {
            int index = LinearProbe(oldTable[i].key);
            table[index] = oldTable[i];
        }
    }
}

#endif