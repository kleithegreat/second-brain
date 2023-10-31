#include "Complex.h"
#include <sstream>
#include <string>

double Complex::getReal() { return real; }
double Complex::getImaginary() {return imag; }
void Complex::setReal(double real) { this->real = real; }
void Complex::setImaginary(double imaginary) { this->imag = imaginary; }
std::string Complex::to_string() {
  std::ostringstream oss;
  oss << real;
  if (imag < 0) { // negative imag
    oss << " - " << (-1*imag);
  }
  else {
    oss << " + " << imag;
  }
  oss << "i";
  return oss.str();
}

Complex Complex::operator=(Complex rhs) {
  this->real = rhs.real;
  this->imag = rhs.imag;
  return *this;
}

Complex Complex::operator==(Complex rhs) {
  return (this->real == rhs.real && this->imag == rhs.imag);
}

Complex Complex::operator+(Complex rhs) {
  Complex result;
  result.real = this->real + rhs.real;
  result.imag = this->imag + rhs.imag;
  return result;
}

Complex Complex::operator-(Complex rhs) {
  Complex result;
  result.real = this->real - rhs.real;
  result.imag = this->imag - rhs.imag;
  return result;
}