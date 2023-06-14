import json
from random import randint
global question
question = json.load(open("topic.json", "r"))
global completed
completed = []

def getKeyArea():
    keyArea = list(question)[randint(0, 9)]
    if keyArea in completed:
        return getKeyArea()
    else:
        completed.append(keyArea)
        return keyArea


def startgame():
    Start_game = input ("Would you like to play the quiz? Enter T for tutorial ")
    if Start_game.lower() == "y":
        print ("Starting game")
        keyArea = getKeyArea()
        print (question[keyArea][0])
    elif Start_game.lower() =="t":
        print(f'''Welcome to Gamivia
A random topic will be chosen
You will have to guess that topic
Fortunately there are clues for these topics
Unfortunately each clue cost one 1 point
Clues range from 1 to 20
Enter the corresponding number to get the corresponding clue
When you are ready to guess, enter Y
But remember each guess costs 2 points
If you run out of points you fail the topic
You continue guessing until all topics run out then the final score will displayed
''')   
        startgame()
    else:
        print ("Then why did you open this program?")
        startgame()

startgame()