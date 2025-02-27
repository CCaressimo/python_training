"""Game of high low"""
import random
from os import system
from game_data import cars
from art import TITLE, VS

def car_details(first_choice, second_choice):
    """Print car details"""
    print(f"A) {first_choice['year']} "
        f"{first_choice['make']} "
        f"{first_choice['model']}")
    print(f"{VS}")
    print(f"B) {second_choice['year']} "
        f"{second_choice['make']} "
        f"{second_choice['model']}")

def player_choice():
    """Function to difine player's choice"""
    player_guess = input("Which car is faster? 'A' or 'B'\n").upper()
    while player_guess != 'A' and player_guess != 'B':
        print("Please answer with 'A' or 'B'")
        player_guess = input("Which car is faster? 'A' or 'B'\n").upper()
    return player_guess

def fastest_car(first_choice, second_choice):
    """Determine which car is faster, and if the player guess is correct"""

    if int(first_choice['horsepower']) > int(second_choice['horsepower']):
        return 'A'
    return 'B'


def game():
    """Play High/Low"""
    score = 0
    second_choice = random.choice(cars)

    play_game = True
    while play_game:
        print(f"Current score: {score}")

        first_choice = second_choice
        second_choice = random.choice(cars)
        for _ in cars:
            if second_choice['model'] == first_choice['model']:
                second_choice = random.choice(cars)

        car_details(first_choice, second_choice)


        fastest_car(first_choice, second_choice)

        if player_choice() == fastest_car(first_choice, second_choice):
            score += 1
            print(f"Correct! Current score: {score}")
            system("clear")
        else:
            play_game = False
            print(f"You guessed wrong, total score: {score}")

        

while input("Would you like to guess which car is faster? Hit enter to play or 'n' to quit: ").lower() != 'n':
    system("clear")
    print(TITLE)
    game()
