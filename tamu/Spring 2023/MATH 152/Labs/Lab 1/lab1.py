from sympy import *

# Problem 1

a, b = symbols("a b")

# Part A

print(((sin(a)**2 + cos(a)**2) / (b**2 + 1)).subs([(a, 1.54), (b, 3.78)]))

print(((sin(a)+cos(a))**2 / (b**2 + 1)).subs([(a, 1.54), (b, 3.78)]))

print("The answers to (a) and (b) are not equal. The expression in part (a) can be simplified to 1 / (b**2 + 1) using the identity sin(x)**2 + cos(x)**2 = 1")

# Problem 2

x = symbols("x")

# Part A
print((sin(x)**2).subs(x, 3*pi / 4) == ((1 - cos(2 * x)) / 2).subs(x, 3*pi / 4))

# Part B
plot((sin(x)**2 - ((1 - cos(2 * x)) / 2)), (x, 0, 2 * pi))
print("y does not equal 0 for all x because the division of floating point numbers is not completely accurate, hence the small fluctuations aroudn the x axis.")

# Problem 3
fx = -1 * x**3 - 2 * x**2 + 5*x
gx = x

# Part A
plot(fx, gx, (x, -4, 4), ylim=(-15, 15))

# Part B



# Problem 4

u = symbols("u")

# Part A
fx = 5 * x**2 * (x**3 - 7) ** (1/2)
u = x**3 - 7
fu = 5/3 * u**(1/2)
