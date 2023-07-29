# Name            : Anuj Mukesh Shukla
# College         : Saffrony Institute of Technology
# File Name       : ChatBot.py
# File Task       : This is an file whose task is to take user input and respod it to according min max Algorithm  
# Support Files   : None
# Dependent Files : Constant.py 
# Email Id        : anujmshukla2002@gmail.com
# Task Title      : TIC-TAC-TOE AI
# Description     : Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms



# importing modules for making game
import copy
import random
import sys
import numpy as np 
import pygame
import Constant as const


#pygame initilization or setup 
pygame.init()
# creating screen
screen = pygame.display.set_mode((const.widthScreen,const.heightScreen))
#setting Captions 
pygame.display.set_caption(const.captionsScreen)
#setting screen colour 
screen.fill(const.bgColour)

#making game's logic or console board which is going to control everything's state in this world of tic tak toe  
class Board:
    # this __init__ methrod will call everytime whenever we creat our game object 
    # this methrod takes one parameter i.e "self" which means taking instant of it own class it is like "this" keyword in java  
    def __init__(self):
        #creating an 2 dimentional array ie full of zero that represent the state of marked boxed by whome
        self.squares = np.zeros((const.row,const.column))
        #creating an 2 dimentional array that keep the record of the empty squares 
        self.emptySquares = self.squares # at starting all aquares are empty 
        #creating variable that keep the record of the marked squares in digit no array 
        self.markedSquares = 0  #this will help us to know when our board is full 
    
    #function which is used to know that who wins befor draw 
    def finalState(self, Show=False):
        # Hear show variable is an Boolean variable which is used to know that game is over and anyone is win
        # return 0 if at this particular instant there is no win (this does't mean draw)
        # return 1 if player 1 wins 
        # retuen 2 if player 2 win
        
        # vertical wins
        # for cheecking for vertical wins we have to loop for all colums and cheeck 
        for col in range(const.column):
            #below is cheeckng that in column if ther same player number then he wins 
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                #hear if any of the play win the to draw line we use below given code 
                if Show:
                    # lets draw the line acording whoever win
                    if self.squares[0][col]==2:
                        color = const.winColorPlayer2
                    else:
                        color = const.winColorPlayer1
                    ipos= const.squareSize*col+const.squareSize//2,const.winLineOffset
                    fpos= const.squareSize*col+const.squareSize//2,const.squareSize*3-const.winLineOffset 
                    pygame.draw.line(screen,color,ipos,fpos,const.winLineWidth)
                return self.squares[0][col] #hear wer are returing that player number whose value is found in an whole column 
       
        # horizontal Wins
        # for cheecking for horizontal wins we have to loop for all rows and cheeck 
        for row in range(const.row):
            #below is cheeckng that in row if ther same player number then he wins 
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                #hear if any of the play win the to draw line we use below given code 
                if Show:
                    # lets draw the line acording whoever win
                    if self.squares[row][0]==2:
                        color = const.winColorPlayer2
                    else:
                        color = const.winColorPlayer1
                    ipos= const.winLineOffset,const.squareSize*row+const.squareSize//2
                    fpos= const.squareSize*3-const.winLineOffset,const.squareSize*row+const.squareSize//2 
                    pygame.draw.line(screen,color,ipos,fpos,const.winLineWidth)
                    
                return self.squares[row][0] #hear wer are returing that player number whose value is found in an whole row
        
        # descending Diagonal win
        #below is cheeckng that in diagonal if there is same player number then he wins 
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if Show:
                # lets draw the line acording whoever win
                if self.squares[1][1]==2:
                    color = const.winColorPlayer2
                else:
                    color = const.winColorPlayer1
                ipos= const.winLineOffset,const.winLineOffset
                fpos= const.squareSize*3-const.winLineOffset,const.squareSize*3-const.winLineOffset 
                pygame.draw.line(screen,color,ipos,fpos,const.winLineWidth)
                    
            return self.squares[1][1] #hear wer are returing that player number whose value is found in an whole decreasing diagonal
        
        # Accending Diagonal win
        #below is cheeckng that in diagonal if there is same player number then he wins 
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            if Show:
                # lets draw the line acording whoever win
                if self.squares[1][1]==2:
                    color = const.winColorPlayer2
                else:
                    color = const.winColorPlayer1
                ipos= const.winLineOffset,const.squareSize*3-const.winLineOffset
                fpos= const.squareSize*3-const.winLineOffset,const.winLineOffset 
                pygame.draw.line(screen,color,ipos,fpos,const.winLineWidth)
                    
            return self.squares[1][1] #hear wer are returing that player number whose value is found in an whole accreasing diagonal
        
        
        #if no one wins then retuen zero 
        return 0             
     
    # Function used to mark that which cell is filled by which player
    def mark_sqt(self, col, row,  player):
        self.squares[row][col] = player 
        self.markedSquares += 1
    
    # we cant mark the square that is already marked hence making methrod to cheeck that 
    def cheeckSquare(self,row,col):
        return self.squares[row][col]==0
    
    #this function will return the list where all the empty squares are placed 
    def getEmptySquare(self):
        emptySquares = []
        for row in range(const.row):
            for col in range (const.column):
                if self.cheeckSquare(row , col):
                    emptySquares.append((row,col))
        return emptySquares
    
    #return true if whole square is fill
    def isFull(self):
        return self.markedSquares==9
    
    #return true if no square is fill
    def isEmpty(self):
        return self.markedSquares==0

class AI:
    
    def __init__(self, level=1, player=2):
        self.level = level 
        self.player = player
    
    #choose random block to mark by ai 
    def randomChoise(self, board):
        emptySquares = board.getEmptySquare()
        index = random.randrange(0, len(emptySquares))
        return emptySquares[index] #this will return the (row,col)

    def minimax(self, board, maximizing):
        # Cheecking Terminal cases i.e if any player wins or not
        case = board.finalState()
        
        # if case is 1 then player 1 wins 
        if case == 1:
            return 1, None #returing an array in which there are two things i.e "evaluation" and "best move"
        # if case is 2 then player 2 wins
        elif case == 2:
            return -1, None
        #draw between both player
        elif board.isFull():
            return 0, None
        
        #maximixing Function 
        if maximizing:
            maxEval = -100
            bestMove = None
            emptySquares = board.getEmptySquare()

            for (row, col) in emptySquares:
                tempBoard = copy.deepcopy(board)
                tempBoard.mark_sqt(col, row, self.player)
                eval, _ = self.minimax(tempBoard, False)
                # print(tempBoard.squares)
                if eval > maxEval:
                    maxEval = eval
                    bestMove = (row, col)

            return maxEval, bestMove
        
        #minimizing Function 
        else:
            minEval = 100
            bestMove = None
            emptySquares = board.getEmptySquare()

            for (row, col) in emptySquares:
                tempBoard = copy.deepcopy(board)
                tempBoard.mark_sqt(col, row, 1)
                eval, _ = self.minimax(tempBoard, True)
                # print(tempBoard.squares)
                if eval < minEval:
                    minEval = eval
                    bestMove = (row, col)

            return minEval, bestMove
        
        
    def eval(self, mainBoard):
        if self.level == 0:
            eval ='random'
            # then we can mark in board randomly 
            move = self.randomChoise(mainBoard)
        else:
            # minimax algorithm
            eval, move = self.minimax(mainBoard, False)
        
        print(f'ai has choosen to mark the square in post {move} with an evaluation of {eval}')
        return move
            
#making game grapic board means how it look and it feel alos graphis board will send information to console or logic board  
class Game:
    # this __init__ methrod will call everytime whenever we creat our game object 
    # this methrod takes one parameter i.e "self" which means taking instant of it own class it is like "this" keyword in java  
    def __init__(self):
        #this is callled nested object i.e anyone creat game object will automatically creat board object and it can be accessable by variable name hear it is "board"
        self.board = Board()
        #making Ai object
        self.ai = AI()
        self.player = 1
        self.gameMode= 'ai' #2 gamming mode i.e ai or pvp
        self.running = True  #this shows that game is ruinning or not. if true then running if false then  not running 
        self.showLines()
        
    def showLines(self):
        #vertical Lines 
        #pygame.draw.line(platform, colour ,starting_point(x,y), ending_point(x,y), width_of_line )
        pygame.draw.line(screen,const.lineColour,(const.squareSize,0),(const.squareSize,const.heightScreen),const.lineWidth)
        pygame.draw.line(screen,const.lineColour,((const.squareSize*2),0),((2*const.squareSize),const.heightScreen),const.lineWidth)
        #horizontal Lines
        pygame.draw.line(screen,const.lineColour,(0,const.squareSize),(const.heightScreen,const.squareSize,),const.lineWidth)
        pygame.draw.line(screen,const.lineColour,(0,(const.squareSize*2)),(const.heightScreen,(2*const.squareSize)),const.lineWidth)
    
    # creating new methrod to chnage player after every one block is marked
    def nextTurn(self):
        self.player = (self.player % 2) +1 # if (1%2)=1 then 1+1 =2 and if (2%2)=0 then 0+1 = 1                     
    
    #making class to show figure on click by user according to the player 
    #the player 1 will put cross x and player 2 will put circle o
    def  drawFigure(self,row,col):
        if self.player == 1:
            #draw Cross we need two line one is acessnding line and another is descend line 
            #descending Line
            crossStartDescending=(col*const.squareSize+const.crossOffset,row*const.squareSize+const.crossOffset)
            crossEndDescending=(col*const.squareSize+const.squareSize-const.crossOffset,row*const.squareSize+const.squareSize-const.crossOffset) 
            pygame.draw.line(screen,const.crossColour,crossStartDescending,crossEndDescending,const.CrossWidth)
            #Ascending line
            crossStartAscending=(col*const.squareSize+const.crossOffset,row*const.squareSize+const.squareSize-const.crossOffset)
            crossEndAscending=(col*const.squareSize+const.squareSize-const.crossOffset,row*const.squareSize+const.crossOffset) 
            pygame.draw.line(screen,const.crossColour,crossStartAscending,crossEndAscending,const.CrossWidth)
            
        elif self.player == 2:
            cicleCenter=(col*const.squareSize + const.squareSize //2,row*const.squareSize + const.squareSize//2) 
            # draw circle
            # pygame.draw.circle(platfrom,colour,center,radius,stroke with)
            pygame.draw.circle(screen,const.circleColour,cicleCenter,const.circleRadius,const.circleWidth)
    
    def isover(self):
        return self.board.finalState(True) !=0 or self.board.isFull()  #return true os game is over (when any of the one condition is true) otherwise false 
        
#our code entery point 
def main():
    #creating Game object here
    game = Game()
    #taking an instant of board class from game class 
    board = game.board
    #taking an instant of ai class from game class
    ai= game.ai
    #creating infinite loop 
    while True:
        #user attempts to close the game window, the program will properly quit, releasing any allocated resources
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #below code is marking square by human     
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos) #this print statement show where you have beel clicked in pixel values, and it is 1D array 
            #  Converting pixel into Cols and rows  
            row = event.pos[1]//const.squareSize
            col = event.pos[0]//const.squareSize
            # print ("(",row,",",col,")")  # this show which row and column you have marked        
            if board.cheeckSquare(row,col) and game.running:
                #making Square
                board.mark_sqt(col,row,game.player)
                #displaying Figure 
                game.drawFigure(row,col)
                #changing player 
                game.nextTurn()
                # print(game.board.squares) #this print statement will show that the array that show mark deatil is marked or not 
                #if game is over then turn this off so that code does't crash 
                if game.isover():
                    game.running = False
            # else:
                # print("cell is already marked",row ,",",col,".")

        
        #below code is marking square by AI            
        if game.gameMode=='ai' and game.player == ai.player and game.running:
            #This will update the screen befor the ai mark 
            pygame.display.update()
            #AI Methrod calling 
            row, col = ai.eval(board) 
            #making Square
            board.mark_sqt(col,row,ai.player)
            #displaying Figure 
            game.drawFigure(row,col)
            #changing player 
            game.nextTurn() 
            #if game is over then turn this off so that code does't crash 
            if game.isover():
                    game.running = False     
            
        pygame.display.update()
       
            
#calling our main methrod 
main()