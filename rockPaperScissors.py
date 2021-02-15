#Porject: Rock Paper Scissor
#By: Mirzokhid Ganiev
#Age: 16
#Grade: 10 G
#Date upon finishing: Sunday, 14th February 2021 (14/02/2021)
#Location: Osh,  kyrgyzstan


#basic idea:
# you play a rock paper scissors game with a computer which radomly chooses the play

#imports

import math
import random
from random import randrange
import sys

#lets play rock paper scissors

scissor = ("|------------------------) \n|                        )\n|             |----------)\n|             |\n|             |----------)\n|    Scissor             )\n|             |----------)\n|               )\n|                )\n|               )\n-----------------\n")
rock = ("_|-----------------------)\n|                       --)\n|                       --)\n|                      --)\n|      Rock            --)\n|                       --)\n|                       --)\n|                      --)\n|                      --)\n~|------------------------)\n")
paper = ("|------------------------)\n|                        )\n|             |----------)\n|             |\n|             |----------)\n|    Paper               )\n|             |----------)\n|             |\n|             |----------)\n|                        )\n|             |----------)\n|             |\n|________     -----------)   \n         |               )\n         |---------------)\n")


ask = input("What do you want to do? a) Play b) Quite [a/b]")
ask.lower

def play():
    global scoreForHuman
    global scoreForComputer
    global scissorChance
    global rockChance
    global paperChance
    global humanMost

    choice = input("Choose your role: a) Rock b) Paper c) Scissor [A/B/C]")
    if choice == "a":
        print("Your choice is Rock: ")
        rockChance += 1
        print(rock)
    elif choice == "b":
        print("Your choice is Paper: ")
        paperChance += 1
        print(paper)
    elif choice == "c":
        print("Your choice is Scissor: ")
        scissorChance += 1
        print(scissor)
    else:
        print("That wasnt an option. Type again")
        play()

    role = [scissor, rock, paper]
    randomRole = random.choice(role)
    print("Computer choice is: \n" + randomRole)
    if rockChance >= paperChance and rockChance >= scissorChance:
        humanMost = "Rock"
    elif paperChance >= rockChance and paperChance >= scissorChance:
        humanMost = "Paper"
    elif scissorChance >= paperChance and scissorChance >= rockChance:
        humanMost = "Scissors"
    print("\n In the next round, the human is most likely to perform (It outputs whichever option which has been used by the human the most) : " + humanMost + "\n")

    if (choice == "a" and randomRole == rock) or (choice == "b" and randomRole == paper) or (choice == "c" and randomRole == scissor):
        print("\nIt was a draw\n")
        print("Number of lives left for Human: " + str(scoreForHuman) + "\n")
        print("Number of lives left for Computer: " + str(scoreForComputer) + "\n")
    elif choice == "a" and randomRole == scissor:
        print("\nThe winner is the human\n") # rock and scissor, winner human
        scoreForComputer -= 1
        print("Number of lives left for Human: " + str(scoreForHuman))
        print("Number of lives left for Computer: " + str(scoreForComputer))
    elif choice == "a" and randomRole == paper:
        print("\nThe winner is the Computer\n") #rock and paper, winner computer
        scoreForHuman -= 1
        print("Number of lives left for Human: " + str(scoreForHuman) + "\n")
        print("Number of lives left for Computer: " + str(scoreForComputer) + "\n")
    elif choice == "b" and randomRole == rock:
        print("\nThe winner is Human\n") #paper and rock, winner human
        scoreForComputer -= 1
        print("Number of lives left for Human: " + str(scoreForHuman) + "\n")
        print("Number of lives left for Computer: " + str(scoreForComputer) + "\n")
    elif choice == "b" and randomRole == scissor:
        print("\nThe winner is the Computer\n") #paper and scissor, winner computer
        scoreForHuman -= 1
        print("Number of lives left for Human: " + str(scoreForHuman) + "\n")
        print("Number of lives left for Computer: " + str(scoreForComputer) + "\n")
    elif choice == "c" and randomRole == rock:
        print("\nThe winner is the Computer\n") #scissor and rock, winner computer
        scoreForHuman -= 1
        print("Number of lives left for Human: " + str(scoreForHuman) + "\n")
        print("Number of lives left for Computer: " + str(scoreForComputer) + "\n")
    elif choice == "c" and randomRole == paper:
        print("\nThe winner is the human\n") #scissor and paper, winner human
        scoreForComputer -= 1
        print("Number of lives left for Human: " + str(scoreForHuman) + "\n")
        print("Number of lives left for Computer: " + str(scoreForComputer) + "\n")
    
    if scoreForComputer == 0:
        print("\nHuman Won")
        print("\nComputer Lost")
        sys.exit()
    elif scoreForHuman == 0:
        print("\nComputer Won")
        print("\nHuman Lost")
        sys.exit()

scoreForHuman = 3
scoreForComputer = 3
scissorChance = 0
rockChance = 0
paperChance = 0
humanMost = "test"

while True:
    if ask == "a":
        play()
    elif ask == "b":
        sys.exit()
    else: 
        print("Sorry that is not an option")
        sys.exit()
