#include "TemperatureData.h"
using std::string;

TemperatureData::TemperatureData() : id(""), year(0), month(0), temperature(0.0) {}

TemperatureData::TemperatureData(string id, int year, int month, double temperature)
	: id(id), year(year), month(month), temperature(temperature) {}

TemperatureData::~TemperatureData() {}

bool TemperatureData::operator<(const TemperatureData& b) {
	if (this->id < b.id) {
		return true;
	} else if (this->id == b.id) {
		if (this->year < b.year) {
			return true;
		} else if (this->year == b.year) {
			if (this->month < b.month) {
				return true;
			} else if (this->month == b.month) {
				if (this->temperature < b.temperature) {
					return true;
				}
			}
		}
	}
	return false;
}
