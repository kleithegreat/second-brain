from sympy import *
from sympy.plotting import (plot,plot_parametric)
import matplotlib.pyplot as plt
import numpy as np

# Problem 1
n, ub = symbols("n ub")
expr = 1/n**4
sn = Sum(expr, (n, 1, ub))

# Part A
s10 = sn.subs(ub, 10)
print(f"The partial sum of the series s10 is {N(s10)}")
print(f"The error in using s10 as an approximation of the sum of the series is {N(pi**4/90 - s10)}")

# Part B
lower_estimate = sn.subs(ub, 10) + integrate(expr, (n, 11, oo))
upper_estimate = sn.subs(ub, 10) + integrate(expr, (n, 10, oo))
print(f"The sum of the series is between {N(lower_estimate)} and {N(upper_estimate)}")

# Part C
print(f"The error in the lower estimate is {N(pi**4/90 - lower_estimate)}")
print(f"The error in the upper estimate is {N(upper_estimate - pi**4/90)}")

# Part D
i = 10
while N(pi**4/90 - sn.subs(ub, i)) > 10**(-6):
    i += 1
print(f"The number of terms needed to get an error of 10^-6 is {i}")

# Problem 2
x = symbols("x")
expr = n**2 * E**(-n)
series = Sum(expr, (n, 2, oo))
fx = x**2 * E**(-x)

# Part A
print(f"The indefintie integral of f(x) is {integrate(fx, x)}")
print(F"The definite integral of f(x) from 1 to infinity is {N(integrate(fx, (x, 1, oo)))}")

# Part B
print("Based on the answer in part a, the series converges for all n >= 2 by the integral test.")

# Part C
sn = Sum(expr, (n, 2, ub))
s10 = sn.subs(ub, 10)
s50 = sn.subs(ub, 50)
s100 = sn.subs(ub, 100)
s = sn.subs(ub, oo)
print(f"The 10th partial sum of the series is {N(s10)}")
print(f"The 50th partial sum of the series is {N(s50)}")
print(f"The 100th partial sum of the series is {N(s100)}")
print(f"The sum of the series is {N(s)}")

# Part D
r100 = integrate(expr, (n, 100, oo))
error = N(s - s100)
print(f"The remainder estimate for the integral test for the 100th partial sum is {N(r100)}")
print(f"The actual value of the error is {error}")
print(f"The larger error is the remainder estimate.")

# Part E
i = 2
while integrate(expr, (n, i, oo)) > 10**(-10):
    i += 1

print(f"The number of terms needed to get an error of 10^-10 is {i}")
print(f"The value of s - s{i} is {N(s - sn.subs(ub, i))} which is less than 10^-10")

# Problem 3
an = (n * sin(n)**2) / (1 + n**3)
s = Sum(an, (n, 1, oo))

# Part A
bn = 1 / n**2
print(f"The sequence an can be compared to the sequence bn which is {bn}")

# Part B
anvals = [an.subs(n, i) for i in range(1, 51)]
bnvals = [bn.subs(n, i) for i in range(1, 51)]
plt.figure()
plt.plot(range(1, 51), anvals,"o",label="an")
plt.plot(range(1, 51), bnvals,"o",label="bn")
plt.legend()
plt.show()

print(f"The sequence bn is larger than an.")

# Part C
print(f"The sum of bn is convergent by the integral test.")
print(f"It can be concluded that an is convergent by comparison to bn.")

# Part D
print(f"The conclusion in part c is conclusive")

# Part E
an = (E**n + 1) / (n * E**n + 1)
bn = 1 / n
print(f"The new sequence an can be compared to the sequence bn which is {bn}")

anvals = [an.subs(n, i) for i in range(1, 51)]
bnvals = [bn.subs(n, i) for i in range(1, 51)]
plt.figure()
plt.plot(range(1, 51), anvals,"o",label="an")
plt.plot(range(1, 51), bnvals,"o",label="bn")
plt.legend()
plt.show()

print(f"The sequence ")