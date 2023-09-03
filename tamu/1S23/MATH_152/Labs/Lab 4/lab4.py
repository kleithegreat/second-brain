from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import scipy

# Problem 1 
x = symbols("x")

# Part A
fx = (5 + sin(x))**(1/4)
plot(fx, (x, 0, 1))

# Part B
a = 0
b = pi/2
n = 200
dx = (b - a) / n
xVals = [i for i in np.arange(a, b, float(dx))]
yVals = [fx.subs(x, i) for i in xVals]

left = sum(yVals) * dx
print(f"The left endpoint riemann sum using n = 200 subintervals is {N(left)}")

# Problem 2
xVals = [i for i in np.arange(a + dx, b + dx, float(dx))]
yVals = [fx.subs(x, i) for i in xVals]
right = sum(yVals) * dx
print(f"The right endpoint riemann sum using n = 200 subintervals is {N(right)}")

# Problem 3

# Part A
xVals = [i for i in np.arange(a + dx/2, b - dx/2 + dx, float(dx))]
yVals = [fx.subs(x, i) for i in xVals]
mid = sum(yVals) * dx
print(f"The midpoint riemann sum using n = 200 subintervals is {N(mid)}")

# Part B
avg = N((left + right) / 2)
print(f"Average of left and right riemann sums: {avg}")
print(f"The average of the left and right riemann sums are approximately equal to the midpoint sum.")

# Problem 4

# Part A
xVals = [i for i in np.arange(a, b + dx, float(dx))]
yVals = [fx.subs(x, i) for i in xVals]
trapezoid = np.trapz(yVals, xVals)
print(f"The trapezoid approximation is {N(trapezoid)}")

# Part B
print(f"The trapezoid approximation is approximately equal to the average of the left and right endpoint approximations.")

# Part C
f = (5 + sin(x))**Rational(1, 4)
plot(f, (x, 0, pi/2))
xp = [0, pi/8, pi/4, 3*pi/8, pi/2]
yp = [f.subs(x, i) for i in xp]
plt.plot(xp, yp)
plt.show()

# Problem 5
xVals = [i for i in np.arange(a, b + dx, float(dx))]
yVals = [fx.subs(x, i) for i in xVals]
simp = scipy.integrate.simps(yVals, xVals)
print(f"The simpson approximation with n=200 subintervals is {N(simp)}")

# Problem 6
actual = 2.4196410881
print(f"Error of left endpoint approximation: {abs(actual - N(left))}")
print(f"Error of right endpoint approximation: {abs(actual - N(right))}")
print(f"Error of midpoint approximation: {abs(actual - N(mid))}")
print(f"Error of trapezoid approximation: {abs(actual - N(trapezoid))}")
print(f"Error of Simpson's method: {abs(actual - N(simp))}")
