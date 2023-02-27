from sympy import *

# question 1
x = symbols("x")
fx = (x**3 - 4*x + 3) / ((x - 5)**2 * (x**2 + 3) * (x**2 + 5))

# part a
A, B, C, D, E, F = symbols("A B C D E F")
expr = A*(x - 5)*(x**2 + 3)*(x**2 + 5) + B*(x**2 + 3)*(x**2 + 5) + (C*x + D)*(x - 5)**2 * (x**2 + 5) + (E*x + F)*(x - 5)**2 * (x**2 + 3)
print(f"Expanded decomposition: {collect(expand(expr), x)}")
x5 = A + C + E
x4 = -5*A + B - 10*C + D - 10*E + F
x3 = 8*A + 30*C - 10*D + 28*E - 10*F - 1
x2 = -40*A + 8*B - 50*C + 30*D - 30*E + 28*F
x1 = 15*A + 125*C - 50*D + 75*E - 30*F + 4
x0 = -75*A + 15*B + 125*D + 75*F - 3
coeffs = solve([x5, x4, x3, x2, x1, x0], [A, B, C, D, E, F])
print(f"The coefficients are: {coeffs}")
decomposed = (A/(x-5) + B/(x-5)**2 + (C*x + D)/(x**2 + 3) + (E*x + F)/(x**2 + 5)).subs(coeffs)
print(f"Resulting polynomial: {decomposed}")
print(f"The integral of the partial fraction decomposition is: {integrate(decomposed)}")

# part b
pdf = apart(fx)
print(f"The partial fraction decomposition using python is: {pdf}")
print(f"The integral of that decomposition is: {integrate(pdf)}")

# part c
print(f"The direct integral of f is: {integrate(fx)}")
assert integrate(decomposed) == integrate(pdf) and integrate(pdf) == integrate(fx)
print("The integrals from part A, B, and C are the same.")

# question 2

# part a

# part b

# part c

# question 3

# part a

# part b

# part c
