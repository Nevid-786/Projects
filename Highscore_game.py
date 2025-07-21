#This programm is to generate a random high score and save it to a file which updates the previos with with latest high score.
import random
import os

def game():
    print("You are playing the game...")
    score =random.randint(1,1000)
    # fetch the previos score
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):#check if there is a previous hi score
            hiscore=int(hiscore)
        else:
            hiscore=0  #if no then take it as 0
    print(f"your score: {score}")
    #update if the latest score is greater as hiscore
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
                f.write(str( score))
    play=(input("To play again press enter,To clear press any otherkey then enter: "))
    
    if(play==""):
        game()
    else:
        with open("hiscore.txt","w") as f:
            f.write("")  
# Check if the file exists
if os.path.exists("hiscore.txt"):
    print(f"The file  already exists. No changes made.")
else:

    #creates a file name hiscore
    with open("hiscore.txt", "w") as file:
        file.write("0")
    print(f"The file has been created.")    
print("Press any key to get a random score:")
start=input()
print('hello')
game()
    