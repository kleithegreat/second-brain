# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   6.13.1: LAB: Howdy Whoop
# Date:         30 September 2022

input1 = int(input("Enter an integer: "))
input2 = int(input("Enter another integer: "))

i = 1
while i < 101:
    # checks if divisible by both
    if i % input1 == 0 and i % input2 == 0:
        print("Howdy Whoop")
    # checks if divisible by second
    elif i % input2 == 0:
        print("Whoop")
    # checks if divisible by first
    elif i % input1 == 0:
        print("Howdy")
    else:
        print(i)
    i += 1
