from random import randint

g = ["Rock", "Paper", "Scissors"]

computer = g[randint(0,2)]
player = False

while player == False:
    player = input("""Rock, Paper, Scissors? 
    Want to exit? Type E and enter: """)
    if player == "Paper" or player == "P" or player == "p" or player == "paper":
        player = "Paper"
    elif player == "Rock" or player == "R" or player == "r" or player == "rock":
            player = "Rock"
    elif player == "Scissors" or player == "S" or player == "s" or player == "scissors" or player == "scissor" or player == "Scissor":
            player = "Scissors"
    print("You picked: ", player)
    if player == "E":
        exit()
    print("Computer picked: ", computer)


    if player == computer:
        print("Tie")
    elif player == "Paper":
        if computer == "Rock":
            print("Win! ", player, " beats ", computer)
        else:
            print("Lose! ", computer, " beats ", player)
    elif player == "Rock":
        if computer == "Scissors":
            print("Win! ", player, " beats ", computer)
        else:
            print("Lose! ", computer, " beats ", player)
    elif player == "Scissors":
        if computer == "Paper":
            print("Win!", player, " beats ", computer)
        else:
            print("Lose!", computer, " beats ", player)
    else:
        print("Check your spelling")
    print("")



    player = False
    computer = g[randint(0,1)]