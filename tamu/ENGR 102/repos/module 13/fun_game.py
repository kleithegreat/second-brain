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
    print("[4] Quit")

def displayInstructions():
    print("Instructions")

def startGame():
    currentGame = Game()
    currentGame.displayBoard()

def getChoice():
    while True:
        try:
            choice = int(input())
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid input! Try again.")
                continue
        except:
            print("Invalid input! Try again.")
            continue
        
class Game:    
    def __init__(self):
        self.board = [[" . " for i in range(7)] for j in range(6)]
        
    def play():
        print()
        
    def move(self, turn, col):
        pass
    
    def displayBoard(self):
        for i, v in enumerate(self.board):
            for j in self.board[i]:
                print(j, end=" ")
            print()
    
    def saveGameToFile(self):
        with open("connect4game.txt", "w") as f: # WILL OVERWRITE PREVIOUS SAVED GAME, TODO: inform player, open saved game feature?
            f.write(self.board)
        
    def openGameFromFile(self): # TODO: check file format
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
        elif choice == 4:
            exit()
        else:
            startGame()
        
if __name__ == "__main__":
    main()
    