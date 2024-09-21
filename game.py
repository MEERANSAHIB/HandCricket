import random
def isvalidinput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 6:
                return value
            else:
                print("Invalid input! Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid number between 0 and 6.")
def start():
    score = 0
    score1 = 0
    bat = bowl = 0 
    print("Welcome TO Hand Cricket Game ")
    print("Odd Or Even")
    choice=int(input("Enter 0 if your choice is even and enter 1 if your choice is odd"))
    cchoice=random.randint(0,1)
    cres=(choice+cchoice)%2
    if choice==cres:
        print("you won the toss select 'batting or bowling'")
        bchoice=int(input("Enter 0 if you want to select batting/Enter 1 if you want to select bowling"))
        if bchoice==1:
            bowl=1
        else:
            bat=1
    else:
        print("you lost the toss")
        cbchoice=random.randint(0,1)
        if cbchoice==0:
            print("the computer selected to bat first")
            bowl=1
        else:
            print("the computer selected to bowl first")
            bat=1
    #batting first
    if bat==1:
        print("start batting")
        ba=0
        bo=1
        while ba!=bo:
            ba=isvalidinput("Enter number from  1 to 6:   ")
            bo=random.randint(0,6)
            print(f"c{bo}")
            if ba!=bo:
             score=score+ba
        print(f"you're out your score is {score}")
        print("Start bowling")
        ba=0
        bo=1
        while ba!=bo and score1<=score:
            bo=isvalidinput("Enter number from  1 to 6:   ")
            ba=random.randint(0,6)
            print(f"c{ba}")
            if ba!=bo:
             score1=score1+ba
        if(score>score1):
            print("OMG YOU WON")
        else:
            print("YOU LOSE")
    #bowling first
    else:
        print("Start Bowling")
        ba=0
        bo=1
        while ba!=bo:
            bo=isvalidinput("Enter number from  1 to 6:  ")
            ba=random.randint(0,6)
            print(f"c{ba}")
            if ba!=bo:
             score1=score1+ba
        print(f"Score {score1} to win")
        
        print("start batting")
        ba=0
        bo=1
        while ba!=bo and score1>=score:
            ba=isvalidinput("Enter number from  1 to 6:  ")
            bo=random.randint(0,6)
            print(f"c{bo}")
            if ba!=bo:
             score=score+ba
        if(score>score1):
            print("OMG YOU WON")
        else:
            print("YOU LOSE")
       
start()
    
