import random

rock =  '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper =     '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

sciissors =      '''     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listOfShapes = [rock, paper, sciissors]

start = print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

playerChoice  = int(input())
if playerChoice >= 0 and playerChoice <=2:
    print(listOfShapes[playerChoice])
computerChoice = random.randint(0,2)
print("Computer Choose")
print(listOfShapes[computerChoice])

if playerChoice >= 3  or playerChoice < 0:
    print("You typed an invalid number")
elif playerChoice == 0  and computerChoice == 2:
    print("You win!")
elif computerChoice == 0 and playerChoice == 2 :
    print("You lose")
elif computerChoice  > playerChoice:
    print("Computer won!")
elif playerChoice  > computerChoice:
    print("you won!!")
elif computerChoice == playerChoice:
    print("It's a draw")







