"""
Random generator for rock, paper, scissors
"""

import random


move_set = ["rock", "paper", "scissors", "gun!"]
computer_move = random.randint(0,3)

print("Lets play Rock, Paper, Scissors")

player_move = int(input("What is your move? 0 for rock, 1 for paper, and 2 for scissor\n"))
if player_move >= 0 and player_move <= 3:
    print(f"Player chose:\n{move_set[player_move]}")

print(f"Computer chose:\n{move_set[computer_move]}")


if player_move >=4 or player_move < 0:
    print("Invalid input...")
elif player_move == 0 and computer_move == 2:
    print("Player wins!")
elif player_move == 2 and computer_move == 0:
    print("The computer won...")
elif computer_move == 3 and player_move == 3:
    print("It's a wild west duel!")
    computer_shot = random.randint(0, 5)
    player_shot = random.randint(0, 5)
    print(f"The computer shot off {computer_shot} rounds!")
    print(f"The player shot off {player_shot} rounds!")
    if player_shot > computer_shot:
        print("The player gunned down the computer")
    elif player_shot == computer_shot:
        print("They killed eachother?!")
    else:
        print("The player got gundowned by the computer...")
elif player_move == 3 and computer_move != 3:
    print("The player executed the computer like a dog!")
elif player_move != 3 and computer_move == 3:
    print("The computer stands up and puts 6 holes into the players head...")
elif computer_move > player_move:
    print("The computer won...")
elif computer_move < player_move:
    print("Player wins!")
elif player_move == computer_move:
    print("tie!")
