import random

Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"
choices = [Rock, Paper, Scissors]
playerwins = "The Player WINS!!!"
computerwins = "The Computer WINSS!!!"


choiceOption = random.choice(choices)
playerInput = input("Rock, Paper, or Scissors: ").lower()
computerInput = choiceOption.lower()

print(f"The Player choose: {playerInput}")
print(f"The Computer choose: {computerInput}")



def winSystem():
    if playerInput == choices[0] and computerInput == choiceOption[1]:
        print(computerwins)
    elif playerInput == choices[0] and computerInput == choiceOption[2]:
        print(playerwins)
    elif playerInput == choices[1] and computerInput == choiceOption[0]:
        print(playerwins)
    elif playerInput == choices[2] and computerInput == choiceOption[1]:
        print(playerwins)
    elif computerInput == choiceOption[1] and playerInput == choices[0]:
        print(computerwins)
    elif computerInput == choiceOption[2] and playerInput == choices[1]:
        print(computerwins)
    else:
        print("Tie")


winSystem()