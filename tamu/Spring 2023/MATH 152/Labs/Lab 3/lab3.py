from sympy import *
from sympy.plotting import (plot,plot_implicit)

# Question 1
x = symbols("x")
blue = x * E**(1 - x/2)
grey = x
green = (x**2) / 2

# Part A
v = integrate(pi * 2**2, (x, 0, 2)) - integrate(pi * blue**2, (x, 0, 2))
print(f"{v} or {N(v)}")

# Part B
y = symbols("y")
expr = y - x * E**(1 - x/2)
invBlue = solve(expr, x)
v = pi * integrate(invBlue[0]**2, (y, 0, 2))
print(f"{v} or {N(v)}")

# Part C
v = integrate(pi * blue**2, (x, 0, 2)) - integrate(pi * grey**2, (x, 0, 2))
print(f"{v} or {N(v)}")

# Part D
expr = y - (x**2 / 2)
invGreen = sqrt(2*y)#solve(expr, x)[1]
v = pi * integrate((2.5 - y)**2 - (2.5 - invGreen)**2, (y, 0, 2))
print(f"{v} or {N(v)}")

# Question 2

# Part A
rho = 1000
g = 9.8
low = 0
high = 2
Ai = 3*y
di = 3 - y
work = rho * g * integrate(Ai * di, (y, low, high))
print(f"{work} newton meters of work")

# Part B
high = y
height = solve(rho * g * integrate(Ai * di, (y, low, high)) - 3 * 10**4, real=True)
print(f"The remaining water is {re(height[1])} meters deep.")

# Question 3
fx = cos(x)**2
gx = cos(x)**4

# Part A
plot(fx, gx, (x, 0, pi/2))
print(N(pi * integrate(solve(cos(x)**2 - y, x)[3]**2 - solve(cos(x)**4 - y, x)[7]**2, (y, 0, 1))))

# Part B
area = integrate(fx, (x, 0, pi/2)) - integrate(gx, (x, 0, pi/2))
print(f"The area of the region is {area}")

# Part C
xbar = integrate(x*(fx - gx), (x, 0, pi/2)) / (integrate(fx, (x, 0, pi/2)) - integrate(gx, (x, 0, pi/2)))
print(N(xbar))
print("The center of mass value makes sense because it looks like the middle???")

# Part D
distance = pi * (pi/2 - xbar)**2
print(f"The center of mass travels {distance} units far")
print(N(distance * area))