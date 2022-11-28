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
# Assignment:   Lab: Topic 13
# Date:         21 November 2022

class Game:
    def __init__(self):
        self.board = [[f" {chr(9675)} " for i in range(7)] for j in range(6)]
        self.turn = True
        
    def play(self):
        self.displayBoard()
        while True:
            if self.turn:
                print("Player 1 to move.")
            else:
                print("Player 2 to move.")
            try:
                if self.move(self.turn, self.getMove()) == -1:
                    break
                self.displayBoard()
            except ValueError:
                print("Column is full! Try again.")
                continue
            except ZeroDivisionError:
                return
            if self.turn:
                if self.checkWin(" x "):
                    print("Player 1 wins!")
                    break
                self.turn = not self.turn
            else:
                if self.checkWin(f" {chr(9679)} "):
                    print("Player 2 wins!")
                    break
                self.turn = not self.turn
                
    def playExisting(self):
        try:
            self.openGameFromFile()
        except:
            print("There is no saved game!")
            return
        self.play()
            
    def checkWin(self, turn: str):
        for i, v in enumerate(self.board):
            for j, b in enumerate(v):
                if b != f" {chr(9675)} ":
                    try:
                        for k in range(4):
                            if self.board[i][j + k] != turn:
                                break
                            elif k == 3:
                                return True
                    except:
                        continue
                    try:
                        for k in range(4):
                            if self.board[i + k][j] != turn:
                                break
                            elif k == 3:
                                return True
                    except:
                        continue
                    try:
                        for k in range(4):
                            if self.board[i + k][j + k] != turn:
                                break
                            elif k == 3:
                                return True
                    except:
                        continue
                    try:
                        for k in range(4):
                            if self.board[i + k][j - k] != turn:
                                break
                            elif k == 3:
                                return True
                    except:
                        continue
        return False
            
    def getMove(self):
        validCols = ["a", "b", "c", "d", "e", "f", "g", "q", "s"]
        while True:
            column = input("Enter a column (Enter Q to quit, S to save game): ")
            if column.lower() in validCols:
                return validCols.index(column)
            else:
                print("Invalid input! Please try again.")
        
    def move(self, turn: bool, col: int):
        if col == 7:
            raise ZeroDivisionError
        elif col == 8:
            while True:
                try:
                    if input("Saving will overwrite the previous game. Would you like to continue? (Type \"yes\" to continue) ").lower() == "yes":
                        self.saveGameToFile()
                        return -1
                except:
                    print("Invalid input! Try again.")
                    continue
        for i, v in enumerate(reversed(self.board)):
            if v[col] not in [" x ", f" {chr(9679)} "]:
                if turn:
                    self.board[5 - i][col] = " x "
                    return
                else:
                    self.board[5 - i][col] = f" {chr(9679)} "
                    return
        raise ValueError
    
    def displayBoard(self):
        for i in range(7):
            print(f" {chr(i + 65).upper()} ", end = "")
        print()
        for i, v in enumerate(self.board):
            for j in v:
                print(j, end="")
            print()
    
    def saveGameToFile(self):
        boardInfo = ""
        for i in self.board:
            for j in i:
                if j == " x ":
                    boardInfo += "1,"
                elif j == f" {chr(9679)} ":
                    boardInfo += "2,"
                else:
                    boardInfo += "x,"
        boardInfo += f"\n{self.turn}"
        with open("connect4game.txt", "w") as f:
            f.write(boardInfo)
        
    def openGameFromFile(self):
        with open("connect4game.txt", "r") as f:
            boardData = f.readline()
            self.turn = bool(f.readline())
        
        boardData = boardData[:len(boardData) - 2]
        boardData = boardData.replace("x", f" {chr(9675)} ")
        boardData = boardData.replace("1", " x ")
        boardData = boardData.replace("2", f" {chr(9679)} ")
        boardData = boardData.split(",")
        
        self.board = []
        row = []
        for i, v in enumerate(boardData):
            if (i + 1) % 7 != 0:
                row.append(v)
            else:
                row.append(v)
                self.board.append(row)
                row = []

def displayRules():
    print()
    print("Rules")

def displayOptions():
    print("[1] Show instructions")
    print("[2] Show rules")
    print("[3] Play")
    print("[4] Open saved game")
    print("[5] Exit")

def displayInstructions():
    print()
    print("Instructions")

def startGame():
    currentGame = Game()
    currentGame.play()
    
def openGame():
    currentGame = Game()
    currentGame.playExisting()

def getChoice():
    while True:
        try:
            choice = int(input())
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid input! Try again.")
                continue
        except:
            print("Invalid input! Try again.")
            continue

def main():
    while True:
        print("\nWelcome to Connect 4! What would you like to do? (Type a number and press enter)")
        displayOptions()
        
        choice = getChoice()
        if choice == 1:
            displayInstructions()
        elif choice == 2:
            displayRules()
        elif choice == 3:
            startGame()
        elif choice == 4:
            openGame()
        else:
            #TODO: ADD TURTLE GRAPHICS
            break
        
if __name__ == "__main__":
    main()
