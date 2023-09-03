# Lecture 2
---
## Propagation of Error
- say quantites A B and C have errors and Q is the combination
- if Q = a + b + c
    - deltaQ^2 = deltaA^2 + deltaB^2 + deltaC^2 + ...
    - lowercase delta
- error of Q is not simply the sum of the errors of its constituents because the individual errors are uncorrelated
    - summing the individual errors is an overestimate of the real error
### Partial Derivatives
- taking the partial derivative of x means to take the derivative of f with respect to x and pretend the other variables are constants
    - e.g. f(x, y, z) = xyz + x^2 * z^2
        - delta/delta x f(x, y ,z) = yz + 2xz^2
> - shit ton of other formulas for error propagation (division, multiplication, exponents, trig, etc.)
> - many formulas are combinations of the fundamental equations, so you can combine them to get the total propagated error

## Propagation of Error Assumptions
- we assume that all errors are **uncorrelated** and **random**
- cant use special cases for correlated formulas
    - eg. x/(x + y) (numerator is correlated with denominator)
    - can solve by rearranging formula such that each variable appears once in a special case

## Significant Figures
- standard practice is to count one doubtful digit as significant
    - e.g. if a pen is between 13.3 and 13.4 cm on a ruler, estimate it to 13.3x cm (the x is an estimate and significant)