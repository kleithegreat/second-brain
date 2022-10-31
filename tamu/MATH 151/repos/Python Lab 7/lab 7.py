from sympy import *

# problem 1
x = symbols("x")

piece1 = 8 - x**2
piece2 = 5 * E**(-1 * ((x - 2) / 2)**2) + x

# part a
print(solve(diff(piece2, x)), x)


# problem 2

# part a
k, r0, r = symbols("k r0 r")