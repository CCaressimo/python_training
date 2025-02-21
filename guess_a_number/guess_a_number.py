"""A number guessing game"""

import random
from os import system
from art import ART

EASY_DIF = 10
HARD_DIF = 5

def check_answer(player_guess, actual_number):
    """Compare player guess with the actual number"""
    if player_guess > actual_number:
        print("Too high!")
    elif player_guess < actual_number:
        print("Too low!")
    else:
        print(f"You guessed correctly! {actual_number}")

def set_difficulty():
    """Set player difficulty"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'hard':
        return HARD_DIF

    return EASY_DIF


def game():
    """Play a guessing game"""
    answer = random.randint(1, 100)
    turns = set_difficulty()
    print("Lets play a guessing game!")
    print("I'm thinking of a number between 1 and 100...")


    player_guess = 0
    while player_guess != answer and turns > 0:
        print(f"Guesses left: {turns}")
        while True:
            try:
                player_guess = int(input("Guess a number: "))
                break
            except:
                print("Please guess a number")

        check_answer(player_guess, answer)
        turns -= 1
        if turns == 0:
            print(f"Game over\nThe correct guess was {answer}")



while input("Would you like to guess a number? Hit enter to play or 'n' to quit: ").lower() != 'n':
    system("clear")
    print(ART)
    game()
