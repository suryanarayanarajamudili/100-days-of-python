import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('Welcome to the Childhood game "Rock, Paper Scissor" get some Nostalgia')
game_images=[rock, paper, scissors]
choices=["Rock", "Paper", "Scissors"]
user_choice=int(input("What do you Choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
computer_choice = random.randint(0, 2)
if user_choice >=0 and user_choice <=2:
    print("Your Choice is: " + choices[user_choice])
    print(game_images[user_choice])
    print("Play Buddy Choice is : " + choices[computer_choice])
    print(game_images[computer_choice])

if user_choice <0 or user_choice>=3:
    print("You Choose an invalid number, You Lose")
elif user_choice==0 and computer_choice==2:
    print("You Win!")
elif computer_choice == 0 and user_choice==2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print ("You Win!")
elif user_choice == computer_choice:
    print("Its a Draw")

print("You wanna play again click on Run Button")

