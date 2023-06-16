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
    global player_points,game_score,player_score,topic_area
    if len(question) == len(completed):
        print (f'''final score 
{player_score}''')
        play_Again = input("Would you like play again? ")
        if play_Again.lower() == "y":
            completed.clear()
            player_points = 0
            game_score = 0
            player_score = 0
            topic_area = getKeyArea()
            player_points = 20
            game_quiz()
        else:
            quit()
    else:
        keyArea = list(question)[randint(0, len(question)-1)]
        if keyArea in completed:
            return getKeyArea()
        else:
            completed.append(keyArea)
        return keyArea
#Allows the program to recognize if the clue has been chosen already
def getclueAnswer(first=False, Clue_choose=""):
    global player_points
    global topic_completed
    global game_score
    global topic_completed
    global player_score
    if first:
        clue = question[topic_area][randint(0,9)-1]
        clue_chosen.append(clue)
        return clue
    elif str(Clue_choose).lower() == 'y':
        guess()
    else:
        try:
            Clue_choose = int(Clue_choose)
            try:
                clue = question[topic_area][Clue_choose]
            except IndexError:
                print("Value out of range")
                clue = getclueAnswer(first, input("Insert Another Number or Y to take a guess "))
            if clue in clue_chosen:
                print("Clue already chosen")
                clue = getclueAnswer(first, input("Insert Another Number or Y to take a guess "))
            else:
                player_points = player_points-1 
                checkGameOver()
                print(clue)
                clue_chosen.append(clue)
        except ValueError:
            print("Invalid value!")
            clue = getclueAnswer(first, input("Insert Valid Value "))
        return clue
    
def checkGameOver():
    global player_points, topic_completed, game_score, clue_chosen, topic_area
    if  player_points <= 0:
                print (f"You have failed to guess, {topic_area}")
                topic_completed = True
                game_score = game_score + 1
                clue_chosen.clear()
                topic_area = getKeyArea()
                player_points = 20
                game_quiz()
# allows the program to assess answers
def guess():
    global player_points
    global game_score
    global topic_completed
    global player_score
    global topic_area
    Answer = input ("Type in answer: ")
    if Answer.lower() == topic_area.lower():
        print("Correct!")
        input("Hit enter to continue")
        topic_completed = True
        game_score = game_score + 1
        player_score = player_score + 1
        clue_chosen.clear()
        topic_area = getKeyArea()
        player_points = 20
        game_quiz()
        
    else:
        print ("Incorrect, two point deducted")
        player_points = player_points - 2
        checkGameOver()
        print (player_points)
        for clue in clue_chosen:
                print(f" - {clue}")
        clue = getclueAnswer(Clue_choose=input("Insert Another Number or Y to take a guess "))
            
        
#Main quiz area
def game_quiz():
    global player_points
    global game_score
    global player_score
    global topic_completed
    if game_score < 11:
        firstclued = False
        print (f"You currently have answered {player_score} area(s) correctly")
        global topic_area
        topic_completed = False
        while not topic_completed:
            if firstclued == False:
                first_clue = getclueAnswer(first=True)
                firstclued = True
            else:
                for clue in clue_chosen:
                    print(f" - {clue}")
                print (f'You have {player_points} point(s) left')
                Clue_choose = input("Would you like to guess with 'y' or get another clue? ")
                getclueAnswer(Clue_choose=Clue_choose)
#Gets called when the program starts. Sets early parameters 
def startgame():
    global player_points
    global game_score
    global player_score
    global topic_area
    Start_game = input ("Would you like to play the quiz? Press Y to Start, Enter T for tutorial ")
    if Start_game.lower() == "y":
        print ("Starting game")
        player_points = 0
        game_score = 0
        player_score = 0
        topic_area = getKeyArea()
        player_points = 20
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
print (f'''
          _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\                /::\____\                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::|   |               /:::/    /                \:::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /:::::|   |              /:::/    /                  \:::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/    /                    \:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/____/                      \:::\    \        /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |            |::|    |                       /::::\    \      /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______      |::|    |     _____    ____    /::::::\    \    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \     |::|    |    /\    \  /\   \  /:::/\:::\    \  /:::/\:::\   \:::\    \ 
/:::/____/  ___\:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\    |::|    |   /::\____\/::\   \/:::/  \:::\____\/:::/  \:::\   \:::\____\\
\:::\    \ /\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /    |::|    |  /:::/    /\:::\  /:::/    \::/    /\::/    \:::\  /:::/    /
 \:::\    /::\ \::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /     |::|    | /:::/    /  \:::\/:::/    / \/____/  \/____/ \:::\/:::/    / 
  \:::\   \:::\ \/____/            \::::::/    /               /:::/    /      |::|____|/:::/    /    \::::::/    /                    \::::::/    /  
   \:::\   \:::\____\               \::::/    /               /:::/    /       |:::::::::::/    /      \::::/____/                      \::::/    /   
    \:::\  /:::/    /               /:::/    /               /:::/    /        \::::::::::/____/        \:::\    \                      /:::/    /    
     \:::\/:::/    /               /:::/    /               /:::/    /          ~~~~~~~~~~               \:::\    \                    /:::/    /     
      \::::::/    /               /:::/    /               /:::/    /                                     \:::\    \                  /:::/    /      
       \::::/    /               /:::/    /               /:::/    /                                       \:::\____\                /:::/    /       
        \::/____/                \::/    /                \::/    /                                         \::/    /                \::/    /        
                                  \/____/                  \/____/                                           \/____/                  \/____/         
                                                                                                                                                      
''')
startgame()
