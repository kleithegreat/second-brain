from sympy import *
from sympy.plotting import (plot,plot_parametric)
import matplotlib.pyplot as plt
import numpy as np

# Question
n, ub = symbols('n ub')
expr = (n**50 * 50**n) / factorial(n)
s = Sum(expr, (n, 1, ub))

# Part A
terms = [N(expr.subs(n, i)) for i in range(1, 6)]
print(f"The first 5 terms are: {terms}")
print(f"The terms appear to be increasing.")

# Part B
an1 = ((n + 1)**50 * 50**(n + 1)) / factorial(n + 1)
an = (n**50 * 50**n) / factorial(n)
L = Limit(an1 / an, n, oo)
L = simplify(L)
print(f"The limit is: {L}")
print(f"The limit is 0, so the series converges.")

# Part C
print("The answer to part (b) tells that the terms of the series decrease fast enough that the series converges.")

# Question 2
an = (n**8) * E**(-5*n)

# Part A
x = symbols('x')
plot((integrate(an, (n, x, oo))), 0.0001, (x, 0, 5),ylim = (0, 0.001))
print("It appears that at least four terms are needed to approximate the integral to 0.0001 by looking at the graph.")

# Part B
terms = nsolve(integrate(an, (n, x, oo)) - 0.0001, 3.7)
print(f"The number of terms needed to approximate the series to 0.0001 is: {ceiling(terms)}")

# Part C    
print(f"The sum of the series within 0.0001 using the integral is {N(integrate(an, (n, 1, ceiling(terms))))}")

# Part D
plot(an.subs(n, n+1), (n, 0, 5), ylim = (0, 0.0001))
print("It appears that at least three terms are needed to approximate the integral to 0.0001 by looking at the graph.")

# Part E
terms = nsolve(an.subs(n, n+1) - 0.0001, 3)
print(f"The number of terms needed to approximate the series to 0.0001 is: {ceiling(terms)}")

# Part F
print(f"The sum of the series within 0.0001 using the alternating series estimation theorem is {N(Sum((-1)**n * an, (n, 1, ceiling(terms))))}")


# Question 3
x, n = symbols('x n')
expr = factorial(n)**2 / factorial(2*n) * x**n
s = Sum(expr, (n, 0, oo))

# Part A
print(f"The limit of the ratio test as n approaches infinity is: {limit(abs(simplify(expr.subs(n, n+1) / expr.subs(n, n))), n, oo)}")

# Part B
print(f"The radius of convergence is 4. The endpoints of the interval of convergence are -4 and 4.")

# Part C
try:
    print(f"The sum of the series when x = 4 is: {N(s.subs(x, 4))}")
except ValueError:
    print("The series diverges for x = 4.")

# Part D
nvals = [10, 100, 1000, 10000]
for i in nvals:
    print(f"The value of |an| when n = {i} is: {N(abs(expr.subs(x, -4).subs(n, i)))}")

print(f"Based on the values of |an|, the series diverges for x = -4.")

# Part E
plot(Sum(expr, (n, 0, 1)), Sum(expr, (n, 0, 3)), Sum(expr, (n, 0, 5)), (x, -4, 4))
