# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   9.16.1: LAB: Small functions
# Date:         24 October 2022

def parta(rSphere: float, rHole: float):
    from math import pi # imports only the pi constant from the math module
    return (4 * pi / 3) * (rSphere ** 2 - rHole ** 2) ** (3 / 2)

def partb(n: int):
    for i in range(1, n, 2): # iterates over all odd numbers from 1 to n
        ints =[]
        for j in range(i, n, 2):
            ints.append(j)
            if sum(ints) == n:
                return ints
            elif sum(ints) > n:
                break
    return False

def partc(char, name, company, email):
    longest = max(len(name), len(company), len(email)) # finds the length of the longest input
    border = "".join([char for i in range(longest + 6)])
    line2 = f"{char}  {name:^{longest}}  {char}"
    line3 = f"{char}  {company:^{longest}}  {char}"
    line4 = f"{char}  {email:^{longest}}  {char}"
    return f"{border}\n{line2}\n{line3}\n{line4}\n{border}"

def partd(list):
    # if else statement finds the median depending on if the given list has an even or odd number of items
    if len(list) % 2 == 0:
        median = (sorted(list)[(len(list) // 2) - 1] + sorted(list)[(len(list) // 2)]) / 2
    else:
        median = sorted(list)[(len(list) // 2)]
    return (min(list), median, max(list))

def parte(times, distances):
    # velocity equals difference in distance divided by difference in time
    return [(distances[i + 1] - distances[i]) / (times[i + 1] - times[i]) for i in range(len(times) - 1)]
    
def partf(nums):
    # algorithm finds every possible combination of two numbers in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 2026:
                return nums[i] * nums[j]
    return False
