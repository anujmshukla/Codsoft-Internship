# Name            : Anuj Mukesh Shukla
# College         : Saffrony Institute of Technology
# File Name       : ChatBot.py
# File Task       : This is an file whose task is to take user message and respod it to according to the question asked  
# Support Files   : None
# Dependent Files : Knowledge.py 
# Email Id        : anujmshukla2002@gmail.com
# Task Title      : CHATBOT WITH RULE-BASED RESPONSES
# Description     : Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow

import re
import Knowledge as KB

def checkAllMessages(splitUserInput):
    # Responses ----------------------------------------------------
    highestProbList = KB.trigger(splitUserInput)

    bestMatch = max(highestProbList,key=highestProbList.get)
    # print(highestProbList)
    if(highestProbList[bestMatch]<1):
        return KB.unknown()
    else:
        return bestMatch

splitUserInput=[]

def getResponse(userInput):
    # Splitting message into words and making them all lowercase for easy analysis
    splitUserInput = re.findall(r'\w+', userInput.lower())
    # in the above patten match the w+ is actually a class in "re" which is equal to [a-zA-Z0-9_] 
    # now whole function will only allow to pass the alphanumecial chararter and remove all othe things 
    # print(splitUserInput)
    response = checkAllMessages(splitUserInput)
    return response

# Taking input and sending it for processing and then providing output
while True:
    userInput = input("You: ")
    botOutput = getResponse(userInput)
    print("Bot:", botOutput)