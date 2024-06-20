from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list
import random

lives = 6
endofgame = False

_word = random.choice(word_list)
word = list()
for i in _word:
    word.append(i)

display = list()
for i in range(len(word)):
    display.append('_')

print(logo)
print('The solution is', ''.join(word), '\n')

while (endofgame == False):

    guess = input('Guess a letter: ').lower()
    clear()
    if guess in display:
        print("You've already guessed {}\n".format(guess))
        continue

    if guess not in word:
        print("You guess {}, that's not in the word. You lose a life.".format(guess))
        lives -= 1
        print(''.join(display))
        print(stages[lives])
    
        if lives == 0:
            endofgame = True
            print('You lose')
        

    else:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print(''.join(display))
        print(stages[lives])


    if word == display:
        endofgame = True
        print('You win!')
    
    print()
