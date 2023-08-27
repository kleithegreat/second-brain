from sympy import *

# problem 1
x, n = symbols("x, n")

expr0 = E ** x * (1 + x ** 2)

# part a
i = 1
while i <= 8:
    print("f", end = "")
    for j in range(i):
        print("'", end = "")
    print(f"(x) = {diff(expr0, x, i)}")
    i += 1

# part b
nthderiv = E ** x * (x ** 2 + 2 * n * x + (n ** 2 - n + 1))
print(f"The formula for the nth derivative of f is {nthderiv}")

# part c
print(f"{diff(expr0, x, 50)}")
print(f"{nthderiv.subs(n, 50)}")

# problem 2
k, t = symbols("k, t")

# part a
y = cos(k * t)
print(f"k = {solve(4 * diff(y, t, 2) + 25 * y, k)}")

# part b
A, B = symbols("A, B")
eq = A * sin(k * t) + B * cos(k * t)
for i in solve(4 * diff(y, t, 2) + 25 * y, k):
    if (4 * diff(eq, t, 2) + 25 * eq).subs(k, i) == 0:
        print(f"Every member of the family of functions y = A sin(kt) + B cos(kt) is also a solution for k = {i}.")
    else:
        print(f"Not every member of the family of functions y = A sin(kt) + B cos(kt) is also a solution for k = {i}.")

# problem 3

# part a
g = ((t - 2) / (2 * t + 1)) ** 9
print(diff(g, t, 1))

# part b
print(simplify(diff(g, t, 1)))

# part c
print(f"Function g would have a horizontal tangent line at x = {solve(diff(g, t, 1), t)}")

# part d
f = (2 * t + 1) ** 5 * (t ** 2 - t + 2) ** 4
print(diff(f, t, 1))

# part e
print(simplify(diff(f, t, 1)))

# part f
print(factor(diff(f, t, 1)))

# part g
print("The factored version would be more useful for locating the horizontal tangent lines of f(t) since in its factored form, it is easier to see where t could equal zero, which is really just where the derivative is equal to zero or a horizontal tangent.")

# problem 4
mu, W, theta = symbols("mu, W, theta")
F = mu * W / (mu * sin(theta) + cos(theta))

# part a
print(f"F'(theta) = {diff(F, theta, 1)}")

# part b
print(f"theta = {solve(diff(F, theta, 1), theta)}")

# part c
plot(diff(F.subs([(W, 100), (mu, 0.6)]), theta, 1), (theta, -1 * pi, pi), ylim = (-1, 1))
print("According to the graph, the values of theta where dF/dTheta = 0 is about -2.5 and 0.5")

# part d
print(f"Given the conditions of part c, dF/dTheta equals zero in the domain of [-pi, pi] when theta equals {solve(diff(F.subs([(W, 100), (mu, 0.6)]), theta, 1), theta)[0]} and {N(solve(diff(F.subs([(W, 100), (mu, 0.6)]), theta, 1), theta)[0] - pi)}.")
