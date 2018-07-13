########### Code for Rock Paper Scissors ############

import random

gestures = ["scissors", "rock", "paper"]

computer = random.choice(gestures)

human = input("Rock, paper, scissors, SHOOT: ")
human = human.lower().lstrip().rstrip()
print("Computer chooses {}".format(computer.upper()))
if computer == human:
    print("TIE")
elif (computer == "scissors" and human == "paper") or (computer == "paper" and human == "rock") or (computer == "rock" and human == "scissors"):
    print("You lost. Go computers. ")
else:
    print("You win! Down with computers. ")
