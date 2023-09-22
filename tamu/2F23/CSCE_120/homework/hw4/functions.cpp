#include <stdexcept>
#include <limits>

int Largest(int a, int b, int c) {
  int d = a;

  if (b > d) {
    d = b;
  }

  if (c > d) {
    d = c;
  }

  return d;
}


bool SumIsEven(int a, int b) {
  if ((a + b) % 2) {
    return false;
  }
  return true;
}


int BoxesNeeded(int apples) {
    if (apples <= 0) {
        return 0;
    }

    if (apples % 20 == 0) {
        return apples / 20;
    } else {
        return (apples / 20) + 1;
    }
}


bool SmarterSection(int A_correct, int A_total, int B_correct, int B_total) {
    if (A_total <= 0 || B_total <= 0 || A_correct < 0 || B_correct < 0 || A_correct > A_total || B_correct > B_total) {
        throw std::invalid_argument("Invalid arguments.");
    }
    double aPercentage = static_cast<double>(A_correct) / A_total;
    double bPercentage = static_cast<double>(B_correct) / B_total;

    return aPercentage > bPercentage;
}


bool GoodDinner(int pizzas, bool is_weekend) {
  if (is_weekend && pizzas >= 10) {
    return true;
  }
  
  if (pizzas >= 10 && pizzas <= 20) {
    return true;
  }

  return false;
}


int SumBetween(int low, int high) {
    if (low > high) {
        throw std::invalid_argument("Low should not exceed high.");
    }
    
    long long n = static_cast<long long >(high) - static_cast<long long>(low) + 1;
    long long sum = (static_cast<long long>(low) + static_cast<long long>(high)) * n / 2;
    
    if (sum > std::numeric_limits<int>::max() || sum < std::numeric_limits<int>::min()) {
        throw std::overflow_error("Sum exceeds the allowable range of int.");
    }
    
    return static_cast<int>(sum);
}


int Product(int a, int b) {
    if (a == 0 || b == 0) return 0;

    if (a > 0) {
      if (b > 0) {
        if (a > std::numeric_limits<int>::max() / b) {
          throw std::overflow_error("Product exceeds the allowable range of int.");
        } 
      } else {
        if (a > std::numeric_limits<int>::min() / b) {
          throw std::overflow_error("Product exceeds the allowable range of int.");
        }
      }
    } else {
      if (b > 0) {
        if (a < std::numeric_limits<int>::min() / b) {
          throw std::overflow_error("Product exceeds the allowable range of int.");
        }
      } else {
        if (a < std::numeric_limits<int>::max() / b) {
          throw std::overflow_error("Product exceeds the allowable range of int.");
        }
      }
    }

    return a * b;
}
