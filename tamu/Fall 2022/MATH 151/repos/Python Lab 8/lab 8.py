from sympy import *

# problem 1
x = symbols("x")
fx = (1/40) * (x**6 + 2*x**5 - 16*x**4 - 20*x**3 + 64*x**2 - 36*x + 72)

# part a
print(f"f'(x) = {diff(fx, x, 1)}")
print(f"Approximate critical numbers: x = {solve(diff(fx, x, 1))}")
print(f"f'(-4) = {diff(fx, x, 1).subs(x, -4)} is negative, so f(x) is decreasing on the interval (-oo, {solve(diff(fx, x, 1))[0]})")
print(f"f'(-3) = {diff(fx, x, 1).subs(x, -3)} is positive, so f(x) is increasing on the interval ({solve(diff(fx, x, 1))[0]}, {solve(diff(fx, x, 1))[1]})")
print(f"f'(0) = {diff(fx, x, 1).subs(x, 0)} is negative, so f(x) is decreasing on the interval ({solve(diff(fx, x, 1))[1]}, {solve(diff(fx, x, 1))[2]})")
print(f"f'(0.5) = {diff(fx, x, 1).subs(x, 0.5)} is positive, so f(x) is increasing on the interval ({solve(diff(fx, x, 1))[2]}, {solve(diff(fx, x, 1))[3]})")
print(f"f'(2) = {diff(fx, x, 1).subs(x, 2)} is negative, so f(x) is decreasing on the interval ({solve(diff(fx, x, 1))[3]}, {solve(diff(fx, x, 1))[4]})")
print(f"f'(4) = {diff(fx, x, 1).subs(x, 4)} is positive, so f(x) is increasing on the interval ({solve(diff(fx, x, 1))[4]}, oo)")
graph1 = plot(diff(fx, x, 1), (x, -5 ,5), ylim = (-5 ,5))

# part b
print(f"f''(X) = {diff(fx, x, 2)}")
inflectionPoints = [N(i) for i in real_roots(diff(fx, x, 2), x)]
print(f"Approximate inflection values: x = {inflectionPoints}")
print(f"f''(-3) = {diff(fx, x, 2).subs(x, -3)} is , so f(x) is concave up on the interval (-oo, {inflectionPoints[0]})")
print(f"f''(-2) = {diff(fx, x, 2).subs(x, -2)} is , so f(x) is concave down on the interval ({inflectionPoints[0]}, {inflectionPoints[1]})")
print(f"f''(0) = {diff(fx, x, 2).subs(x, 0)} is , so f(x) is concave up on the interval ({inflectionPoints[1]}, {inflectionPoints[2]})")
print(f"f''(1) = {diff(fx, x, 2).subs(x, 1)} is , so f(x) is concave down on the interval ({inflectionPoints[2]}, {inflectionPoints[3]})")
print(f"f''(3) = {diff(fx, x, 2).subs(x, 3)} is , so f(x) is concave up on the interval ({inflectionPoints[3]}, oo)")
graph1 = plot((diff(fx, x, 1), (x, -5 ,5)), (diff(fx, x, 2), (x, -5 ,5)), ylim = (-5 ,5))

# part c
print(f"f(x) has {len(solve(diff(fx, x, 1)))} local extrema and {len(inflectionPoints)} inflection points.")

# part d
plot(fx, (x, -10, 10), ylim = (-10, 10))

# problem 2
b = symbols("b")
gx = x**3 * E**(b*x**2)

# part a
graph2 = plot((gx.subs(b, -3), (x, -3, 3)), ylim = (-1, 1), show = False)
for i in range(-2, 4):
    graph2.append(plot(gx.subs(b, i), (x, -3, 3), show = False)[0])
graph2.show()

# part b
print(f"Critical values of g: b = {solve(diff(gx, x), x)}")
print("In order for the critical values -sqrt(6)*sqrt(-1/b)/2 and sqrt(6)*sqrt(-1/b)/2 to be real, b must be negative")

# part c
print("As b approaches negative infinity, the critical values approach 0.")
plot(gx.subs(b, -100), (x, -2, 2), ylim = (-0.0005, 0.0005), depth = 10000)

# part d
print(f"Inflection points of g: b = {solve(diff(gx, x, 2), x)}")
print("All inflection points are real when b is negative.")

# part e
print(f"The critical values include -1 and 1 when b = {solve(solve(diff(gx, x, 1), x)[2] - 1, b)[0]}")
print(f"The inflection points include -1 and 1 when b = {solve(solve(diff(gx, x, 2), x)[2] - 1, b)[0]} and {solve(solve(diff(gx, x, 2), x)[4] - 1, b)[0]}")
plot((gx.subs(b, -3/2), (x, -3, 3)), (gx.subs(b, -1/2), (x, -3, 3)), (gx.subs(b, -3), (x, -3, 3)), ylim = (-1, 1))

# problem 3
a, b, x = symbols("a b x")

# part a
fx = ln(5 - x)
a, b = 1, 4
secant = (fx.subs(x, b) - fx.subs(x, a)) / (b - a)
print(f"c = {solve(diff(fx, x, 1) - secant, x)[0].evalf()} or {solve(diff(fx, x, 1) - secant, x)[0]}")

# part b
gx = (x - 5)**(-1 * 5)
print("The Mean Value Theorem cannot be applied here since g(x) is not continuous on the open interval (0, 8).")
plot(gx, (x, 0, 8), ylim = (-10, 10))

# part c
hx = 8*x**2 * cos(4*x)
a, b = pi/4, 3*pi/4
secant = (hx.subs(x, b) - hx.subs(x, a)) / (b - a)
print(f"c = {nsolve(diff(hx, x, 1) - secant, x, 1.7)}")
