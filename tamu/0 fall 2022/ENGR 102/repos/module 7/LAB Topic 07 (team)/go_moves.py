# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               Agustin Portillo
# Section:      522
# Assignment:   Topic 7 Lab: Go Moves
# Date:         07 October 2022

# initializes a 9 by 9 2D array to represent the board using a list comprehension, blank spaces are represented with " . "
board = [[" . " for i in range(9)] for j in range(9)]

# this dictionary is used to convert the coordinate from the user into an array index that can be used to retrieve or store data in the board array
coordinates = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
}

# this variable determines whether the program should place a black or white marker on the board and is flipped after every successful move
turnBlack = True

# executes the inside code until the user types "stop" or "Stop" in the prompt for coordinates
while True:
    # this nested for loop prints the properly formatted board according to the coordinate system
    for i in range(8, -1, -1):
        for j in range(9):
            print(board[i][j], end = "")
        print()

    # prints to the user whose turn it is based on the variable turnBlack
    if turnBlack:
        print("Black to move")
    else:
        print("White to move")

    # takes the users input as a string
    userInput = input("Enter a coordinate: ")

    # breaks out of the loop and thus stops the program if the user types "stop" or "Stop"
    if userInput == "stop" or userInput == "Stop":
        break

    # enclosed in a try except statement in case the user types a string that is not a coordinate which would cause an exception
    try:
        # checks if the first character of the coordinate is key value in the coordinates dictionary and if the second character is an integer in range [1, 9] inclusive
        # if the conditions are not met, a message is printed telling the user the coordinate is not valid
        if not (userInput[0].lower() in coordinates.keys() and int(userInput[1]) in range(1, 10)):
            print("Your coordinate is not valid! Try again.")
            continue

        # if coordinate is verified to be valid, this if statement checks whether the space is already occupied or not
        # if the condition is not met, a message is printed telling the user the space is already occupied
        elif not board[int(userInput[1]) - 1][coordinates.get(userInput[0].lower())] == " . ":
            print("Space is occupied! Try again.")
            continue

        # given the coordinate is valid and unoccupied, a black or white marker is placed on the coordinate depending on the current turn given by whether boolean turnBlack is true or false
        else:
            if turnBlack:
                board[int(userInput[1]) - 1][coordinates.get(userInput[0].lower())] = f" {chr(9679)} "
            else:
                board[int(userInput[1]) - 1][coordinates.get(userInput[0].lower())] = f" {chr(9675)} "

            # boolean turnBlack is flipped after every successful turn
            turnBlack = not turnBlack
    except:
        print("Your coordinate is not valid! Try again.")
