import tkinter
from PIL import ImageTk, Image
#from math import inf

"""
This class represents the state of a game of TicTacToe
It keeps track of a 3x3 grid, where each position of a grid is
1 if player 1 has claimed it
2 if player 2 has claimed it

"""
class TTTBoard:

    # These don't change from game to game, they should be static
    p1char = 'X'
    p2char = 'O'
    blankchar = ' '

    """ Initialize the board """
    def __init__(self,canvas):
        # 0 represents blank
        # 1 represents player 1
        # 2 represents player 2
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.canvas = canvas
        self.curPlayer = 1
        #This is one way to keep track of the end state of the game
        self.totalmoves = 0

    """ Return the plays whose turn it currently is """
    def currentPlayer(self):
        return self.curPlayer

    """ makeMove is changed slightly  to now receive a row and column
    directly, not a string. It doesn't have to return anything either"""
    def makeMove(self,r,c):
        if self.grid[r][c] == 0:
            self.grid[r][c] = self.curPlayer
            #Sneaky trick to switch players
            self.curPlayer = 3 - self.curPlayer
            self.totalmoves = self.totalmoves + 1

    def click(self,event):
        row = (event.x - 170)//180
        col = (event.y - 70)//180
        if 0 <= row < 3 and 0 <= col < 3:
            self.makeMove(row,col)

    def drawBoard(self):
        #kitten = ImageTk.PhotoImage(Image.open('kitten.jpg').resize((540,540),Image.ANTIALIAS))
        #self.canvas.create_image(460,300,image=kitten)
        #Draw the lines for the tictactoe grid
        for i in range(310,670,180):
            self.canvas.create_line(i,30,i,570)
        for i in range(210,570,180):
            self.canvas.create_line(130,i,670,i)
        #For each player, draw the appropriate piece
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 1:
                    self.canvas.create_oval(135+180*i,35+180*j,305+180*i,205+180*j,fill='red')
                elif self.grid[i][j] == 2:
                    self.canvas.create_oval(135+180*i,35+180*j,305+180*i,205+180*j,fill='blue')




    """ Prints out a string representation of this object.
    This is very minimal and bare bones string representation
    Yours should be more interesting"""

    def __str__(self):
        # This is one of many ways to do this
        ans = '-------\n'
        for row in self.grid:
            for pos in row:
                ans = ans + '|'
                if pos == 1:
                    ans = ans + TTTBoard.p1char
                elif pos == 2:
                    ans = ans + TTTBoard.p2char
                else:
                    ans = ans + TTTBoard.blankchar
            ans = ans + '|\n'
            ans = ans + '-------\n'
        return ans


    """ Return the current winner of this board.
        0 means the game is ongoing
        1 means Player 1 has won
        2 means Player 2 has won
        3 means a draw """
    def winner(self):
        #Horizontal tests
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != 0:
                return self.grid[i][0]
        #Vertical tests
        for j in range(3):
            if self.grid[0][j] == self.grid[1][j] == self.grid[2][j] and self.grid[0][j] != 0:
                return self.grid[0][j]
        #Forward Diagonal
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != 0:
            return self.grid[0][0]
        #Backwards Diagonal
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != 0:
            return self.grid[0][2]
        #Check for draws
        if self.totalmoves == 9:
            return 3
        else:
            return 0


    #Return a list of tuples of legal moves
    def legalmoves(self):
        res = []
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    res.append( (i,j) )
        return res
