from sympy import *
from sympy.plotting import (plot,plot_parametric)
import matplotlib.pyplot as plt
import numpy as np

# Question 1
x, n = symbols('x n')
expr = ((-1)**(n+1) * (-2 + 4*x**2)**n) / (4**n * n)
s = Sum(expr, (n, 1, oo))

# Part A
ratio = abs(simplify(expr.subs(n, n+1) / expr))
print(f"The limit of the ratio of the nth and (n+1)th terms is {limit(ratio, n, oo)}")

# Part B  wolfram alpha says endpoints exclusive????
print(f"The radius of convergence is 2*sqrt(3/2) and the endpoints are -sqrt(3/2) and sqrt(3/2).")

if Sum(((-1)**(n+1) * (-2 + 4*(sqrt(3/2))**2)**n) / (4**n * n), (n, 1, oo)).is_convergent() == True:
    print(f"The series converges when x = sqrt(3/2), so sqrt(3/2) is in the interval of convergence.")
else:
    print(f"The series does not converge when x = sqrt(3/2), so sqrt(3/2) is not in the interval of convergence.")

if Sum(((-1)**(n+1) * (-2 + 4*(-sqrt(3/2))**2)**n) / (4**n * n), (n, 1, oo)).is_convergent() == True:
    print(f"The series converges when x = -sqrt(3/2), so -sqrt(3/2) is in the interval of convergence.")
else:
    print(f"The series does not converge when x = -sqrt(3/2), so -sqrt(3/2) is not in the interval of convergence.")

# Part C
plot(Sum(expr, (n, 1, 5)), Sum(expr, (n, 1, 10)), Sum(expr, (n, 1, 15)), log((2*x**2 + 1) / 2), (x, -3, 3), ylim = (-1, 2))

# Question 2
expr = ((-1)**n * sqrt(pi) * x**(2*n + 1)) / ((2*n + 1) * factorial(n))
s = Sum(expr, (n, 0, oo))

# Part A
print(f"|a_n+1 / a_n| = {abs(simplify(expr.subs(n, n+1) / expr))}")
print(f"The limit of the ratio test as n approaches infinity is {limit(abs(simplify(expr.subs(n, n+1) / expr)), n, oo)}")

# Part B
print(f"The radius of convergence is infinite and the endpoints are -oo and oo exclusive.")

if Sum(((-1)**n * sqrt(pi) * oo**(2*n + 1)) / ((2*n + 1) * factorial(n)), (n, 0, oo)).is_convergent() == True:
    print(f"The series converges when x = oo, so oo is in the interval of convergence.")
else:
    print(f"The series does not converge when x = oo, so oo is not in the interval of convergence.")

if Sum(((-1)**n * sqrt(pi) * (-oo)**(2*n + 1)) / ((2*n + 1) * factorial(n)), (n, 0, oo)).is_convergent() == True:
    print(f"The series converges when x = -oo, so -oo is in the interval of convergence.")
else:
    print(f"The series does not converge when x = -oo, so -oo is not in the interval of convergence.")

# Part C
t = symbols('t')
fx = sqrt(pi) * integrate(E**(-1 * t**2), (t, 0, x))
plot(Sum(expr, (n, 0, 5)), Sum(expr, (n, 0, 10)), Sum(expr, (n, 0, 15)), fx, (x, -10, 10), ylim = (-2, 2))

# Part D
s100 = Sum(expr, (n, 0, 100))
print(f"f(5) is approximatly {N(s100.subs(x, 5))} using s100 as an approximation.")
print(f"The decimal approximation of pi/2 is {N(pi/2)}.")
print(f"The two approximations are about equal.")

# Question 3
expr = ((-1)**n * x**(2*n + 1)) / (factorial(n) * factorial((n + 1)) * 2**(2*n + 1))
J1x = Sum(expr, (n, 0, oo))

# Part A
ratio = abs(simplify(expr.subs(n, n+1) / expr))
print(f"The radius of convergence is infinite since the limit of the ratio test is 0.")

# Part B
plot(Sum(expr, (n, 0, 1)), Sum(expr, (n, 0, 2)), Sum(expr, (n, 0, 3)), Sum(expr, (n, 0, 4)), Sum(expr, (n, 0, 5)), (x, 0, 5), ylim = (-0.6, 0.6))

# Part C
plot(besselj(1, x), besselj(2, x), besselj(3, x), besselj(4, x), besselj(5, x))

# Part D
plot(besselj(1, x), Sum(expr, (n, 0, 1)), Sum(expr, (n, 0, 2)), Sum(expr, (n, 0, 3)), Sum(expr, (n, 0, 4)), Sum(expr, (n, 0, 5)), (x, 0, 5), ylim = (-0.6, 0.6))
