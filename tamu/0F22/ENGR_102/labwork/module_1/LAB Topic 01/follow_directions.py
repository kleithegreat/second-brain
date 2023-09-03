# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   1.12.1: LAB: Follow directions
# Date:         26 Aug0ust

print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")
print("My guess is 2")

# function f(x)
def function(x):
    return (x ** 2 - 1)/(x - 1)

index = 0
while index < 8:
    print(function(1 + 0.1 / 10 ** index))
    index += 1

print()
print("My guess was correct")