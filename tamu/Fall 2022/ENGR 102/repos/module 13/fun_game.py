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

from turtle import Turtle, Screen

class Game:
    def __init__(self):
        """
        Creates a new Game object. Takes no arguments. 
        Attribute "board" is a 2D array 7 long and 6 deep. 
        Attribute "turn" is true by default and is true when it is player 1's turn.
        """
        self.board = [[f" {chr(9675)} " for i in range(7)] for j in range(6)] # initializes a 6 tall 7 wide board
        self.turn = True # true if player 1's turn, false if player 2's turn
        
    def play(self):
        """
        Starts a new game.
        """
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
        """
        Starts a game from existing game data.
        """
        try:
            self.openGameFromFile()
        except:
            print("There is no saved game!")
            return
        self.play()
            
    def checkWin(self, turn: str):
        """Checks for whether either player has four pieces in a row.

        Args:
            turn (str): String representing the piece of the corresponding player who is being checked.

        Returns:
            boolean: true if player has 4 in a row, false if not
        """
        for i, v in enumerate(self.board): # iterates through every spot on the board and sees if it has four of the same value in a row
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
        """
        Reads input from the player

        Returns:
            int: index of the selected column of the board, 7 if player wants to quit, 8 if player wants to save the game
        """
        validCols = ["a", "b", "c", "d", "e", "f", "g", "q", "s"]
        while True:
            column = input("Enter a column (Enter Q to quit, S to save game): ")
            if column.lower() in validCols: # checks if user input is valid
                return validCols.index(column.lower())
            else:
                print("Invalid input! Please try again.")
        
    def move(self, turn: bool, col: int):
        """
        Checks if the player wants to quit or save the game and acts accordingly.
        If given a column index, this method places a piece in the corresponding column given the current turn.

        Args:
            turn (bool): true if player 1 to play, false if player 2 to play
            col (int): index of column where piece is supposed to go

        Raises:
            ZeroDivisionError: if player wants to quit the game
            ValueError: if the column selected is already full

        Returns:
            _type_: -1 if player confirms they want to save the game. otherwise returns nothing.
        """
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
        """
        Displays the current game board to the console.
        """
        for i in range(7): # displays the column letters first
            print(f" {chr(i + 65).upper()} ", end = "")
        print()
        for i, v in enumerate(self.board):
            for j in v:
                print(j, end="")
            print()
    
    def saveGameToFile(self):
        """
        Saves the current board and turn data to a file which can be read later.
        """
        boardInfo = ""
        for i in self.board:
            for j in i: # replaces baord data with filler data to avoid ascii error
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
        """
        Loads saved game data into current games board and turn boolean.
        """
        with open("connect4game.txt", "r") as f:
            boardData = f.readline() # board data is the first line of the file
            self.turn = bool(f.readline()) # current turn is the second line of the file
        
        boardData = boardData[:len(boardData) - 2]
        boardData = boardData.replace("x", f" {chr(9675)} ") # replaces filler data with board data to avoid ascii error
        boardData = boardData.replace("1", " x ")
        boardData = boardData.replace("2", f" {chr(9679)} ")
        boardData = boardData.split(",")
        
        self.board = []
        row = []
        for i, v in enumerate(boardData):
            if (i + 1) % 7 != 0: # separates 1D array into 2D array
                row.append(v)
            else:
                row.append(v)
                self.board.append(row)
                row = []

def displayRules():
    """
    Displays the basic rules of connect-4.
    """
    print()
    print("Players take turns putting pieces in columns.")
    print("Whoever gets four pieces in a row (horizontally, vertically, or diagonally) first wins.")

def displayOptions():
    """
    Displays the available options for the player.
    """
    print("[1] Show instructions")
    print("[2] Show rules")
    print("[3] Play")
    print("[4] Open saved game")
    print("[5] Exit")

def displayInstructions():
    """
    Displays some simple instructions for how to use the program.
    """
    print()
    print("Enter a number on the menu screen to do something.")
    print("To play, players take turns entering a column letter indicating in which column they would like to drop their piece.")
    print("When in the game, players can enter \"S\" to save the game, and \"Q\" to quit the game.")

def startGame():
    """
    Starts a new game.
    """
    currentGame = Game()
    currentGame.play()
    
def openGame():
    """
    Starts a game from existing game data.
    """
    currentGame = Game()
    currentGame.playExisting()

def getChoice():
    """
    Reads the players input and returns it if it is found to be valid.

    Returns:
        int: choice number of corresponding options
    """
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
    """
    Loads the game menu.
    """
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
            wn = Screen()
            rootwindow = wn.getcanvas().winfo_toplevel()
            rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
            tur = Turtle()
            tur.forward(200)
            tur.clone()
            break
        
if __name__ == "__main__":
    main()
