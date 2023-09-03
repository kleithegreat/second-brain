from sympy import *

# problem 1
x, r = symbols("x, r")
y = E ** (r * x)

# part a
#print(solve((2 * diff(y, x, 2) + diff(y, x, 1) - y), r))

# part b
#print(solve((diff(y, x, 2) + 6 * diff(y, x, 1) + 10 * y), r))

# part c
#y = E ** (-3 * x) * (cos(x) + sin(x))
y = cos(x) + sin(x)
equation = (diff(y, x, 2) + 6 * diff(y, x, 1) + 10 * y)
print(simplify(equation))
