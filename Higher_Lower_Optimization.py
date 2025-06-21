import art
from game_data import data
import random
def play():
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        if account_a == account_b:
            account_b = random.choice(data)
        if account_a != account_b:
            break
    score = 0
    while True:
        account_name = account_a["name"]
        account_description = account_a["description"]
        account_country = account_a["country"]
        A = account_a["follower_count"]
        print(art.logo)
        print(f"Your Score is: {score}")
        print(f"Compare A={account_name} a {account_description} from {account_country}")
        account_name = account_b["name"]
        account_description = account_b["description"]
        account_country = account_b["country"]
        B = account_b["follower_count"]
        print(art.vs)
        print(f"Against B={account_name} a {account_description} from {account_country}")
        print("Who has more followers type \"A\" or \"B\"")
        winner = input(">")
        while winner.upper() not in ["A", "B"]:
            print("Please enter either \"A\" or \"B\" only")
            winner = input(">")
        if winner.upper() == "A":
            if A >= B:
                score += 1
            else:
                print("Oh! Looks like you lost")
                print(f"Your final score is: {score}")
                print("Thanks for playing!")
                break
        if winner.upper() == "B":
            if B >= A:
                score += 1
            else:
                print("Oh! Looks like you lost")
                print(f"Your final score is: {score}")
                print("Thanks for playing!")
                break
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
def play_again():
    play_again=input("Do you want to play again? Type \"Y\" or \"N\":")
    while play_again.upper() not in ["Y","N"]:
        play_again=input("Please enter either \"Y\" or \"N\" only:")
    if play_again.upper()=="Y":
        print("\n"*100)
        play()
play()
play_again()
