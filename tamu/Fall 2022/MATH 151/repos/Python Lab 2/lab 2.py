import math
from sympy import *

a, b, c, d = symbols('a, b, c, d')

# problem 1
expr0 = 1 + a * (a + 1)* (a + 2) * (a + 3)

# part a
print(solve(expr0, a))

# part b
print(expand(expr0))

# part c
print(factor(expr0))

# part d
plot(expr0, (a, -5, 1), ylim = [-5, 5])

# problem 2
expr1 = (-1 / 2) * b * c ** 2 + d
expr2 = -1 * a * b * c - a ** 2 * b * E ** (-c / a) + a ** 2 * b + d

# part a
print(solve(expr1.subs([(b, 9.8), (d, 6)]), c)[1])

# part b
print(solve(expr2.subs([(a, 2), (b, 9.8), (d, 6)]), c)[1])

# part c
plot(expr1.subs([(b, 9.8), (d, 6)]), expr2.subs([(a, 2), (b, 9.8), (d, 6)]), (c, 0, 3), ylim = [-2, 8])

# problem 3
expr3 = a * sin(c * d)
expr4 = b * cos(d)

# part a
ix = expr3.subs([(a, 1), (c, 2)])
iy = expr4.subs([(b, 1)])

iix = expr3.subs([(a, 3), (c, 2)])
iiy = expr4.subs([(b, 1)])

iiix = expr3.subs([(a, 1), (c, 3)])
iiiy = expr4.subs([(b, 2)])
plot_parametric((ix, iy), (iix, iiy), (iiix, iiiy))

# part b
# variable a changes the width of the lissajous figure where numbers whose absolute value is greater than one increase width while numbers whose absolute value is between one and zero decrease the width
# variable b changes the height of the lissajous figure in the same way variable a changes the width; numbers whose absolute value is greater than one increase the height while numbers whose absolute value is between zero and one decrease the height
# variable n changes the number of oscillations between the top and bottom of the lissajous figure