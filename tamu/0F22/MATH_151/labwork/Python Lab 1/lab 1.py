import math
from sympy import *

a, b, c, d = symbols('a, b, c, d')

# problem 1

# part a
print((79 * (math.e ** 1.29 + 11.1 **2))/(2026-5.1**3))

# part b
exp0 = cos(a) * sec(b) + tan(c)
exp0_sub = exp0.subs([(a, 11 * pi / 12), (b, 75 * pi / 180), (c, 7 * pi / 12)])
print("Exact value:", exp0_sub.simplify())
print("Approximate value:", exp0_sub.evalf())


# problem 2

# part a
exp1 = sqrt(a ** 2 - 4) / (a - 2)
xvals = [-10, -100, -1000000]
exp1_eval = [exp1.subs(a, i).evalf() for i in xvals]
print("Function f(x) with x-values", xvals, "evaluate to", exp1_eval, "respectievly.")

# part b
xvals = [2.01, 2.0001, 2.000001]
exp1_eval = [exp1.subs(a, i).evalf() for i in xvals]
print("Function f(x) with x-values", xvals, "evaluate to", exp1_eval, "respectievly.")

# part c
# when x values get really large in the negative direction, f(x) approaches -1

# part d
# when x value get really close to 2 from the right, f(x) approaches infinity


# problem 3

# part a
# a = x, b = v, c = alpha, d = h
exp2 = (-16 * a ** 2) / (b ** 2 * cos(c) ** 2) + tan(c) * a + d
exp2_eval = exp2.subs([(a, 409), (b, 130), (c, 26 * pi / 180), (d, 3)]).evalf()
print("The ball will end up", exp2_eval,"feet up at the wall; it will not clear the wall.")

# part b
# d = y
exp3 = d + (16 * a ** 2) / (b ** 2 * cos(c) ** 2) - tan(c) * a
exp3_eval = exp3.subs([(a, 15), (b, 24), (c, 54.2 * pi / 180), (d, 10)]).evalf()
print("Luka Doncic released the ball", exp3_eval, "feet high.")