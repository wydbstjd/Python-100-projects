from art import logo6, vs # art.py
from game_data import data # game_data.py
from replit import clear
import random
def random_person():
    return random.choice(data)

def vs_game():
    score = 0
    game_over = False
    A = random_person()

    print(logo6)
    while not game_over:

        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")

        print(vs)

        B = random_person()
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ")

        clear()
        print(logo6)

        if choice == 'A':
            if A['follower_count'] > B['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                game_over = True
                print(f"Sorry, that's wrong. final score: {score}")

        elif choice == 'B':
            if A['follower_count'] < B['follower_count']:
                A = B
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                game_over = True
                print(f"Sorry, that's wrong. final score: {score}")


vs_game()

