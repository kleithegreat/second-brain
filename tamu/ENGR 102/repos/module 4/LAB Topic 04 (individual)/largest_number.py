# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   4.16.1: LAB: Largest number
# Date:         16 September 2022

userinput = list()

# for loop takes input and compares to current maximum
for i in range(3):
    userinput.append(float(input(f"Enter number {i + 1}: ")))
    if userinput[i] >= userinput[i - 1]:
        maximum = userinput[i]

print(f"The largest number is {maximum}")