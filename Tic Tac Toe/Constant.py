# Name            : Anuj Mukesh Shukla
# College         : Saffrony Institute of Technology
# File Name       : ChatBot.py
# File Task       : This is an file whose task is to take user input and respod it to according min max algorith 
# Support Files   : Tic_Tac_Toe.py
# Dependent Files : None 
# Email Id        : anujmshukla2002@gmail.com
# Task Title      : TIC-TAC-TOE AI
# Description     : Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms



#initial setup Constant 
widthScreen = 600  #Pixel 
heightScreen = 600 #Pixel 
captionsScreen = "TIC TAC TOE GAME"

#Defining the colours of an screen 
bgColour="dark gray"
lineColour="light gray"
lineWidth=10

#defining rows and column for game
row=3
column=3
squareSize = widthScreen // row  #600/3=200 pixel


#defining the of the circle's parameter 
circleColour = "red"
circleRadius= squareSize // 4
circleWidth=15 


#defining the of the Cross's parameter 
#for descending lines 
crossOffset=50 #offset is the diffrence between the horizontal line and our line 
CrossWidth=20
crossColour = "Yellow"

#winning line settings
winLineOffset=20
winColorPlayer2=circleColour
winColorPlayer1=crossColour
winLineWidth=20