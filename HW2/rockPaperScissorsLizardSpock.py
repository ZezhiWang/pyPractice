import random;  

CompeteResult = {"Rock":["Rock","Scissors","Lizard","Paper","Spock"],"Scissors":["Scissors","Spock","Paper","Rock","Lizard"],"Paper":["Paper","Spock","Rock","Lizard","Scissors"],"Lizard":["Lizardr","Spock","Paper","Rock","Scissors"],"Spock":["Spock","Scissors","Rock","Lizard","Paper"]} 
Sign = {1:"Rock", 2:"Scissors", 3:"Paper",4:"Lizard", 5:"Spock" } 
Result = {0:"Tied", 1:"WIN", 2:"WIN", 3:"LOST", 4:"LOST"}  
  
def game():  
    print "1:Rock, 2:Scissors, 3:Paper, 4:Lizard, 5:Spock, 0:quit"
    while True:  
        userSign = input("Your Choice:") 
        if userSign in [1, 2, 3, 4, 5, 0]:  
            if userSign == 0:  
                break  
            else:
                user = Sign[userSign]
                userResult = CompeteResult[user]
                pc = Sign[pcSign()]
                print " User:" + user + "\n PC:" + pc + "\n Result: U " + Result[userResult.index(pc)]
        else:  
            print "Try again"  

def pcSign():  
    return random.randint(1,5) 
  
game()  
