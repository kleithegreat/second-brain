from sympy import *

x, t, n = symbols('x, t, n')

# problem 1
expr0 = (2 * x + 1) / (x ** 2 + 2)

# part a
tangent = expr0.subs(x, 2) + diff(expr0, x).subs(x, 2) * (x - 2)
print(f"The equation of the tangent line where x = 2 is y = {tangent}")

# part b
normal = expr0.subs(x, 2) + -1 / (diff(expr0, x).subs(x, 2)) * (x - 2)
print(f"The equation of the normal line where x = 2 is y = {normal}")

# part c
plot((tangent, (x, 0, 3)), (normal, (x, 0, 3)), (expr0, (x, 0, 3)), ylim = (-1, 2))

# problem 2
expr1 = sin(x) - (1/1000) * sin(1000 * x)

# part a
plot(expr1, (x, -2 * pi, 2 * pi))
print("Slope of y look like about 1 near x = 0")

# part b
plot(expr1, (x, -0.25, 0.25))
print("Slope of y looks like about 1 near x = 0")

# part c
print(f"The actual slope of the tangent line of y at x = 0 is {diff(expr1, x).subs(x, 0)}")

# part d
plot(expr1, (x, -0.001, 0.001))

# problem 3
expr2 = 100000 * (1 - (1/60) * t) ** 2

# part a
print(f"The average rate of change of V from 0 to 10 minutes is {(expr2.subs(t, 10) - expr2.subs(t, 0)) / 10}")

# part b
print(f"The instantaneous rate of change of V with respect to t is V'(t) = {diff(expr2, t)}")

# part c
print(f"The instantaneous rate of change of V at t = 10 minutes is {diff(expr2, t).subs(t, 10)} gallons per minute")

# part d
print("The answers in parts (a) and (c) are different because part (a) is asking for the average rate of change over a period of time, while part (c) is asking for the instantaneous rate of change at a specific point in time. The two are different because the functions rate of change changes with time since it is a quadratic and not a linear function.")

# problem 4
expr3 = E ** x * (1 + x ** 2)

# part a
i = 1
while i <= 8:
    print("f", end = "")
    for j in range(i):
        print("'", end = "")
    print(f"(x) = {diff(expr3, x, i)}")
    i += 1

# part b
nthderiv = E ** x * (x ** 2 + 2 * n * x + (n ** 2 - n + 1))
print(f"The formula for the nth derivative of f is {nthderiv}")

# part c
print(f"{diff(expr3, x, 50)}")
print(f"{nthderiv.subs(n, 50)}")