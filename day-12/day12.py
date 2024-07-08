# 숫자 맞추기 게임
import random
from art import logo5

def guess_number(chance):
    num = random.randint(1,100)
    attempts = chance
    game_over = False

    while attempts > 0:

        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))

        if guess == num:
            print(f'You got it! The answer was {num}')
            return

        elif guess > num:
            print('Too high.\nGuess again.')
            attempts -= 1

        else:
            print('Too low.\nGuess again.')
            attempts -= 1

    print("You've run out of guesses, you lose.")
    return

print(logo5)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    guess_number(10)

elif difficulty == 'hard':
    guess_number(5)

