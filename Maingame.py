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
def getclueAnswer(first=False, Clue_choose=""):
    global player_points
    if first:
        clue = question[topic_area][randint(0,len(topic_area)-1)]
        clue_chosen.append(clue)
    elif str(Clue_choose).lower() == 'y':
        guess()
    else:
        try:
            Clue_choose = int(Clue_choose)
            try:
                clue = question[topic_area][Clue_choose]
            except IndexError:
                print("Value out of range")
                return getclueAnswer(first, input("Insert Another Number or Y to take a guess "))
            if clue in clue_chosen:
                print("Clue already chosen")
                return getclueAnswer(first, input("Insert Another Number or Y to take a guess "))
            else:
                print(clue)
                clue_chosen.append(clue)
                player_points = player_points-1 
        except ValueError:
            print("Invalid value!")
            return getclueAnswer(first, input("Insert Valid Value "))
    return clue

def guess():
    print("well you can't guess cause james is lazy and didn't code in a guess")
    
#Main quiz
def game_quiz():
    global player_points
    global game_score
    global player_score
    if game_score < 11:
        firstclued = False
        print (f"You currently have {player_score} points")
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
                first_clue = getclueAnswer(first=True)
                firstclued = True
            else:
                for clue in clue_chosen:
                    print(f" - {clue}")
                print (f'You have {player_points} left')
                Clue_choose = input("Would you like to guess with 'y' or get another clue? ")
                getclueAnswer(Clue_choose=Clue_choose)
#Gets called when the program starts
def startgame():
    global player_points
    global game_score
    global player_score
    Start_game = input ("Would you like to play the quiz? Enter T for tutorial ")
    if Start_game.lower() == "y":
        print ("Starting game")
        player_points = 0
        game_score = 0
        player_score = 0
        game_quiz()
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