from random import randint

import art
import game_data as gd


def play():
    score = 0
    dict_a, index_a = get_entry()
    is_game_over = False
    while not is_game_over:
        dict_b, index_b = get_entry(exclude_one=True, excluded_index=index_a)

        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {dict_a['name']}, a {dict_a['description']} from {dict_a['country']}.")
        print(art.vs)
        print(f"Against B: {dict_b['name']}, a {dict_b['description']} from {dict_b['country']}.")

        print("\nWho has more followers? Type \"A\" or \"B\":")

        choice = get_input(["A", "B"])

        if dict_a["follower_count"] == dict_b["follower_count"]:
            score += 1
        elif dict_a["follower_count"] > dict_b["follower_count"]:
            if choice == "A":
                score += 1
            else:
                is_game_over = True
        elif dict_a["follower_count"] < dict_b["follower_count"]:
            if choice == "B":
                score += 1
            else:
                is_game_over = True

        if not is_game_over:
            dict_a = dict_b
            index_a = index_b
        print("\n" * 100)

    print(art.logo)
    print(f"Sorry that's wrong. Final score: {score}.\n")


def get_entry(exclude_one=False, excluded_index=0):
    """Returns a randomly picked entry and its index as a tuple of DICT and INT, other than the one matching
    the provided index."""
    entries = len(gd.data)
    chosen_index = randint(0, entries - 1)
    chosen_dict = gd.data[chosen_index]
    # make sure the chosen index and dict are not the same
    while exclude_one and chosen_index == excluded_index:
        chosen_index = randint(0, entries - 1)
        chosen_dict = gd.data[chosen_index]
    return chosen_dict, chosen_index


def get_input(choices_list):
    """Gets input from the user, returns it as STR. Only accepts choices from the provided list."""
    while True:
        user_choice = input("> ").upper()
        if user_choice not in choices_list:
            formatted_list = []
            for char in choices_list:
                formatted_list.append(f"\"{char}\"")
            print(f"Invalid choice. Please type {' or '.join(formatted_list)}.")
        else:
            return user_choice

while True:
    play()
    print("Do you want to play another round? Type \"Y\" or \"N\":")
    quit_choice = get_input(["Y", "N"])
    if quit_choice == "N":
        break
    else:
        print("\n" * 100)

print("Thanks for playing.")
