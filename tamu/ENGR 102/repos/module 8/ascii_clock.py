# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               
#               
#               
# Section:      522
# Assignment:   Topic 7 Lab: Go Moves
# Date:         17 October 2022

userInput = input("Enter the time: ")
grid = ["", "", "", "", ""]

translate = {
    "0": ["000", "0 0", "0 0", "0 0", "000"],
    "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
    "2": ["222", "  2", "222", "2  ", "222"],
    "3": ["333", "  3", " 33", "  3", "333"],
    "4": ["4 4", "4 4", "444", "  4", "  4"],
    "5": ["555", "5  ", "555", "  5", "555"],
    "6": ["666", "6  ", "666", "6 6", "666"],
    "7": ["777", "  7", "  7", "  7", "  7"],
    '8': ["888", "8 8", "888", "8 8", "888"],
    "9": ["999", "9 9", "999", "  9", "  9"],
    ":": ["   ", " : ", "   ", " : ", "   "]
}

for i in userInput:
    for j in range(5):
        grid[j] += translate[i][j]
        try:
            if i != ":" and userInput[userInput.index(i) + 1] != ":":
                grid[j] += " "
        except IndexError:
            continue

for i in range(5):
    print(grid[i])
