"""
Created on 09:27:15
Author: Reji Jacob

"""

import random
import time

print("""

      Rock - Paper - Scissors Game
      
      Please choose one of them:

      1. Rock
      2. Paper
      3. Scissors
      4. Exit Game

    Rules:

    1. Rock beats Scissors
    2. Scissors beats paper
    3. Paper beats Rock

    Let's Start !!

"""
)

while True:

    User_1 = int(input("Your choice: "))

    if User_1 == 4:
        print("Game Over!")
        break

    elif User_1 >= 5:
        print("Please Enter valid number choices from 1 to 4!")

    else:

        Game = {1:"Rock", 2:"Paper", 3:"Scissors"}
        AI_1 = random.randint(1,3)
        
        AI = Game.get(AI_1)
        User = Game.get(User_1)

        if User == "Rock" and AI == "Scissors":
            time.sleep(0.1)
            print("I chose Scissors, You win!")

        elif User == "Rock" and AI == "Paper":
            time.sleep(0.1)
            print("I chose Paper, You Lose!")

        elif User == "Paper" and AI == "Scissors":
            time.sleep(0.1)
            print("I chose Scissors, You Lose!")

        elif User == "Paper" and AI == "Rock":
            time.sleep(0.1)
            print("I chose Rock, You Won!")

        elif User == "Scissors" and AI == "Rock":
            time.sleep(0.1)
            print("I chose Rock, You Lose!")

        elif User == "Scissors" and AI == "Paper":
            time.sleep(0.1)
            print("I chose Paper, You Win!")

        else:
            print("It's a Draw! Please Continue..")

            
