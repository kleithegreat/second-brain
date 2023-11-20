#include "TemperatureDatabase.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

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
	ifstream file(filename);
	ofstream results("result.dat");

	if (!file.is_open()) {
		cout << "Error: Unable to open " << filename << endl;
		exit(1);
	}

	string line;
	while (getline(file, line)) {
		std::istringstream iss(line);

		string id;
		string query;
		int yearStart;
		int yearEnd;

		if (!(iss >> id >> query >> yearStart >> yearEnd)) {
			cout << "Error: Other invalid query" << endl;
			continue;
		}

		if (query != "AVG" && query != "MODE") {
			cout << "Error: Unsupported query " << query << endl;
			continue;
		}

		if (yearStart < 1800 || yearEnd > 2023 || yearStart > yearEnd) {
			cout << "Error: Invalid range " << yearStart << "-" << yearEnd << endl;
			continue;
		}

		string value;

		if (query == "AVG") {
			std::vector<double> total;
			Node* current = records.getHead();

			while (current != nullptr) {
				total.push_back(current->data.temperature);
			}

			double sum = 0;
			for (size_t i = 0; i < total.size(); i++) {
				sum += total[i];
			}

			if (total.size() == 0) {
				value = "unknown";
			} else {
				double average = sum / total.size();
				value = std::to_string(average);
			}
		} else {
			std::vector<int> frequencies(101);
			Node* current = records.getHead();

			while (current != nullptr) {
				int rounded;

				int integerPart = static_cast<int>(current->data.temperature);
				double fractionalPart = current->data.temperature - integerPart;

				if (current->data.temperature >= 0) {
					rounded = (fractionalPart >= 0.5) ? (integerPart + 1) : integerPart;
				} else {
					rounded = (fractionalPart <= -0.5) ? (integerPart - 1) : integerPart;
				}

				int index = rounded + 50;
				frequencies[index]++;

				current = current->next;
			}

			int max = 0;
			int maxIndex = 0;
			for (size_t i = 0; i < frequencies.size(); i++) {
				if (frequencies[i] > max) {
					max = frequencies[i];
					maxIndex = i;
				}
			}

			if (max == 0) {
				value = "unknown";
			} else {
				double mode = maxIndex - 50;
				value = std::to_string(mode);
			}
		}

		results << id << " " << yearStart << " " << yearEnd << " " << query << " " << value << endl;
	}

	file.close();
	results.close();
}
