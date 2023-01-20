from sympy import *

a, b, c, d = symbols('a b c d')

# problem 1
expr0 = a ** 5 + 4 * a ** 3 - 2 * a ** 2 + 8 * a - 1

# part a
print("Plugging in 0 for x produces "+ str(expr0.subs(a, 0)) + ", and plugging in 1 for x produces " + str(expr0.subs(a, 1)) + ", meaning that the y-value 0 must be contained within the domain of [0, 1].")

# part b
i = 0
while i < len(solve(expr0, a)):
    if solve(expr0, a)[i] >= 0 and solve(expr0, a)[i] <= 1:
        root = solve(expr0, a)[i]
        break
    i += 1
print("In the domain of [0, 1], f(x) has a root of " + str(float(root)) + ".")

# problem 2
expr1a = 2 * a - 3
expr1b = 4 * a - a ** 2
expr1c = (a ** 2 - 6 * a + 8) / (a - 4)
expr1d = E ** ((a - 4) * ln(3))

# part a
print(f"As x approaches 3 from the left, f(x) approaches {limit(expr1a, a, 3)}.")
print(f"As x approaches 3 from the right, f(x) approaches {limit(expr1b, a, 3)}.")
print("f(x) is continuous at x = 3")
print(f"As x approaches 4 from the left, f(x) approaches {limit(expr1b, a, 4)}.")
print(f"As x approaches 4 from the right, f(x) approaches {limit(expr1c, a, 4)}.")
print("f(x) is discontinuous at x = 4. f(x) is left continuous at x = 4.")
print(f"As x approaches 5 from the left, f(x) approaches {limit(expr1c, a, 5)}.")
print(f"As x approaches 5 from the right, f(x) approaches {limit(expr1d, a, 5)}.")
print("f(x) is continuous at x = 5.")

# part b
plot((expr1a, (a, 0 , 3)), (expr1b, (a, 3, 4)), (expr1c, (a, 4, 5)), (expr1d, (a, 5, 6)), ylim = (-5, 8))

# problem 2
expr2 = (a * b) / (b + (a - b) * (E ** (-1 * c * d)))

# part a
plot(expr2.subs([(a, 1000), (b, 10), (c, 0.1)]), (d, 0, 100), ylim = (0, 1000))
print(f"The limit of P(t) where K = 1000 as t approaches infinity is {limit(expr2.subs([(a, 1000), (b, 10), (c, 0.1)]), d, oo)}.")

# part b
plot(expr2.subs([(a, 1), (b, 10), (c, 0.1)]), (d, 0, 50), ylim = (0, 10))
print(f"The limit of P(t) where K = 1 as t approaches infinity is {limit(expr2.subs([(a, 1), (b, 10), (c, 0.1)]), d, oo)}.")

# part c
plot(expr2.subs([(a, 15), (b, 10), (c, 0.1)]), (d, 0, 20), ylim = (0, 15))
print(f"The limit of P(t) where K = 15 as t approaches infinity is {limit(expr2.subs([(a, 15), (b, 10), (c, 0.1)]), d, oo)}.")

# last part
print("As the variable t goes to infinity, population size goes to whatever value variable K is. From this we can infer that the variable K represents the maximum population size of the model.")
