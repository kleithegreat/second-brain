# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   4.19.1: LAB: Calculate roots
# Date:         16 September 2022

from math import *

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

# check for valid input and special case
if a == 0 and b == 0 and c != 0:
    print("You entered an invalid combination of coefficients!")
    exit()
elif a == 0:
    print(f"The root is x = {(-1 * c) / b}")
else:
    if b ** 2 - 4 * a * c >= 0:
        root1 = (- b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
        root2 = (- b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
    else:
        root1 = str(- b / 2 * a) + " + " + str(sqrt(-1 * (b ** 2 - 4 * a * c)) / 2 * a) + "i"
        root2 = str(- b / 2 * a) + " - " + str(sqrt(-1 * (b ** 2 - 4 * a * c)) / 2 * a) + "i"

    if (root1 == root2):
        print(f"The root is x = {root1}")
    else:
        print(f"The roots are x = {root1} and x = {root2}")