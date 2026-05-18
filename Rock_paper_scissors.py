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

game = [rock,paper,scissors]
user_choice = int(input("What do you wanna choose?Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if user_choice > 0 and user_choice <= 2:
    print(game[user_choice])
computer_choice = random.randint(0,2)
print("Computer Choose:")
print(game[computer_choice])
if user_choice == computer_choice:
    print("DRAW")
elif user_choice > computer_choice:
    print("You WIN")
elif user_choice < computer_choice:
    print("You LOSE")
elif user_choice == 0 and computer_choice == 2:
    print("You WIN")
elif user_choice == 2 and computer_choice == 0:
    print("You LOSE")
elif user_choice > 2:
    print("Invalid input try again")
