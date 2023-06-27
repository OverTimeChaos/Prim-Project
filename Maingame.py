import json
import tastetherainbow
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
        print (f'''{tastetherainbow.fg.green}final score:
{player_score}{tastetherainbow.reset}''')
        play_Again = input(tastetherainbow.fg.cyan+"Would you like play again? "+tastetherainbow.reset)
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
        clue = question[topic_area][randint(0,19)]
        clue_chosen.append(clue)
        return clue
    elif str(Clue_choose).lower() == 'y':
        guess()
    else:
        try:
            Clue_choose = int(Clue_choose)
            try:
                clue = question[topic_area][Clue_choose-1]
            except IndexError:
                print(tastetherainbow.fg.red+"Value out of range"+tastetherainbow.reset)
                return getclueAnswer(first, input(tastetherainbow.fg.magenta+"Insert Value in range "+tastetherainbow.reset))
            if clue in clue_chosen:
                print(tastetherainbow.fg.red+"Clue already chosen"+tastetherainbow.reset)
                return getclueAnswer(first, input(tastetherainbow.fg.magenta+"Insert Another Number or Y to take a guess "+tastetherainbow.reset))
            else:
                player_points = player_points-1 
                checkGameOver()
                clue_chosen.append(clue)
        except ValueError:
            print(tastetherainbow.fg.red+"Invalid value!"+tastetherainbow.reset)
            return getclueAnswer(first, input(tastetherainbow.fg.magenta+"Insert Valid Value "+tastetherainbow.reset))
        return clue
# check if player has run out of
def checkGameOver():
    global player_points, topic_completed, game_score, clue_chosen, topic_area
    if  player_points <= 0:
        print (f"{tastetherainbow.fg.magenta}You have failed to guess, {topic_area}{tastetherainbow.reset}")
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
    Answer = input (tastetherainbow.fg.yellow +"Type in answer: "+tastetherainbow.reset)
    if Answer.lower() == topic_area.lower():
        print(tastetherainbow.fg.green+"Correct!"+tastetherainbow.reset)
        input(tastetherainbow.fg.green+"Hit enter to continue "+tastetherainbow.reset)
        topic_completed = True
        game_score = game_score + 1
        player_score = player_score + 1
        clue_chosen.clear()
        topic_area = getKeyArea()
        player_points = 20
        game_quiz()
        
    else:
        print (tastetherainbow.fg.red+"Incorrect, two point deducted"+tastetherainbow.reset)
        player_points = player_points - 2
        checkGameOver()
        print (f'{tastetherainbow.fg.cyan}You have {player_points} point(s) left{tastetherainbow.reset}')
        for clue in clue_chosen:
                print(f"{tastetherainbow.fg.magenta} - {clue}{tastetherainbow.reset}")
        clue = getclueAnswer(Clue_choose=input(tastetherainbow.fg.red+"Insert Another Number or Y to take a guess "+tastetherainbow.reset))      
#Main quiz area
def game_quiz():
    global player_points
    global game_score
    global player_score
    global topic_completed
    if game_score < 11:
        firstclued = False
        print (f"{tastetherainbow.fg.blue}You currently have answered {player_score} area(s) correctly{tastetherainbow.reset}")
        global topic_area
        topic_completed = False
        while not topic_completed:
            if firstclued == False:
                first_clue = getclueAnswer(first=True)
                firstclued = True
            else:
                for clue in clue_chosen:
                    print(f"{tastetherainbow.fg.magenta} - {clue}{tastetherainbow.reset}")
                print (f'{tastetherainbow.fg.cyan}You have {player_points} point(s) left{tastetherainbow.reset}')
                Clue_choose = input(tastetherainbow.fg.yellow+"Would you like to guess with 'y' or enter a number to get another clue? "+tastetherainbow.reset)
                getclueAnswer(Clue_choose=Clue_choose)
#Gets called when the program starts. Sets early parameters 
def startgame():
    global player_points
    global game_score
    global player_score
    global topic_area
    Start_game = input (tastetherainbow.fg.yellow+"Would you like to play the quiz? Press Y to Start, Enter T for tutorial "+tastetherainbow.reset)
    if Start_game.lower() == "y":
        print (tastetherainbow.fg.blue+"Starting game"+tastetherainbow.reset)
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
        print (tastetherainbow.fg.red+"Then why did you open this program?"+tastetherainbow.reset)
        startgame()
print (f'''
          {tastetherainbow.fg.red}_____{tastetherainbow.reset}                    {tastetherainbow.fg.green}_____{tastetherainbow.reset}                     {tastetherainbow.fg.yellow}_____{tastetherainbow.reset}                    {tastetherainbow.fg.blue}_____{tastetherainbow.reset}                    {tastetherainbow.fg.magenta}_____{tastetherainbow.reset}                    {tastetherainbow.fg.cyan}_____{tastetherainbow.reset}          
         {tastetherainbow.fg.red}/\    \{tastetherainbow.reset}                  {tastetherainbow.fg.green}/\    \{tastetherainbow.reset}                   {tastetherainbow.fg.yellow}/\    \{tastetherainbow.reset}                  {tastetherainbow.fg.blue}/\    \{tastetherainbow.reset}                  {tastetherainbow.fg.magenta}/\    \{tastetherainbow.reset}                  {tastetherainbow.fg.cyan}/\    \{tastetherainbow.reset}         
        {tastetherainbow.fg.red}/::\    \{tastetherainbow.reset}                {tastetherainbow.fg.green}/::\    \{tastetherainbow.reset}                 {tastetherainbow.fg.yellow}/::\____\{tastetherainbow.reset}                {tastetherainbow.fg.blue}/::\____\{tastetherainbow.reset}                {tastetherainbow.fg.magenta}/::\    \{tastetherainbow.reset}                {tastetherainbow.fg.cyan}/::\    \{tastetherainbow.reset}        
       {tastetherainbow.fg.red}/::::\    \{tastetherainbow.reset}              {tastetherainbow.fg.green}/::::\    \{tastetherainbow.reset}               {tastetherainbow.fg.yellow}/::::|   |{tastetherainbow.reset}               {tastetherainbow.fg.blue}/:::/    /{tastetherainbow.reset}                {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}              {tastetherainbow.fg.cyan}/::::\    \{tastetherainbow.reset}       
      {tastetherainbow.fg.red}/::::::\    \{tastetherainbow.reset}            {tastetherainbow.fg.green}/::::::\    \{tastetherainbow.reset}             {tastetherainbow.fg.yellow}/:::::|   |{tastetherainbow.reset}              {tastetherainbow.fg.blue}/:::/    /{tastetherainbow.reset}                  {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}            {tastetherainbow.fg.cyan}/::::::\    \{tastetherainbow.reset}      
     {tastetherainbow.fg.red}/:::/\:::\    \{tastetherainbow.reset}          {tastetherainbow.fg.green}/:::/\:::\    \{tastetherainbow.reset}           {tastetherainbow.fg.yellow}/::::::|   |{tastetherainbow.reset}             {tastetherainbow.fg.blue}/:::/    /{tastetherainbow.reset}                    {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}          {tastetherainbow.fg.cyan}/:::/\:::\    \{tastetherainbow.reset}     
    {tastetherainbow.fg.red}/:::/  \:::\    \{tastetherainbow.reset}        {tastetherainbow.fg.green}/:::/__\:::\    \{tastetherainbow.reset}         {tastetherainbow.fg.yellow}/:::/|::|   |{tastetherainbow.reset}            {tastetherainbow.fg.blue}/:::/____/{tastetherainbow.reset}                      {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}        {tastetherainbow.fg.cyan}/:::/__\:::\    \{tastetherainbow.reset}    
   {tastetherainbow.fg.red}/:::/    \:::\    \{tastetherainbow.reset}      {tastetherainbow.fg.green}/::::\   \:::\    \{tastetherainbow.reset}       {tastetherainbow.fg.yellow}/:::/ |::|   |{tastetherainbow.reset}            {tastetherainbow.fg.blue}|::|    |{tastetherainbow.reset}                       {tastetherainbow.fg.magenta}/::::\    \{tastetherainbow.reset}      {tastetherainbow.fg.cyan}/::::\   \:::\    \{tastetherainbow.reset}   
  {tastetherainbow.fg.red}/:::/    / \:::\    \{tastetherainbow.reset}    {tastetherainbow.fg.green}/::::::\   \:::\    \{tastetherainbow.reset}     {tastetherainbow.fg.yellow}/:::/  |::|___|______{tastetherainbow.reset}      {tastetherainbow.fg.blue}|::|    |     _____{tastetherainbow.reset}    {tastetherainbow.fg.magenta}____    /::::::\    \{tastetherainbow.reset}    {tastetherainbow.fg.cyan}/::::::\   \:::\    \{tastetherainbow.reset}  
 {tastetherainbow.fg.red}/:::/    /   \:::\ ___\{tastetherainbow.reset}  {tastetherainbow.fg.green}/:::/\:::\   \:::\    \{tastetherainbow.reset}   {tastetherainbow.fg.yellow}/:::/   |::::::::\    \{tastetherainbow.reset}     {tastetherainbow.fg.blue}|::|    |    /\    \{tastetherainbow.reset}  {tastetherainbow.fg.magenta}/\   \  /:::/\:::\    \{tastetherainbow.reset}  {tastetherainbow.fg.cyan}/:::/\:::\   \:::\    \{tastetherainbow.reset} 
{tastetherainbow.fg.red}/:::/____/  ___\:::|    |{tastetherainbow.reset}{tastetherainbow.fg.green}/:::/  \:::\   \:::\____\{tastetherainbow.reset} {tastetherainbow.fg.yellow}/:::/    |:::::::::\____\{tastetherainbow.reset}    {tastetherainbow.fg.blue}|::|    |   /::\____\{tastetherainbow.reset}{tastetherainbow.fg.magenta}/::\   \/:::/  \:::\____\{tastetherainbow.reset}{tastetherainbow.fg.cyan}/:::/  \:::\   \:::\____\\{tastetherainbow.reset}
{tastetherainbow.fg.red}\:::\    \ /\  /:::|____|{tastetherainbow.reset}{tastetherainbow.fg.green}\::/    \:::\  /:::/    /{tastetherainbow.reset} {tastetherainbow.fg.yellow}\::/    / ~~~~~/:::/    /{tastetherainbow.reset}    {tastetherainbow.fg.blue}|::|    |  /:::/    /{tastetherainbow.reset}{tastetherainbow.fg.magenta}\:::\  /:::/    \::/    /{tastetherainbow.reset}{tastetherainbow.fg.cyan}\::/    \:::\  /:::/    /{tastetherainbow.reset}
 {tastetherainbow.fg.red}\:::\    /::\ \::/    /{tastetherainbow.reset}  {tastetherainbow.fg.green}\/____/ \:::\/:::/    /{tastetherainbow.reset}   {tastetherainbow.fg.yellow}\/____/      /:::/    /{tastetherainbow.reset}     {tastetherainbow.fg.blue}|::|    | /:::/    /{tastetherainbow.reset}  {tastetherainbow.fg.magenta}\:::\/:::/    / \/____/{tastetherainbow.reset}  {tastetherainbow.fg.cyan}\/____/ \:::\/:::/    /{tastetherainbow.reset} 
  {tastetherainbow.fg.red}\:::\   \:::\ \/____/{tastetherainbow.reset}            {tastetherainbow.fg.green}\::::::/    /{tastetherainbow.reset}                {tastetherainbow.fg.yellow}/:::/    /{tastetherainbow.reset}      {tastetherainbow.fg.blue}|::|____|/:::/    /{tastetherainbow.reset}    {tastetherainbow.fg.magenta}\::::::/    /{tastetherainbow.reset}                    {tastetherainbow.fg.cyan}\::::::/    /{tastetherainbow.reset}  
   {tastetherainbow.fg.red}\:::\   \:::\____\{tastetherainbow.reset}               {tastetherainbow.fg.green}\::::/    /{tastetherainbow.reset}                {tastetherainbow.fg.yellow}/:::/    /{tastetherainbow.reset}       {tastetherainbow.fg.blue}|:::::::::::/    /{tastetherainbow.reset}      {tastetherainbow.fg.magenta}\::::/____/{tastetherainbow.reset}                      {tastetherainbow.fg.cyan}\::::/    /{tastetherainbow.reset}   
    {tastetherainbow.fg.red}\:::\  /:::/    /{tastetherainbow.reset}               {tastetherainbow.fg.green}/:::/    /{tastetherainbow.reset}                {tastetherainbow.fg.yellow}/:::/    /{tastetherainbow.reset}        {tastetherainbow.fg.blue}\::::::::::/____/{tastetherainbow.reset}        {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}                      {tastetherainbow.fg.cyan}/:::/    /{tastetherainbow.reset}    
     {tastetherainbow.fg.red}\:::\/:::/    /{tastetherainbow.reset}               {tastetherainbow.fg.green}/:::/    /{tastetherainbow.reset}                {tastetherainbow.fg.yellow}/:::/    /{tastetherainbow.reset}          {tastetherainbow.fg.blue}~~~~~~~~~~{tastetherainbow.reset}               {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}                    {tastetherainbow.fg.cyan}/:::/    /{tastetherainbow.reset}     
      {tastetherainbow.fg.red}\::::::/    /{tastetherainbow.reset}               {tastetherainbow.fg.green}/:::/    /{tastetherainbow.reset}                {tastetherainbow.fg.yellow}/:::/    /{tastetherainbow.reset}                                     {tastetherainbow.fg.magenta}\:::\    \{tastetherainbow.reset}                  {tastetherainbow.fg.cyan}/:::/    /{tastetherainbow.reset}      
       {tastetherainbow.fg.red}\::::/    /{tastetherainbow.reset}               {tastetherainbow.fg.green}/:::/    /{tastetherainbow.reset}                {tastetherainbow.fg.yellow}/:::/    /{tastetherainbow.reset}                                       {tastetherainbow.fg.magenta}\:::\____\{tastetherainbow.reset}                {tastetherainbow.fg.cyan}/:::/    /{tastetherainbow.reset}       
        {tastetherainbow.fg.red}\::/____/{tastetherainbow.reset}                {tastetherainbow.fg.green}\::/    /{tastetherainbow.reset}                 {tastetherainbow.fg.yellow}\::/    /{tastetherainbow.reset}                                         {tastetherainbow.fg.magenta}\::/    /{tastetherainbow.reset}                {tastetherainbow.fg.cyan}\::/    /{tastetherainbow.reset}        
                                  {tastetherainbow.fg.green}\/____/{tastetherainbow.reset}                   {tastetherainbow.fg.yellow}\/____/{tastetherainbow.reset}                                           {tastetherainbow.fg.magenta}\/____/{tastetherainbow.reset}                  {tastetherainbow.fg.cyan}\/____/{tastetherainbow.reset}         
                                                                                                                                                      
''')

startgame()
