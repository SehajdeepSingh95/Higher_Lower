import art
from game_data import data
import random
import os

highest_score=0

def get_random_account():
    return random.choice(data)

def format_account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    return (a_followers > b_followers and guess == "A") or (b_followers > a_followers and guess == "B")

def play():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()

    while game_should_continue:
        os.system("cls" if os.name == "nt" else "clear")
        print(art.logo)
        print(f"Your current score: {score}")
        print(f"Compare A: {format_account(account_a)}")
        print(art.vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        while guess not in ["A", "B"]:
            guess = input("Please enter either 'A' or 'B': ").upper()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        if check_answer(guess, a_follower_count, b_follower_count):
            score += 1
            account_a = account_b
            account_b = get_random_account()
            while account_a == account_b:
                account_b = get_random_account()
        else:
            print(f"Wrong answer. Final score: {score}")
            game_should_continue = False

def play_again():
    again = input("Play again? (Y/N): ").upper()
    while again not in ["Y", "N"]:
        again = input("Please enter 'Y' or 'N': ").upper()
    if again == "Y":
        print("\n" * 100)
        play()
        play_again()

play()
play_again()