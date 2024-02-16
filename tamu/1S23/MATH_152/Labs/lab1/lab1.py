from sympy import *

# Problem 1
a, b = symbols("a b")

# Part A
print(((sin(a)**2 + cos(a)**2) / (b**2 + 1)).subs([(a, 1.54), (b, 3.78)]))
print(((sin(a)+cos(a))**2 / (b**2 + 1)).subs([(a, 1.54), (b, 3.78)]))
print("The answers to (a) and (b) are not equal. The expression in part (a) can be simplified to 1 / (b**2 + 1) using the identity sin(x)**2 + cos(x)**2 = 1")

# Problem 2
x = symbols("x", real=True)

# Part A
print((sin(x)**2).subs(x, 3*pi / 4) == ((1 - cos(2 * x)) / 2).subs(x, 3*pi / 4))

# Part B
plot((sin(x)**2 - ((1 - cos(2 * x)) / 2)), (x, 0, 2 * pi))
print("y does not equal 0 for all x because the division of floating point numbers is not completely accurate, hence the small fluctuations around the x axis.")

# Problem 3
fx = -1 * x**3 - 2 * x**2 + 5*x
gx = x

# Part A
plot(fx, gx, (x, -4, 4), ylim=(-15, 15))

# Part B
bounds = solve(fx - gx, x)
area = Abs(integrate(fx, (x, bounds[2], bounds[0])) - integrate(gx, (x, bounds[2], bounds[0]))) + Abs(integrate(fx, (x, bounds[0], bounds[1])) - integrate(gx, (x, bounds[0], bounds[1])))
print(f"Exact area: {area}, Approximate area: {N(area)}")

# Problem 4
u = symbols("u")

# Part A
fx = 5 * x**2 * (x**3 - 7) ** (1/2)
f = 5/3 * u**(1/2)

print(f"{integrate(f, u)} + C")

# Part B
print(integrate(fx, x, manual=True))
print(integrate(f, u).subs(u, x**3 - 7))
print(integrate(fx, x, manual=True) == integrate(f, u).subs(u, x**3 - 7))

# Part C
print(f"Exact: (5/3 * (3**3 - 7)**(1/2)) - (5/3 * (2**3 - 7)**(1/2)), Approximate: {(integrate(f, u).subs(u, x**3 - 7)).subs(x, 3) - (integrate(f, u).subs(u, x**3 - 7)).subs(x, 2)}")

# Part D
print(integrate(fx, (x, 2, 3), manual=True))