#This file contains classes for different types of Players that might play this
#game.
import random
import RTTTBoard
import copy


class HumanPlayer:
    def __init__(self,mainGame,board,canvas):
        self.mainGame = mainGame
        self.board = board
        self.canvas = canvas

    def decideMove(self):
        self.canvas.bind("<Button-1>",self.gameClick)

    def gameClick(self,event):
        self.board.click(event)
        self.mainGame.playerTurn()


class RandomPlayer:
    def __init__(self,mainGame,board):
        self.mainGame = mainGame
        self.board = board

    def decideMove(self):
        legalmoves = self.board.legalmoves()
        move = legalmoves[ random.randint(0,len(legalmoves)-1)]
        self.board.makeMove(move[0],move[1])
        self.mainGame.playerTurn()




class AIPlayer:
    def __init__(self,mainGame,playernum,board):
        self.mainGame = mainGame
        self.playernum = playernum
        self.board = board

        # self.r
        # self.c

    def decideMove(self):
        depth = 6
        max = float('-inf')
        for (i, j) in (self.board.legalmoves()):
            value = self.minimax(i, j, 6, True)
            if value >= max:
                max = value
                (x, y) = (i, j)
        self.board.makeMove(x,y)



            # value := max(value, minimax(i, j, 6, TRUE))
            # if the current (i, j) has the max value:
            #   self.r = i
            #   self.c = j
            # board.deleteMove(i, j)


    def heuristic(self, board):
        if type(self.board).__name__ == 'TTTBoard':
            return self.TTTheuristic(board)
        elif type(self.board).__name__ == 'RTTTBoard':
            return self.RTTThueristic(board)
        else:
            return 0

    def TTTheuristic(self, board):
        if self.board.grid[1][1] == self.playernum:
            return 50
        if self.board.grid[1][1] == 3 - self.playernum:
            return -50
        else:
            return 0

    #You write this
    def RTTTheuristic(self, board):
        if self.board.grid[4][4] == self.playernum:
            return 50
        elif self.board.grid[4][4] == 3 - self.playernum:
            return -50
        else:
            return 0

        #if we havw two Xs in a row:


    def minimax(self, i, j, depth, maximizingPlayer):
        copyBoard = copy.deepcopy(self.board)
        copyBoard.makeMove(i, j)

        call = copyBoard.winner()
        if depth == 0 or call != 0:
            if self.playernum == call:
                return 100
            elif self.playernum == 3 - call :
                return -100
            if call == 3:
                return 0
            if call == 0:
                return self.heuristic(copyboard)

        if maximizingPlayer:
            bestvalue = -100
            for (x, y) in copyBoard.legalmoves():
                # copyBoard = copy.deepcopy(self.board)

                value = minimax(x, y, depth - 1, False)
                bestvalue = max(bestvalue, value)
            return bestvalue


        else: #minimizing player
            bestvalue = 100
            for (x, y) in copyBoard.legalmoves():
                # copyBoard = copy.deepcopy(self.board)
                # self.board.copyBoard.makeMove(i, j)
                value = minimax(x, y, depth - 1, True)
                bestvalue = min(bestvalue, value)
            return bestvalue
