# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   5.4.1: LAB: Boiling curve
# Date:         23 September 2022

from math import log10

# converts the user input into a float and stores it in the temp variable
temp = float(input("Enter the excess temperature: "))

# checks if the input is within the domain of the calcualtion
if temp < 1.3 or temp > 1200:
    # tells the user that their input is not valid for the calculation
    print("Surface heat flux is not available")
    # exits the program if input is not valid
    exit()

# determines which initial and final x and y values should be used in the flux calculation
# assign points A and B to initial and final x and y values if input is less than or equal to 5
if temp <= 5:
    x0 = 1.3
    y0 = 1000
    x1 = 5
    y1 = 7000
# assign points B and C to initial and final x and y values if input is less than or equal to 30
elif temp <= 30:
    x0 = 5
    y0 = 7000
    x1 = 30
    y1 = 1.5 * 10 ** 6
# assign points C and D to initial and final x and y values if input is less than or equal to 120
elif temp <= 120:
    x0 = 30
    y0 = 1.5 * 10 ** 6
    x1 = 120
    y1 = 2.5 * 10 ** 4
# assign points D and E to initial and final x and y values if input is less than or equal to 1200
else:
    x0 = 120
    y0 = 2.5 * 10 ** 4
    x1 = 1200
    y1 = 1.5 * 10 ** 6

# calculates flux using appropriate initial and final x and y values using user input
flux = y0 * (temp / x0) ** (log10(y1 / y0) / log10(x1 / x0))

# prints the calculated flux value rounded to the nearest integer
print(f"The surface heat flux is approximately {round(flux)} W/m^2")
