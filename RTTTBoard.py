"""
This Lab is an implementation of a Recursive TicTacToe board

In recusrive TicTacToe, you play on a 3x3 grid of tictactoe boards.

Each player chooses a square to play on.

"""

import tkinter
import copy
from PIL import ImageTk, Image
class RTTTBoard:
    p1char = 'X '
    p2char = 'O '
    blankchar = '- '

    """ Initialize the board """
    def __init__(self,canvas):
        self.grid = []
        #this is the grid for the larger grid
        self.boxWinner = [[0,0,0],[0,0,0],[0,0,0]]
        self.canvas = canvas
        #this creates the bigger grid
        for i in range (0,9):
            self.grid.append([0,0,0,0,0,0,0,0,0])

        self.curPlayer = 1
        self.totalmoves = 0
        self.Nextbox = None
        self.r1 = 0
        self.c1 = 0

    def __deepcopy__(self,memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k,v in self.__dict__.items():
            if type(v).__name__ not in ('Canvas','PhotoImage'):
                setattr(result,k, copy.deepcopy(v,memo))

        return result

    """ Return the plays whose turn it currently is """
    def currentPlayer(self):
        return self.curPlayer
    #this fucntion will predict where the players next move should be
    def BoxCoordinate(self, a, b):
        self.a1 = a%3
        self.b1 = b%3
        return [self.a1, self.b1]



    """ Attempt to make the move described by the input string move
        if the move was valid, the board state should reflect that change
        and you should return True

        if the move was not valid, the board state should be unchanged,
        and you should return False """

# Make move fucntion
    def makeMove(self,r,c):
        #spilts up user input
        #moves = move.split()


        print(self.legalmoves())

        try:
            #r = int(moves[0])
            #c = int(moves[1])
            #calculate the bigger grid of where the user played
            self.r1 = r // 3
            self.c1 = c // 3
            #save the coordinates of the bigger box
            self.currentMove = [self.r1, self.c1]
            #only allow player to play anywhere when nextbox = none

            if self.Nextbox is not None:
                #if the player inputs a value that does not match the value next box wants it to play in it will return false
                if self.currentMove[0] != self.Nextbox[0] and self.currentMove[1] != self.Nextbox[1]:
                    return False



            #    return True
            if self.grid[r][c] == 0:
                #only allows player to play in the big box that has no value(a big box that is not won)
                if self.boxWinner[self.r1][self.c1] == 0:
                    self.grid[r][c] = self.curPlayer
                    box = self.BoxCoordinate(r,c)
                    self.Nextbox = box
                        #Sneaky trick to switch players
                    self.curPlayer = 3 - self.curPlayer
                    self.totalmoves = self.totalmoves + 1

                    return True
                else:
                    return False
            else:
                return False

        except:
            return False





    """ Prints out a string representation of this object """

# To create the board to print out on the terminal
    def __str__(self):

        ans = '* * * * * * * * * * * * * \n'
        for row in range (len(self.grid)):
            for col in range (len(self.grid[row])):
                if col == 0:
                    ans = ans + '* '
                if self.grid[row][col] == 1:
                    ans = ans + RTTTBoard.p1char
                elif self.grid[row][col] == 2:
                    ans = ans + RTTTBoard.p2char
                else:
                    ans = ans + RTTTBoard.blankchar
                if col == 2 or col == 5:
                    ans = ans + '* '

                if col == 8:
                    ans = ans + '*\n'
            if row == 2 or row == 5:
                ans = ans + '* * * * * * * * * * * * * \n'
        ans = ans + '* * * * * * * * * * * * * \n'
        return ans



    # You may want to write helper functions
    """ Return the current winner of this board.
        0 means the game is ongoing
        1 means Player 1 has won
        2 means Player 2 has won
        3 means a draw """

    def click(self,event):
        #Splits click up into 9x9
        row = (event.x - 130)//60
        col = (event.y - 30)//60
        #splits click up into a 3x3
        row1 = (event.x - 130)//180
        col1 = (event.y - 30)//180

        #only allows you to do this when the next move is a value
        if self.Nextbox is not None:

            #self.canvas.create_rectangle(130+row1*180,30 +col1*180, 310+row1*180,210+col1*180,fill='yellow')

            #only allows a move to be played if the next move matches the current 3x3 grid
            if self.a1 == row1  and self.b1 == col1 :


                self.makeMove(row,col)
        else :
            if 0 <= row < 9 and 0 <= col < 9:
                self.makeMove(row,col)





    def drawBoard(self):
        #Draw the lines for the tictactoe grid
        #coulmns
        self.DogCat = ImageTk.PhotoImage(Image.open('catdog.jpg').resize((540,540),Image.ANTIALIAS))
        #creates the highlighted box behind the RTTT board
        if self.Nextbox is not None:
            self.canvas.create_rectangle(130+ self.Nextbox[0]*180,30 +self.Nextbox[1]*180, 310+self.Nextbox[0]*180,210+self.Nextbox[1]*180,fill='yellow')
        else:
            #self.canvas.create_rectangle(130,30,670,570, fill = 'yellow')
            self.canvas.create_image(400,300, image = self.DogCat)


        for i in range(190, 670, 60):
            self.canvas.create_line(i , 30, i , 570)
        #row
        for i in range(90, 570, 60):
            self.canvas.create_line(130, i, 670 , i)
        #Fat Coloumn
        for i in range(130, 730, 180):
            self.canvas.create_line(i , 30, i , 570, fill = "hot pink", width = 3)
        #Fat row
        for i in range(30, 630, 180):
            self.canvas.create_line(130 , i, 670  , i , fill = "hot pink", width = 3)

        #For each player, draw the appropriate piece
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 1:
                    self.canvas.create_oval(130+60*i,30+60*j,185+60*i,85+60*j,fill='red')
                elif self.grid[i][j] == 2:
                    self.canvas.create_oval(130+60*i,30+60*j,185+60*i,85+60*j,fill='blue')



#Function to check the winner of the individual boxes and the big boxes aswell
    def winner(self):


        #Vertical tests for the smaller boxes
        for i in range(0,9):
            for j in range (0,8,3):
                if self.grid[i][j] == self.grid[i][j+1] == self.grid[i][j+2] and self.grid[i][j] != 0:


                    r1 = i//3
                    c1 = j//3
                    #only allows the reset to none on the first time winner is discovered
                    if self.boxWinner[r1][c1] == 0:
                        self.boxWinner[r1][c1] = self.grid[i][j]

                        self.Nextbox = None


                    for h in range (0,3):
                        for k in range (0,3):
                            if self.grid[h*3+r1][k*3+c1] == 0:
                                self.grid[h*3+r1][k*3+c1] = 3 - self.curPlayer


        #Horizontal tests for the smaller boxes
        for j in range(0,9):
            for i in range (0,8,3):
                if self.grid[i][j] == self.grid[i+1][j] == self.grid[i+2][j] and self.grid[i][j] != 0:

                    r1 = i//3
                    c1 = j//3
                    if self.boxWinner[r1][c1] == 0:
                        self.boxWinner[r1][c1] = self.grid[i][j]

                        self.Nextbox = None

                    for h in range (0,3):
                        for k in range (0,3):
                            if self.grid[h*3+r1][k*3+c1] == 0:
                                self.grid[h*3+r1][k*3+c1] = 3 - self.curPlayer
        #Forward Diagonal for the smaller boxes
        for i in range(0,8,3):
            for j in range (0,8,3):
                if self.grid[i][j] == self.grid[i+1][j+1] == self.grid[i+2][j+2] and self.grid[i][j] != 0:

                    r1 = i//3
                    c1 = j//3
                    if self.boxWinner[r1][c1] == 0:
                        self.boxWinner[r1][c1] = self.grid[i][j]
                        self.Nextbox = None

                    for h in range (0,3):
                        for k in range (0,3):
                            if self.grid[h*3+r1][k*3+c1] == 0:
                                self.grid[h*3+r1][k*3+c1] = 3 - self.curPlayer

        #Backwards Diagonal for the smaller boxes
        for i in range (0,8,3):
            for j in range (0,8,3):
                if self.grid[i][j+2] == self.grid[i+1][j+1] == self.grid[i+2][j] and self.grid[i][j+2] != 0:

                    r1 = i//3
                    c1 = j//3
                    if self.boxWinner[r1][c1] == 0:
                        self.boxWinner[r1][c1] = self.grid[i][j]
                        self.Nextbox = None
                    for h in range (0,3):
                        for k in range (0,3):
                            if self.grid[h*3+r1][k*3+c1] == 0:
                                self.grid[h*3+r1][k*3+c1] = 3 - self.curPlayer

        #Horizontal test for the latger grid
        for i in range(3):
            if self.boxWinner[i][0] == self.boxWinner[i][1] == self.boxWinner[i][2] and self.boxWinner[i][0] != 0:
                return self.boxWinner[i][0]
        #Vertical tests for the larger grid
        for j in range(3):
            if self.boxWinner[0][j] == self.boxWinner[1][j] == self.boxWinner[2][j] and self.boxWinner[0][j] != 0:
                return self.boxWinner[i][0]
        #Forward Diagonalfor the larger grid
        if self.boxWinner[0][0] == self.boxWinner[1][1] == self.boxWinner[2][2] and self.boxWinner[0][0] != 0:
            return self.grid[0][0]
        #Backwards Diagonal for the larger grid
        if self.boxWinner[0][2] == self.boxWinner[1][1] == self.boxWinner[2][0] and self.boxWinner[0][2] != 0:
            return self.boxWinner[0][2]

        #Draw tests:
        for i in range(3):
            for j in range(3):
                #if there is a draw on one of the board or the next box is full it will set next box to none so the player can play anywhere.
                if self.grid[i*3][j*3] != 0 and self.grid[i*3][j*3+1] != 0 and self.grid[i*3][j*3+2] != 0 and self.grid[i*3+1][j] != 0 and self.grid[i*3+1][j+1] != 0 and self.grid[i*3+1][j+2] != 0 and self.grid[i*3+2][j] != 0 and self.grid[i*3+2][j+1] != 0 and self.grid[i*3+2][j+2] != 0:
                    self.Nextbox = None

        #if the total moves are 81 and there are no winner then the entire game is a draw
        if self.totalmoves == 81:
            return 3
        else:
            return 0


    def legalmoves(self):
        res = []
        if self.Nextbox == None:
            for k in range(3):
                for h in range(3):
                    if self.boxWinner[k][h] == 0: #to only allow input in a non completed board
                        for i in range(9):
                            for j in range(9):
                                if self.grid[i][j] == 0:
                                    res.append( (i,j) )

        if self.Nextbox is not None:
            for i in range(3 * self.Nextbox[0],3 * self.Nextbox[0] + 3):
                for j in range(3 * self.Nextbox[1],3 * self.Nextbox[1]+ 3):
                    if self.grid[i][j] == 0:
                        res.append( (i,j) )

        return res
