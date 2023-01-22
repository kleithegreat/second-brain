# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.28.1: LAB: Kaprekar's constant
# Date:         07 October 2022

userInput = input("Enter a four-digit integer: ")
ascending = [int(userInput) // 1000, (int(userInput) // 100) % 10, (int(userInput) // 10) % 10, int(userInput) % 10]
count = 0
print(userInput, end = "")

while not (ascending[0] == ascending[1] and ascending[1] == ascending[2] and ascending[2] == ascending[3]): # checks if at least two unique digits present
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
else:
    count = 1
    print(" > 0")
    print(f"{userInput} reaches 0 via Kaprekar's routine in {count} iterations")
    exit()

print()
print(f"{userInput} reaches 6174 via Kaprekar's routine in {count} iterations")
