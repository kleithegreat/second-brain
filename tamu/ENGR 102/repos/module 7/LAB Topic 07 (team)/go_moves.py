board = [[" . " for i in range(9)] for j in range(9)]

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

turnBlack = True

while True:
    for i in range(8, -1, -1):
        for j in range(9):
            print(board[i][j], end = "")
        print()
    if turnBlack:
        print("Black to move")
    else:
        print("White to move")
    userInput = input("Enter a coordinate: ")
    if userInput == "stop" or userInput == "Stop":
        break
    if not (userInput[0].lower() in coordinates.keys() and int(userInput[1]) in range(1, 10)):
        print("Your coordinate is not valid! Try again.")
        continue
    elif not board[int(userInput[1]) - 1][coordinates.get(userInput[0].lower())] == " . ":
        print("Space is occupied! Try again.")
        continue
    else:
        if turnBlack:
            board[int(userInput[1]) - 1][coordinates.get(userInput[0].lower())] = f" {chr(9679)} "
        else:
            board[int(userInput[1]) - 1][coordinates.get(userInput[0].lower())] = f" {chr(9675)} "
        turnBlack = not turnBlack
