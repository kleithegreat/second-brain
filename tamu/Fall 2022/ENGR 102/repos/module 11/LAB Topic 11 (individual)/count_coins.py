# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   11.12.1: LAB: Counting coins
# Date:         07 November 2022

with open("game.txt", "r") as instructionsFile:
    instructions = instructionsFile.read().split("\n")
totalCoins = 0
coinChanges = []

try:
    i = 0
    while True:
        if instructions[i][:4] == "coin":
            if instructions[i][5] == "+":
                totalCoins += int(instructions[i][6:])
                coinChanges.append(instructions[i][6:])
            else:
                totalCoins -= int(instructions[i][6:])
                coinChanges.append(f"-{instructions[i][6:]}")
            i += 1
        elif instructions[i][:4] == "jump":
            if instructions[i][5] == "+":
                i += int(instructions[i][6:])
            else:
                i -= int(instructions[i][6:])
        elif instructions[i][:4] == "none":
                i += 1
except IndexError:
    print(f"Total coins collected: {totalCoins}")

coinChanges[:-1] = [i + "\n" for i in coinChanges[:-1]] # insert line breaks
with open("coins.txt", "w") as coins:
    for i in coinChanges:
        coins.write(i)
