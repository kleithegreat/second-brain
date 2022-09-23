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

from math import e # imports euler's constant from the math module for use in calculation

userInput = input("Enter your sex (M/F): ") # takes in user input in order to compare to both uppercase and lowercase letters
if userInput == "F" or userInput == "f": # assigns sex parameter based on user input
    sex = 0.879
else:
    sex = 0
age = int(input("Enter your age (years): ")) # stores the users age for use in calculation
bmiInput = float(input("Enter your BMI: "))
if bmiInput < 25: # assigns the BMI parameter based on the user input
    BMI = 0
elif bmiInput < 27.5:
    BMI = 0.699
elif bmiInput < 30:
    BMI = 1.97
else:
    BMI = 2.518
userInput = input("Are you on medication for hypertension (Y/N)? ")
if userInput == "n" or userInput == "N": # assigns hypertension parameter based on user input
    hypertension = 0
else:
    hypertension = 1.222
userInput = input("Are you on steroids (Y/N)? ")
if userInput == "y" or userInput == "Y": # assigns steroids parameter based on user input
    steroids = 2.191
else:
    steroids = 0
userInput = input("Do you smoke cigarettes (Y/N)? ")
if userInput == "y" or userInput == "Y": # assigns smoker parameter based on user input
    smoker = 0.855
else:
    userInput = input("Did you used to smoke (Y/N)? ")
    if userInput == "y" or userInput == "Y": # checks if user used to smoke
        smoker = -0.218
    else:
        smoker = 0
userInput = input("Do you have a family history of diabetes (Y/N)? ")
if userInput == "y" or userInput == "Y": # assigns history parameter based on user input
    userInput = input("Both parent and sibling (Y/N)? ")
    if userInput == "y" or userInput == "Y": # checks whether family history is both parental and sibling or just one
        history = 0.753
    else:
        history = 0.728
else:
    history = 0
exponent = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history
risk = 100 / (1 + e ** exponent) # calculates risk percent
print(f"Your risk of developing type-2 diabetes is {risk:.1f}%") # formats the percent chance to once decimal place
