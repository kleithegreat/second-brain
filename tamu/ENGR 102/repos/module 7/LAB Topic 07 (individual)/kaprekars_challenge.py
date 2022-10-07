# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.29.1: LAB: Kaprekar's constant challenge
# Date:         07 October 2022

count = 0
ascending = [0, 0, 0, 0]
def increment():
    ascending[3] += 1
    i = 0
    while i < 4:
        if ascending[i] == 10:
            ascending[i - 1] += 1
            ascending[i] = 0
            i -= 1
            continue
        i += 1

iteration = 0
while iteration < 10000:
    while not (ascending[0] == ascending[1] and ascending[1] == ascending[2] and ascending[2] == ascending[3]):
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

        if ascending == [6, 1, 7, 4]:
            break
    increment()
    iteration += 1

print(f"Kaprekar's routine takes {count} total iterations for all four-digit numbers")
