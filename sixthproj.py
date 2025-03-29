import random
options = ["Scissor", "Rock", "Paper"]
def game(userchoice, playdefault):
    while playdefault == "Yes":
        compchoice = random.choice(options)
        if userchoice == compchoice:
            print("Hey! It was a tie")
        elif userchoice == "Rock":
            if compchoice == "Scissor":
                print("You won! I picked " + compchoice)
            elif compchoice == "Paper":
                print("You lost! I picked " + compchoice)
        elif userchoice == "Scissor":
            if compchoice == "Paper":
                print("You won! I picked " + compchoice)
            elif compchoice == "Rock":
                print("You lost! I picked " + compchoice)            
        elif userchoice == "Paper":
            if compchoice == "Rock":
                print("You won! I picked " + compchoice)
            elif compchoice == "Scissor":
                print("You lost! I picked " + compchoice)
        playdefault = input("Do you want to play again? Type Yes if so! \n")
        userchoice = input("What's ur pick: Rock, Paper, or Scissor? \n")
play = input("Do wou want to play the game? \n")
choice = input("What's ur pick: Rock, Paper, or Scissor? \n")
print(game(choice, play))


