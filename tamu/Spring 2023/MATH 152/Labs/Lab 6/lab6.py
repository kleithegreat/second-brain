from sympy import *
import matplotlib.pyplot as plt
from numpy import cumsum

# Question 1
n = symbols("n")
an = 1 + 1/n**2

# Part a
print(f"The first ten terms of the sequence are: {[an.subs(n, i) for i in range(1, 11)]}")

# Part b
nvals = [an.subs(n, i) for i in range(1, 31)]
plt.figure()
plt.plot(range(1, 31), nvals, "o")
plt.show()

# Part c
print(f"The limit of the sequence as n approaches infinity is {limit(an, n, oo)}")


# Question 2
bn = (4/5)**n / n

# Part a
assert limit(bn, n, oo) == 0
print(f"The limit of the sequence as n approaches infinity is: {limit(bn, n, oo)}")

# Part b
b1_50 = [bn.subs(n, i) for i in range(1, 51)]
s1_50 = cumsum(b1_50)

plt.figure()
plt.plot(range(1, 51), b1_50, "ro", label="sequence")
plt.plot(range(1, 51), s1_50, "bo", label="partial sums")
plt.legend()
plt.show()

# Part c
print(N(Sum(bn, (n, 1, oo)))) #TODO: infinite or finite series? how do exact form?

# Question 3
an = 3 / (n**2 + 4*n)

# Part a
print(f"The limit of the sequence as n approaches infinity is: {limit(an, n, oo)}")

# Part b
print(f"First 12 terms: {[an.subs(n, i) for i in range(1, 13)]}")
print(f"First 12 partial sums: {cumsum([an.subs(n, i) for i in range(1, 13)])}")

# Part c
print(f"The partial fraction decomposition of the series is: {apart(an)}")

# Part d
# TODO: how do


# Question 4

# Part a
a = [1]
for n in range(1, 11):
    a.append(1/(3 * a[n-1]**2) + (2*a[n-1])/3)

print(f"The first ten terms of the sequence are: {a}")
print("The limit of the sequence as n approaches infinity is 1")

# Part b
a = [100]
for n in range(1, 11):
    a.append(1/(3 * a[n-1]**2) + (2*a[n-1])/3)

print(f"The first ten terms of the sequence with a0 = 100 are: {a}")

# Part c
print("Regardless of the starting term, the sequence always converges to 1 when n approaches infinity.")
