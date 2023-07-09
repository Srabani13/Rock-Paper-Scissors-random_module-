import random
option = ["Rock", "Paper", "Scissor" ]

# rock vs paper = paper Win
# rock vs scissor = rock win
# paper vs scissor = scissor win


while True:
    Ucount = 0
    Scount =0
    UC = int(input('''
Let's start the game.....
1. YES
2. EXIT                  

    '''))

    if UC ==1 :
        for a in range (1,6):
            userInput = int(input('''
1. Rock 
2. Paper
3. Scissor
'''))
            if userInput ==1:
                uchoice ="Rock"
            elif userInput ==2:
                 uchoice ="Paper"
            elif userInput ==3: 
                uchoice ="Scissor"
          
            systemChoice = random.choice(option)
           
            if systemChoice ==uchoice:
                print("Print System Choice: ",systemChoice )
                print("Print User Choice: ",uchoice )
                print("Game Draw")
                Ucount += 1
                Scount += 1
            elif(uchoice =="Rock" and systemChoice =="Scissor" ) or (uchoice =="Scissor" and systemChoice =="Paper") or (uchoice =="Paper" and systemChoice =="Rock"):
                print("YOU WIN !!")
                print("Print System Choice: ",systemChoice )
                print("Print User Choice: ",uchoice )
                Ucount += 1
            else :
                print("SYSTEM WIN !!")
                print("Print System Choice: ",systemChoice )
                print("Print User Choice: ",uchoice )
                Scount += 1
        if Ucount == Scount:
            print("System Score: ",Scount)
            print("User Score: ",Ucount)
            print("Final Game Draw......")
        elif Ucount > Scount: 
             print("System Score: ",Scount)
             print("User Score: ",Ucount)
             print("USER WIN.....")
        else:
             print("System Score: ",Scount)
             print("User Score: ",Ucount)
             print("SYSTEM WIN......")
    


    else :
        break