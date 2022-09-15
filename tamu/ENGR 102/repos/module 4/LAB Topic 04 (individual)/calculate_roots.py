# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   
# Date:         

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

if a == b == c == 0:
    print("The root is x = 0")
if (a and b == 0) and (c != 0):
    print("You entered an invalid combination of coefficients!")
elif a == 0:
    print(f"The root is x = {(-1 * c) / b}")
