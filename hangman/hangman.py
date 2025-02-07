"""
Building a hangman game to incorporate statements and loops
"""

import random
from hangman_words import word_list
from hangman_stages import stages

random_word = random.choice(word_list)
BLANK_WORD = ""
LIVES = 0

for letter in random_word:
    BLANK_WORD += letter.replace(letter, "_")

display = list(BLANK_WORD)

# print(random_word)
print(BLANK_WORD)


while (''.join(display)) != random_word:
    guessed_letter = input("Guess a letter: ").lower()

    FOUND = False

    # for i in range(len(random_word)):
    #     if display[i] == guessed_letter:
    #         print("Already guessed")
    #     elif random_word[i] == guessed_letter:
    #         display[i] = guessed_letter
    #         found = True

    for i, letter in enumerate(random_word):
        if display[i] == guessed_letter:
            print("Already guessed")
        elif letter == guessed_letter:
            display[i] = guessed_letter
            FOUND = True


    if not FOUND:
        LIVES += 1
        print(stages[LIVES])

    print(''.join(display))

    if (''.join(display)) == random_word:
        print("You win")
    elif LIVES == 6:
        print("You lose")
        print(f"The word was {random_word}")
        break
