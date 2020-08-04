import TTTBoard
import RTTTBoard
import tkinter
from PlayerTypes import *
from PIL import ImageTk, Image


class GameCentral():

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Welcome to Game Central")
        self.canvas = tkinter.Canvas(self.root,height=800,width=800)
        self.canvas.pack()
        self.gameboard = None
        self.startscreen = {}
        self.startscreen['gameType'] = None
        self.startscreen['P1'] = None
        self.startscreen['P2'] = None
        self.startscreen['ready'] = False
        self.player1 = None
        self.player2 = None
        self.drawStartScreen()
        self.canvas.mainloop()

    ''' Each screen function is responsible for drawing the screen and setting
    up  the appropriate bindings

    Note: This is fairly messy GUI coding. A better way could have been to define a
    "Button" class, and use that Button class.
    '''
    def drawStartScreen(self):
        print(self.startscreen['ready'])
        #Delete anything else on the screen
        self.canvas.delete('all')
        if self.startscreen['gameType'] and self.startscreen['P1'] and self.startscreen['P2']:
            self.startscreen['ready'] = True
        #Draw the screen
        print('image')
        #kitten = ImageTk.PhotoImage(Image.open('kitten.jpg').resize((540,540),Image.ANTIALIAS))
        #self.canvas.create_image(460,300,image=kitten)
        self.canvas.create_text(400,100,text='Welcome to Game Central')
        #Game Choice
        if self.startscreen['gameType'] == 'TTT':
            self.canvas.create_rectangle(100,200,300,300, fill='yellow')
        else:
            self.canvas.create_rectangle(100,200,300,300)
        self.canvas.create_text(200,250,text='Play TicTacToe')
        if self.startscreen['gameType'] == 'RTTT':
            self.canvas.create_rectangle(500,200,700,300,fill='yellow')
        else:
            self.canvas.create_rectangle(500,200,700,300)
        self.canvas.create_text(600,250,text='Play Recursive TicTacToe')

        #Player 1
        self.canvas.create_text(400,325,text='Choose Player 1')
        if self.startscreen['P1'] == 'Human':
            self.canvas.create_rectangle(100,350,300,450, fill='yellow')
        else:
            self.canvas.create_rectangle(100,350,300,450)
        self.canvas.create_text(200,400,text='Human')
        if self.startscreen['P1'] == 'Random':
            self.canvas.create_rectangle(300,350,500,450, fill='yellow')
        else:
            self.canvas.create_rectangle(300,350,500,450)
        self.canvas.create_text(400,400,text='Random')
        if self.startscreen['P1'] == 'AI':
            self.canvas.create_rectangle(500,350,700,450, fill='yellow')
        else:
            self.canvas.create_rectangle(500,350,700,450)
        self.canvas.create_text(600,400,text='AI')


        self.canvas.create_text(400,475,text='Choose Player 2')
        if self.startscreen['P2'] == 'Human':
            self.canvas.create_rectangle(100,500,300,600, fill='yellow')
        else:
            self.canvas.create_rectangle(100,500,300,600)
        self.canvas.create_text(200,550,text='Human')
        if self.startscreen['P2'] == 'Random':
            self.canvas.create_rectangle(300,500,500,600, fill='yellow')
        else:
            self.canvas.create_rectangle(300,500,500,600)
        self.canvas.create_text(400,550,text='Random')
        if self.startscreen['P2'] == 'AI':
            self.canvas.create_rectangle(500,500,700,600, fill='yellow')
        else:
            self.canvas.create_rectangle(500,500,700,600)
        self.canvas.create_text(600,550,text='AI')


        #Start Button
        if self.startscreen['ready']:
            self.canvas.create_rectangle(300,650,500,750,fill='green')
        else:
            self.canvas.create_rectangle(300,650,500,750,fill='red')
        self.canvas.create_text(400,700,text='Start!')


        #Bind the mouse button
        self.canvas.bind("<Button-1>",self.startScreenClick)

    def startScreenClick(self,event):
        print("Start Screen was clicked")
        if 100 <= event.x <= 300 and 200 <= event.y <= 300 :
            self.startscreen['gameType'] = 'TTT'
            self.drawStartScreen()
        elif 500 <= event.x <= 700 and 200 <= event.y <= 300 :
            self.startscreen['gameType'] = 'RTTT'
            self.drawStartScreen()

        elif 100 <= event.x <= 300 and 350 <= event.y <= 450 :
            self.startscreen['P1'] = 'Human'
            self.drawStartScreen()
        elif 300 <= event.x <= 500 and 350 <= event.y <= 450 :
            self.startscreen['P1'] = 'Random'
            self.drawStartScreen()
        elif 500 <= event.x <= 700 and 350 <= event.y <= 450 :
            self.startscreen['P1'] = 'AI'
            self.drawStartScreen()
        elif 100 <= event.x <= 300 and 500 <= event.y <= 600 :
            self.startscreen['P2'] = 'Human'
            self.drawStartScreen()
        elif 300 <= event.x <= 500 and 500 <= event.y <= 600 :
            self.startscreen['P2'] = 'Random'
            self.drawStartScreen()
        elif 500 <= event.x <= 700 and 500 <= event.y <= 600 :
            self.startscreen['P2'] = 'AI'
            self.drawStartScreen()

        elif 300 <= event.x <= 500 and 650 <= event.y <= 750 and self.startscreen['ready']:
            print('GameTime!')
            if self.startscreen['gameType'] == 'TTT':
                self.gameboard = TTTBoard.TTTBoard(self.canvas)
            else:
                self.gameboard = RTTTBoard.RTTTBoard(self.canvas)

            if self.startscreen['P1'] == 'Human':
                self.player1 = HumanPlayer(self,self.gameboard,self.canvas)
            elif self.startscreen['P1'] == 'Random':
                self.player1 = RandomPlayer(self,self.gameboard)
            else:
                self.player1 = AIPlayer(self,1,self.gameboard)

            if self.startscreen['P2'] == 'Human':
                self.player2 = HumanPlayer(self,self.gameboard,self.canvas)
            elif self.startscreen['P2'] == 'Random':
                self.player2 = RandomPlayer(self,self.gameboard)
            else:
                self.player2 = AIPlayer(self,2,self.gameboard)

            self.playerTurn()

    def playerTurn(self):
        winner = self.gameboard.winner()
        if winner != 0:
            self.drawEndScreen(winner)
            return
        #Delete anything else on the screen
        self.canvas.delete('all')
        #Draw the game screen
        self.gameboard.drawBoard()
        #Draw a prompt for the player
        self.canvas.create_text(400,700,text=("Player " + str(self.gameboard.currentPlayer())+ "'s turn!"))
        #Bind the mouse button
        if self.gameboard.currentPlayer() == 1:
            curplayer = self.player1
        else:
            curplayer = self.player2
        curplayer.decideMove()
        #self.canvas.bind("<Button-1>",self.gameClick)

    def drawEndScreen(self,winner):
        self.canvas.delete('all')
        #Draw the final game screen
        self.gameboard.drawBoard()
        if winner != 3:
            self.canvas.create_text(400,700,text=('Player '+str(winner)+' wins!'))
        else:
            self.canvas.create_text(400,700,text=('It was a draw!'))
        self.canvas.create_rectangle(100,650,300,750)
        self.canvas.create_text(200,700,text='Play Again')
        self.canvas.create_rectangle(500,650,700,750)
        self.canvas.create_text(600,700,text='Quit')
        self.canvas.bind("<Button-1>",self.endClick)

    def endClick(self,event):
        if 100 <= event.x <= 300 and 650 <= event.y <= 750 :
            self.startscreen['gameType'] = None
            self.startscreen['P1'] = None
            self.startscreen['P2'] = None
            self.startscreen['ready'] = False
            self.drawStartScreen()
        elif 500 <= event.x <= 700 and 650 <= event.y <= 750 :
            #This ends the mainloop call, and the game.
            self.root.quit()


# The main function is much simpler in an event-driven programming setup
def main():
    m = GameCentral()


if __name__ == "__main__":
    main()
