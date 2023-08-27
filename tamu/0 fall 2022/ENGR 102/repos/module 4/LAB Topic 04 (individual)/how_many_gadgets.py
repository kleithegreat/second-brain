# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   4.18.1: LAB: How many gadgets
# Date:         16 September 2022

days = int(input("Please enter a positive value for day: "))

# checks for valid input
if days < 0:
    print("You entered an invalid number!")
    exit()

total = 0
if (days < 11):
    total += 5 * days
elif (days < 61):
    total += 50 + (days - 10) * 50
elif (days < 101):
    total += 3775 - (109 - days) * (110 - days) / 2
else:
    total = 3730

print(f"The total number of gadgets produced on day {days} is {int(total)} ")