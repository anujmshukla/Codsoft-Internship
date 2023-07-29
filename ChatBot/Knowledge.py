# Name            : Anuj Mukesh Shukla
# College         : Saffrony Institute of Technology
# File Name       : Knowledge.py
# File Task       : This is an file which contain knowledge of chatbot as well as some string matching pattent functions which return the list of message with an amount of match percentage with question asked by user   
# Support Files   : This file is support file of chatbot
# Dependent Files : None 
# Email Id        : anujmshukla2002@gmail.com
# Task Title      : CHATBOT WITH RULE-BASED RESPONSES
# Description     : Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow



def messageProbabilityCalculator(userMessage, recognizedWords, singleResponse=False, requiredWords=[]):
    # meaning of each variable
    # userMessage = what ever the user have enter in an form of array with splited words in an sentence 
    # recognizedWords = array words that are need to be present in user message to reply coressponding message as a bot reply 
    # requiredWords =  array that have some words that must be compulory present in "userMessage" in order to reply coressponding message as a bot reply  
    # singleResponse = used to control response i.e is this is true means no need that "requiredWords" must compulsory present in "userMessage" if false then it is compulsory  
    
    messageProbability = 0
    hasRequiredWords = True
    
    #haseRequiredWords = vaiable used to denote that "requiredWords" array words are present in "userMessage" or not

    # Count how many words are present in each predefined message
    for word in userMessage:
        if word in recognizedWords:
            messageProbability += 1

    # Calculating the probability of the recognized word
    accuracyPercentage = float(messageProbability) / float(len(recognizedWords))

    # Check if required words are present in the user message
    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break
    
    if hasRequiredWords or singleResponse:
        return int(accuracyPercentage * 100)
    else:
        return 0 
    
highestProbList = {}
#heat  "highestProbList = {}" ia an assocative array in which the response which was need to send by the machine is used as index 

def response(splitUserInput,botResponse, listOfWords, singleResponse=False, requiredWords=[]):
    highestProbList[botResponse] = messageProbabilityCalculator(splitUserInput, listOfWords, singleResponse, requiredWords)

def unknown():
    response= "this knowlede is not present in my knowledgw base sorry :( ,We will try to update soon "
    return response

def trigger(splitUserInput):
    # from hear all the knowledge start 
    response( splitUserInput ,'hello!!', ['hello', 'hi', 'sup', 'hey', 'heyyo'], True, [])
    response( splitUserInput ,'i am made by Anuj M Shukla, Bachelor of Technology', ['who', 'make', 'you', 'owner', 'guru','developer'], True, [])
    response( splitUserInput ,'i am doing fine and you?', ['how', 'are', 'you', 'doing'], False, ['how'])
    response( splitUserInput ,'thank you!', ['i', 'love', 'your', 'response'], True, [])
    response( splitUserInput ,'Welcome! Pleasure is all mine', ['thanks', 'thx', 'you', 'care'], False, ['you'])
    response( splitUserInput ,'AI (Artificial Intelligence) is the broader field of creating machines that can perform tasks requiring human-like intelligence', ['what', 'is', 'ai','Artificial','Intelligence'], False, ['ai'])   
    response( splitUserInput ,'ML (Machine Learning) is a subset of AI that focuses on enabling machines to learn and improve from experience without explicit programming.',['what', 'is', 'ml','Machine','Learning'], False, ['ml'])
    response( splitUserInput ,'Great remains always healthy', ['fine', 'great', 'amazing', 'fit as fuck','supreb','amazing'], True, [])
    response( splitUserInput ,'AI (Artificial Intelligence) is the broader field of creating machines that can perform tasks requiring human-like intelligence, while ML (Machine Learning) is a subset of AI that focuses on enabling machines to learn and improve from experience without explicit programming.', ['what', 'is', 'ai', 'ml','and'], False, ['ai','ml'])
    return highestProbList