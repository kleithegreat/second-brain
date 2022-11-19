from sympy import *

# problem 1

x = symbols("x")
y = (1 + 26/x)**x

# part a
f = ln(1 + 26/x)
g = x**-1

# part b
print(f"THe limit of f as x approaches infinity is {limit(f, x, oo)}")
print(f"THe limit of g as x approaches infinity is {limit(g, x, oo)}")

# part c
print(f"The limit of y as x approaches infinity is {E**limit(diff(f, x)/diff(g, x), x, oo)}")

# part d
print(f"{limit(y, x ,oo)} is equal to {E**limit(diff(f, x)/diff(g, x), x, oo)}")

# problem 2

# part a
print(f"The radius of the billboard would have to be {sqrt((50 + 10 + 10)**2 + (42 + 4 + 4)**2) / 2} or {(sqrt((50 + 10 + 10)**2 + (42 + 4 + 4)**2) / 2).evalf()} inches.")

# part b
frameWidth, frameHeight = symbols("frameWidth frameHeight")
Area = (frameWidth - 8) * (frameHeight - 20)
frameHeight = solve(frameWidth**2 + frameHeight**2 - (55 * 2)**2, frameHeight)[1]
criticalValue = solve(diff(Area, frameWidth))[0]
print(f"The dimensions a = {criticalValue - 8} and b = {frameHeight.subs(frameWidth, criticalValue) - 20} would maximize the area of the picture in the frame.")

# problem 3
R1, R2, h = symbols("R1 R2 h")
R2 = 2 * R1
V = 1/3 * pi * h * (R1**2 + R2**2 + R1*R2)
SA = pi * (R1 + R2) * sqrt((R2 - R1)**2 + h**2) + pi * (R1**2 + R2**2)

# part a
SA = SA.subs([(R2, 2 * R1), (h, solve(V - 590, h)[0])])
plot(diff(SA, R1), (R1, 0, 5), ylim = (300, 800))

# part b


# problem 4
x = symbols("x")
f2dx = 5 / (x + 1) ** 2

# part a
fdx = integrate(f2dx, x) + 3 - integrate(f2dx, x).subs(x, 0)
print(f"f'(x) = {fdx}")
fx = integrate(fdx, x) + 9 - integrate(fdx, x).subs(x, 0)
print(f"f(x) = {fx}")

# part b
c1, c2 = symbols("c1 c2")
fdx = integrate(f2dx, x) + c1
fx = integrate(fdx, x) + c2
solns = list(linsolve([fx.subs(x, 1) - 10, fx.subs(x, 4) - 10], (c1, c2)))[0]
print(solns)
print(f"f(x) = {fx.subs([(c1, solns[0]), (c2, solns[1])])}")
