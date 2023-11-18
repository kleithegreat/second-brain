# include <string>
# include "Node.h"

using std::string;

Node::Node() : data(TemperatureData()), next(nullptr) {}

Node::Node(string id, int year, int month, double temperature)
	: data(TemperatureData(id, year, month, temperature)), next(nullptr) {}

Node::Node(const Node& other) : data(other.data), next(other.next) {}

Node& Node::operator=(const Node& other) {
	if (this == &other) {
		return *this;
	}

	this->data = other.data;
	this->next = other.next;

	return *this;
}

bool Node::operator<(const Node& b) {	
	return this->data < b.data;
}
