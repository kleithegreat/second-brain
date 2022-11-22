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

def displayRules():
    print("Rules")

def displayOptions():
    print("[1] Show instructions")
    print("[2] Show rules")
    print("[3] Play")
    print("[4] Open saved game")
    print("[5] Quit")

def displayInstructions():
    print("Instructions")

def startGame():
    currentGame = Game()
    currentGame.play()

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
        
class Game:    
    def __init__(self):
        self.board = [[f" {chr(9675)} " for i in range(7)] for j in range(6)]
        
    def play(self):
        turn = True
        while True:
            self.displayBoard()
            if turn:
                print("Player 1 to move.")
            else:
                print("Player 2 to move.")
            try:
                self.move(turn, self.getMove())
                turn = not turn
            except ValueError:
                print("Column is full! Try again.")
            if turn:
                if self.checkWin(" x "):
                    print("Player 1 wins!")
                    break
            else:
                if self.checkWin(f" {chr(9679)} "):
                    print("Player 2 wins!")
                    break
            
    def checkWin(self, turn: str): # TODO: DOESNT WORK PROPERLY
        for i, v in enumerate(self.board):
            for j, b in enumerate(v):
                if b != f" {chr(9675)} ":
                    try:
                        for k in range(4):
                            if self.board[i][j + k] != turn:
                                break
                            else:
                                return True
                    except:
                        continue
                    try:
                        for i in range(4):
                            if self.board[i + k][j] != turn:
                                break
                            else:
                                return True
                    except:
                        continue
                    try:
                        for i in range(4):
                            if self.board[i + k][j + k] != turn:
                                break
                            else:
                                return True
                    except:
                        continue
                    try:
                        for i in range(4):
                            if self.board[i + k][j - k] != turn:
                                break
                            else:
                                return True
                    except:
                        continue
        return False
            
    def getMove(self):
        validCols = ["a", "b", "c", "d", "e", "f", "g"]
        while True:
            column = input("Enter a column (Q to quit): ")
            if column.lower() == "q":
                exit()
            if column.lower() in validCols:
                return validCols.index(column)
            else:
                print("Invalid input! Please try again.")
        
    def move(self, turn: bool, col: int):
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
            for j in self.board[i]:
                print(j, end="")
            print()
    
    def saveGameToFile(self):
        with open("connect4game.txt", "w") as f: # WILL OVERWRITE PREVIOUS SAVED GAME, TODO: inform player, open saved game feature?
            f.write(self.board)
        
    def openGameFromFile(self): # TODO: check file format, make sure is readable
        with open("connect4game.txt", "r") as f:
            self.board = f.read()
    
def main():
    while True:
        print("\nWelcome to Connect 4! What would you like to do? (Type a number)")
        displayOptions()
        
        choice = getChoice()
        if choice == 1:
            displayInstructions()
        elif choice == 2:
            displayRules()
        elif choice == 3:
            startGame()
        elif choice == 4:
            pass #TODO: add startgame with existing game
        else:
            exit()
        
if __name__ == "__main__":
    main()
