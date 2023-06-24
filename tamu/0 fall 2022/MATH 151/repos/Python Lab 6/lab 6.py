from sympy import *

# problem 1
x, r = symbols("x, r")
y = E ** (r * x)

# part a
print(solve((2 * diff(y, x, 2) + diff(y, x, 1) - y), r))

# part b
print(solve((diff(y, x, 2) + 6 * diff(y, x, 1) + 10 * y), r))

# part c
y = E ** (-3 * x) * (cos(x) + sin(x))
print((diff(y, x, 2) + 6 * diff(y, x, 1) + 10 * y))

# problem 2
t = symbols("t")
x = E ** (2 * sin(t))
y = E ** cos(t)

# part a
print(f"<{x.subs(t, pi / 6)} + {diff(x, t, 1).subs(t, pi / 6) * t}, {y.subs(t, pi / 6)} + {diff(y, t, 1).subs(t, pi / 6) * t}>")
print(f"<{N(x.subs(t, pi / 6))} + {diff(x, t, 1).subs(t, pi / 6) * t}, {N(y.subs(t, pi / 6))} + {diff(y, t, 1).subs(t, pi / 6) * t}>")

# part b
print("Horizontal:")
for i in solve(diff(y, t, 1)):
    print(f"({x.subs(t, i)}, {y.subs(t, i)})")

print("Vertical:")
for i in solve(diff(x, t, 1)):
    print(f"({x.subs(t, i)}, {y.subs(t, i)})")

# part c
plot0 = plot_parametric((x, y), (t, 0, 2 * pi), show = false)
tangent1 = plot_parametric(((x.subs(t, pi / 6) + diff(x, t, 1).subs(t, pi / 6) * t), (y.subs(t, pi / 6) + diff(y, t, 1).subs(t, pi / 6) * t)), (t, 0, 2 * pi), show = false)
plot0.append(tangent1[0])

'''horizontals = {}
for i in solve(diff(y, t, 1)):
    horizontals[solve(diff(y, t, 1)).index(i)] = plot_parametric()

print(horizontals)'''


plot0.show()


# problem 3
x, y = symbols("x, y")
limacon = (-1 * ((x ** 2 + y ** 2) / 4) + 2 * x - 2) ** 2 - 5 * (x ** 2 + y ** 2)

# part a
plot_implicit(limacon, (x, -5, 20), (y, -15, 15))

# part b
print(idiff(limacon, y, x))

# part c



# problem 4
x = symbols("x")
y = (x ** (1 / 5) * (x ** 3 + 1) ** (1 / 2)) / (2 - 7 * x) ** 4

# part a
expanded = expand_log(ln(y), force = True)
print(diff(expanded, x, 1) * y)

# part b
print(diff(y, x, 1))

# part c
print((diff(expanded, x, 1) * y).expand())
print((diff(y, x, 1)).expand())
