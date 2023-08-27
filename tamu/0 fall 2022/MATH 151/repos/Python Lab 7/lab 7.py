from sympy import *

# problem 1
x = symbols("x")

piece1 = 8 - x**2
piece2 = 5 * E**(-1 * ((x - 2) / 2)**2) + x

# part a
newton = x - diff(piece2, x) / diff(piece2, x, 2)
print(f"{solve(diff(piece1, x), x)[0]}, {newton.subs(x, 2.4)}, {newton.subs(x, 4.7)}")

# part b
wholeFunction = Piecewise((8 - x**2, x < 0), (5 * E**(-1 * ((x - 2) / 2)**2) + x, x >= 0))
candidates = [-5, solve(diff(piece1, x), x)[0], newton.subs(x, 2.4), newton.subs(x, 4.7), 5]
minimum = 0
maximum = 0
for i in candidates:
    if wholeFunction.subs(x, i) > maximum:
        maximum = wholeFunction.subs(x, i)
    if wholeFunction.subs(x, i) < minimum:
        minimum = wholeFunction.subs(x, i)
i = -5
while i <= 5:
    if wholeFunction.subs(x, i) > maximum:
        maximum = "DNE"
        break
    i += 0.01
i = -5
while i <= 5:
    if wholeFunction.subs(x, i) < minimum:
        minimum = "DNE"
        break
    i += 0.01
    
print(f"The absolute maximum for f(x) is {maximum} and the absolute minimum is {minimum} in the domain of [-5, 5]")

# part c
candidates = [-10, solve(diff(piece1, x), x)[0], newton.subs(x, 2.4), newton.subs(x, 4.7), 10]
minimum = 0
maximum = 0
for i in candidates:
    if wholeFunction.subs(x, i) > maximum:
        maximum = wholeFunction.subs(x, i)
    if wholeFunction.subs(x, i) < minimum:
        minimum = wholeFunction.subs(x, i)
i = -10
while i <= 10:
    if wholeFunction.subs(x, i) > maximum:
        maximum = "DNE"
        break
    i += 0.01
i = -10
while i <= 10:
    if wholeFunction.subs(x, i) < minimum:
        minimum = "DNE"
        break
    i += 0.01
print(f"The absolute maximum for f(x) is {maximum.evalf()} and the absolute minimum is {minimum.evalf()} in the domain of [-10, 10]")

# part d
plot((piece1, (x, -10, 0)), (piece2, (x, 0, 10)), ylim = [-10, 10])

# problem 2
k, r0, r = symbols('k r0 r')
v = k*r0*r**2 - k*r**3

# part a
half_r0 = v.subs(r, .5*r0)
twothirds_r0 = v.subs(r, 2/3*r0)
one_r0 = v.subs(r, r0)
print(f'{twothirds_r0} is greater than {half_r0} and {one_r0} on [.5r0, r0], so v has an abs max at r = (2/3)*r0 on [.5r0, r0]')

# part b
print()
print(f'the abs max value of v on [.5r0, r0] is {twothirds_r0}')

# part c
print()
vsub = v.subs({k:15000, r0: .65})
print(f'the maximum value of the function is {vsub.subs(r,130/300)} and it occurs at r = 130/300 (or r = .4333)')

# part d
vplot = plot(vsub,(r,0,.65))

# problem 3
x = symbols("x")
fx = atan(x)
gx = acot(x)

# part a
dfx = diff(fx, x)
dgx = diff(gx, x)
print(f"The derivative of f(x) + g(x) is {simplify(dfx + dgx)}")

# part b
print("The derivative of f(x) + g(x) tells you that the graph of f(x) + g(x) is flat for all x")

# part c
combined = Piecewise((fx + gx + pi, x <= 0), (fx + gx, x > 0))
plot(combined)

print("The function is arctan(x) + arccot(x) + pi when x <= 0, and arctan(x) + arccot(x) when x is greater than 0")

# part d
print("This makes sense for x > 0 because tan x is equal to cot(pi / 2 - x)")
