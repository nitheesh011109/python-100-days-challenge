import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""

EASY_LIVES = 10
HARD_LIVES = 5

def check_answer(actual_number, user_guess, lives):
    if user_guess > actual_number:
        print("You guessed too high.")
        return lives - 1

    elif user_guess < actual_number:
        print("You guessed too low.")
        return lives - 1

    else:
        print(f"You got it! The answer was {actual_number}")
        return lives

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LIVES
    else:
        return HARD_LIVES

def game():
    print(logo)
    print("Welcome to Number Guessing Game")
    print("I am thinking of a number between 1 and 100")

    number = random.randint(1, 100)
    lives = set_difficulty()
    guess = 0

    while number != guess:

        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        lives = check_answer(number, guess, lives)
        
        if lives == 0:
            print("You ran out of guesses, YOU LOSE!")
            return
        elif guess != number:
            print("Guess again.")

game()