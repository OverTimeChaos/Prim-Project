import json
from random import randint
global question
#load json
question = json.load(open("topic.json", "r"))
global completed
completed = []
global clue_chosen
clue_chosen = []

#Allows the program to uniquely choose a Area
def getKeyArea():
    keyArea = list(question)[randint(0, 9)]
    if keyArea in completed:
        return getKeyArea()
    else:
        completed.append(keyArea)
        return keyArea
#Allows the program to recognize if the clue has been chosen already
def getclueAnswer(first, Clue_choose):
    if first:
        clue = topic_area[randint(0,19)]
        clue_chosen.append(clue)
        print (clue)
    elif Clue_choose.lower() == 'y':
    
    else:
    
    return clue

    
#Main quiz
def game_quiz(game_score,player_points,player_score):
    if game_score < 11:
        firstclued = False
        print (f"You currently have {player_score}")
        global topic_area
        topic_area = getKeyArea()
        player_points = 20
        topic_completed = False
    while topic_completed == False:
        if player_points == 0:
            print (f"You have failed to guess, {topic_area}")
            topic_completed == True
           
        else:
            if firstclued == False:
                first_clue = getclueAnswer(True)
                firstclued = True
            else: 
                print (f''' {clue_chosen}
                       You have {player_points} left''')
                Clue_choose = input("Would you like to guess with 'y' or get another clue? ")
                getclueAnswer(Clue_choose)
#Gets called when the program starts
def startgame():

    Start_game = input ("Would you like to play the quiz? Enter T for tutorial ")
    if Start_game.lower() == "y":
        print ("Starting game")
        player_points = 0
        game_score = 0
        player_score = 0
        game_quiz(game_score,player_points,player_score)
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
print("o")