#include "TemperatureDatabase.h"
#include <iostream>
#include <fstream>
#include <sstream>

using std::cout, std::endl, std::string, std::ofstream, std::ifstream;

TemperatureDatabase::TemperatureDatabase() : records(LinkedList()) {}
TemperatureDatabase::~TemperatureDatabase() {}

void TemperatureDatabase::loadData(const string& filename) {
	ifstream file(filename);

	if (!file.is_open()) {
		cout << "Error: Unable to open " << filename << endl;
		exit(1);
	}

	string line;
	while (getline(file, line)) {
		std::istringstream iss(line);

		string id;
		int year;
		int month;
		double temperature;

		if (!(iss >> id >> year >> month >> temperature)) {
            cout << "Error: Other invalid input" << endl;
            continue;
        }

        if (temperature < -50 || temperature > 50) {
            cout << "Error: Invalid temperature " << temperature << endl;
            continue;
        }

        if (year < 1800 || year > 2023) {
            cout << "Error: Invalid year " << year << endl;
            continue;
        }

        if (month < 1 || month > 12) {
            cout << "Error: Invalid month " << month << endl;
            continue;
        }

        records.insert(id, year, month, temperature);
	}

	file.close();
}

void TemperatureDatabase::outputData(const string& filename) {
	ofstream dataout("sorted." + filename);
	
	if (!dataout.is_open()) {
		cout << "Error: Unable to open " << filename << endl;
		exit(1);
	}

	dataout << records.print();
}

void TemperatureDatabase::performQuery(const string& filename) {
	// TODO: implement this function
}
