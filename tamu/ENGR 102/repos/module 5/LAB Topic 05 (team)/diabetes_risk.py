# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               Agustin Portillo
# Section:      522
# Assignment:   5.3.1: LAB: Diabetes risk
# Date:         23 September 2022

import math

if input("Enter your sex (M/F): ") == "F":
    sex = 0.879
else:
    sex = 0
age = int(input("Enter your age (years): "))
bmiInput = float(input("Enter your BMI: "))
if bmiInput < 25:
    BMI = 0
elif bmiInput < 27.5:
    BMI = 0.699
elif bmiInput < 30:
    BMI = 1.97
else:
    BMI = 2.518
if input("Are you on medication for hypertension (Y/N)? ") == "n":
    hypertension = 0
else:
    hypertension = 1.222
if input("Are you on steroids (Y/N)? ") == "y":
    steroids = 2.191
else:
    steroids = 0
if input("Do you smoke cigarettes (Y/N)? ") == "y":
    smoker = 0.855
if input("Did you used to smoke (Y/N)? ") == "y":
    smoker = -0.218
else:
    smoker = 0
if input("Do you have a family history of diabetes (Y/N)? ") == "y":
    if input("Do both your parent(s) and sibling(s) have a history of diabetes? ") == "y":
        history = 0.753
    else:
        history = 0.728
else:
    history = 0
exponent = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history
risk = 100 / (1 + math.e ** exponent)
print(f"Your risk of developing type-2 diabetes is {risk:.1f}%")