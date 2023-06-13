def startgame():
    Start_game = input ("would you like to play the quiz? Enter T for tutorial ")
    if Start_game.lower() == "y":
        print ("starting game")
    elif Start_game.lower() =="t":
        print (f'Welcome to Gamivia')
        startgame()
          #A random topic will be chosen
           #You will have to guess that topic
           #Fortunately there are clues for these topics
           #Unfortunately each clue cost one 1 point
           #Clues range from 1 to 20
           #Enter the corresponding number to get the corresponding clue
           #When you are ready to guess, enter Y
           #But remember each guess costs 2 points
           #If you run out of points you fail the topic
           #You continue guessing until all topics run out then the final score will displayed
        
    else:
        print ("Then why did you open this program?")
        startgame()
startgame()
