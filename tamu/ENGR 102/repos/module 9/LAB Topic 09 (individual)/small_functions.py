# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   9.16.1: LAB: Small functions
# Date:         24 October 2022

def parta(rSphere: float, rHole: float):
    return (4 / 3) * (rSphere ** 2 - rHole ** 2) ** (3 / 2)

def partb(n: int):
    for i in range(1, n, 2):
        ints =[]
        for j in range(i, n, 2):
            ints.append(j)
            if sum(ints) == n:
                return ints
            elif sum(ints) > n:
                break
    return False

def partc(char: str, name: str, company: str, email: str):
    longest = max(len(name), len(company), len(email))