from random import randint

print("Hello! Welcome to my game of Rock, Paper, Scissors!")
print("For this game, input your answers in CAPITAL LETTERS!")
print("Stone beats bird, bird beats water, and water beats stone.")
playerInput = str(input("Please enter STONE, WATER, or BIRD "))

if (playerInput != "STONE" and playerInput != "WATER" and playerInput != "BIRD"):
    print("OOPS! YOU MADE IN INVALID SELECTION")
else:

    print("Great! You chose: " + playerInput)

    print("Now I will make my selection")
    chosen = randint(1,3)
    if chosen == 1:
        compInput = "STONE"
    elif chosen == 2:
        compInput = "WATER"
    else:
        compInput = "BIRD"

    print(compInput)
    print("Alright, I have made my selection")
    print("The matchup is: " + playerInput + " vs. " + compInput)

    if playerInput == compInput:
        print("It's a draw!")
    elif (playerInput == "STONE" and compInput == "BIRD"):
        print("You WIN!")
    elif (playerInput == "STONE" and compInput == "WATER"):
        print("You LOSE!")
    elif (playerInput == "WATER" and compInput == "STONE"):
        print("You WIN!")
    elif (playerInput == "WATER" and compInput == "BIRD"):
        print("You LOSE!")
    elif (playerInput == "BIRD" and compInput == "ROCK"):
        print("You LOSE!")
    elif (playerInput == "BIRD" and compInput == "WATER"):
        print("You WIN!")

    print("THANKS FOR PLAYING!")

