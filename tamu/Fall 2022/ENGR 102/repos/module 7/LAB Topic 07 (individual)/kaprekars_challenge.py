# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.29.1: LAB: Kaprekar's constant challenge
# Date:         07 October 2022

total = 0
index = [0, 0, 0, 0]

def increment():
    index[3] += 1
    i = 1
    while i < 4:
        if index[i] == 10:
            index[i - 1] += 1
            index[i] = 0
            i -= 1
            continue
        i += 1

iteration = 0
while iteration < 10000:
    #print(index)
    count = 0

    if not (index[0] == index[1] and index[1] == index[2] and index[2] == index[3]):
        ascending = sorted(index)
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

            if ascending == [6, 1, 7, 4]:
                break
    else:
        count = 1

    #print(count)
    total += count
    #print(total)
    increment()
    iteration += 1
total -= 2

print(f"Kaprekar's routine takes {total} total iterations for all four-digit numbers")
