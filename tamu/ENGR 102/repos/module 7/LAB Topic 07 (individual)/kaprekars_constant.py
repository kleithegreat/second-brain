# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.28.1: LAB: Kaprekar's constant
# Date:         07 October 2022

userInput = input("Enter a four-digit integer: ")
ascending = [int(x) for x in userInput]
count = 0
print(userInput, end = "")

while True:
    ascending.sort()
    descending = [x for x in reversed(ascending)]

    for i in range(4):
        ascending[i] = descending[i] - ascending[i]
    count += 1
    i = 0
    while i < len(ascending):
        if ascending[i] < 0:
            ascending[i - 1] -= 1
            ascending[i] += 10
            i -= 1
            continue
        i += 1

    print(f" > {int(''.join(map(str,ascending)))}", end = "")
    if ascending == [6, 1, 7, 4]:
        break

print()
print(f"{userInput} reaches 6174 via Kaprekar's routine in {count} iterations")
