from sympy import *
from sympy.plotting import (plot,plot_implicit)

# Problem 1
x, y = symbols("x y")

# Part A
equation = Eq(x, -1 * y**2 + 5*y - 3)
plot_implicit(equation, (x, -10, 10), (y, -2, 5))

# Part B
print(solve(equation.subs(x, 0), y))

# Part C
volume = integrate(pi * (-1 * y**2 + 5*y - 3)**2, (y, solve(equation.subs(x, 0), y)[0], solve(equation.subs(x, 0), y)[1]))
print(N(volume))

# Problem 2

# Part A
volume = integrate(pi * cos(x)**2, (x, 0, solve(sin(x) - cos(x))[0])) - integrate(pi * sin(x)**2, (x, 0, solve(sin(x) - cos(x))[0]))
print(N(volume))

# Part B
volume = pi * integrate(asin(y)**2, (y, 0, sqrt(2)/2)) + pi * integrate(acos(y)**2, (y, sqrt(2)/2, pi))
print(N(volume))

# Part C


# Problem 3
fx = 12 / (8 + x**4)

# Part A
plot((fx, (x, -3 ,3)), (-1 * fx, (x, -3 ,3)))

# Part B
surfaceArea = integrate(fx, (x, -3, 3)) - integrate(-fx, (x, -3, 3))
print(N(surfaceArea))

# Part C
volume = integrate(pi * fx**2, (x, -3, 3))
print(N(volume))

# Problem 4

# Part A
"""
i = integrate( E**(-1 * sqrt(x)), (x, 0, 1) )
ii = integrate( (E**(-cos(x))) * sin(2*x), (x, 0, pi / 2) )
iii = integrate( 2 * x * E**(-1 * x), (x, 0, 1) )

print(i == ii and ii == iii)
"""

f=(E**(-sqrt(x)))
g=((E**(-cos(x)))*(sin(2*x)))
h=((2*x)*(E**(-x)))

fint=integrate(f,(x,0,1))
gint=integrate(g,(x,0,pi/2))
hint=integrate(h,(x,0,1))

print("Integration of f is ", fint.evalf())
print("Integration of g is ", gint.evalf())
print("Integration of h is ", hint.evalf())

print("Therefore, all three integrals are equal")

# Part B
print("For the first integral (i), u has to be square root of x, which will make du as 1/2*u. Bound will not change as 0 and 1 stays the same under square root of x")
print("\n")
print("For the second integral (ii), u has to be cos(x), which will make du as -sin(x). Then change sin(2x) into 2sin(x)cos(x). sin(x) should be canceled out and bound will be changed [0,1]")
