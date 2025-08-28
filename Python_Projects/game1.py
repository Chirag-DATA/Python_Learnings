# It is a rock, paper, scissor game

import random
while True:
    play = input("Do you want to play more (Y/N): ")
    if play == "Y":
        lst = ["Rock", "Paper", "Scissor"]
        user = input("Enter your move from Rock/Paper/Scissor: ")
        computer = random.choice(lst)

        print(f'Your move : {user}. Computer move : {computer}')
        
        if user == computer:
            print("It's a tie...")

        elif user == "Rock":
            if computer == "Paper":
                print("Paper covers Rock! Computer wins this game...")
            else:
                print("Rock breaks Scissor! You wins the game...")

        elif user == "Paper":
            if computer == "Rock":
                print("Paper covers the rock! You wins the game...")
            else:
                print("Scissor cuts the paper! Computer wins the game...")
        elif user == "Scissor":
            if computer == "Rock":
                print("Rock breaks the Scissor!Computer wins the game...")
            else:
                print("Scissor cuts the paper! You wins the game...")
    elif play == "N":
        break


