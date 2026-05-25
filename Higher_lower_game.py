import os
import random
from HL_game_data import data
from HL_art import vs,logo

def format_name(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name},a {account_description} from {account_country}"

def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_name(account_a)}")
    print(vs)
    print(f"Aganist B: {format_name(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    os.system('cls')
    print(logo)
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_answer(guess, a_followers, b_followers)
    
    if is_correct:
        score += 1
        print(f"You're right! Your current score is {score}")
    else:
        print(f"Sorry, that's wrong. Your Final score was {score}")
        game_should_continue = False