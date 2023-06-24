# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Quinn Hamilton
#               Jinyu Zhou
#               Joaquin Torres
#               
# Section:      522
# Assignment:   Topic 8 Lab: ASCII clock
# Date:         17 October 2022

# asks user for input and initalizes grid array for printing
userInput = input("Enter the time: ")
grid = ["", "", "", "", ""]

# creates a dictionary to translate from user inputed text to individual lines to print
# each cell describes one character from top to bottom as the array indicies increase
translate = {
    "0": ["000 ", "0 0 ", "0 0 ", "0 0 ", "000 "],
    "1": [" 1  ", "11  ", " 1  ", " 1  ", "111 "],
    "2": ["222 ", "  2 ", "222 ", "2   ", "222 "],
    "3": ["333 ", "  3 ", "333 ", "  3 ", "333 "],
    "4": ["4 4 ", "4 4 ", "444 ", "  4 ", "  4 "],
    "5": ["555 ", "5   ", "555 ", "  5 ", "555 "],
    "6": ["666 ", "6   ", "666 ", "6 6 ", "666 "],
    "7": ["777 ", "  7 ", "  7 ", "  7 ", "  7 "],
    '8': ["888 ", "8 8 ", "888 ", "8 8 ", "888 "],
    "9": ["999 ", "9 9 ", "999 ", "  9 ", "999 "],
    ":": ["  ", ": ", "  ", ": ", "  "]
}

# adds each line to the grid array to print according to the user input
for i in userInput:
    for j in range(5):
        grid[j] += translate[i][j]

# prints the time line by line with a for loop
print() # print new line first
for i in range(5):
    print(grid[i])
