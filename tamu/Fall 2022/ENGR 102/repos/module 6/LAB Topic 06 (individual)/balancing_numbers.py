# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   6.15.1: LAB: Balancing numbers
# Date:         30 September 2022

n = int(input("Enter a value for n: "))

r = 0
# increments r until the left side of number n is greater than the right
while ((n + r) * (n + r + 1)) / 2 - (n * (n + 1)) / 2 <= (n * (n - 1)) / 2:
    if ((n + r) * (n + r + 1)) / 2 - (n * (n + 1)) / 2 == (n * (n - 1)) / 2:
        print(f"{n} is a balancing number with r={r}")
        exit()
    r += 1

print(f"{n} is not a balancing number")
