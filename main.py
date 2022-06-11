import random

while True:

    R = 'rock'
    P = 'paper'
    S = 'scissors'

    listOfOptions = [R, P, S]

    playerChoice = input("Pick an option (rock, paper, scissors): \n")

    CPUChoice = random.choice(listOfOptions)

    print(f"\nPlayer({playerChoice}):CPU({CPUChoice})")

    if playerChoice == CPUChoice:
        print(f"It's a tie! Both players selected {playerChoice}")
    elif playerChoice == R:
        if CPUChoice == S:
            print("You won this round! Rock smashes scissors!")
        else:
            print("Oops you lost! Paper covers rock!")
    elif playerChoice == P:
        if CPUChoice == R:
            print("You won this round! Paper covers rock!")
        else:
            print("Oops you lost! Scissors cuts paper!")
    elif playerChoice == P:
        if CPUChoice == R:
            print("You won this round! Paper covers rock!")
        else:
            print("Oops you lost! Scissors cuts paper!")
    elif playerChoice == S:
        if CPUChoice == P:
            print("You won this round! Scissors cuts paper!")
        else:
            print("Oops you lost! Rock smashes scissors!")
    else:
        print("Invalid choice")        
     
     
    playAnotherGame = input("Play again? (yes/no): ")
    if (playAnotherGame != "yes"):
        break        
    


