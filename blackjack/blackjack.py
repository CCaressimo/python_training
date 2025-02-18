"""Blackjack game"""
import random
from os import system
from art import BLACKJACK

def final_hand(p_score, d_score):
    """Prints hands"""
    result = "Draw"
    if d_score == 0:
        result = "Dealer has Blackjack, you lose!"
    elif p_score == 0:
        result = "Blackjack!"
    elif p_score > 21:
        result = "Busted!"
    elif d_score > 21:
        result = "Dealer busted!"
    elif p_score > d_score:
        result = "You win!"
    elif p_score < d_score:
        result = "Dealer wins!"
    return result

def play_game():
    """Play a game of blackjack"""
    playerhand = []
    dealerhand = []
    dealer_score = -1
    player_score = -1
    is_game_over = False

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def deal_card():
        """Returns a random card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    for _ in range(2):
        playerhand.append(deal_card())
        dealerhand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(playerhand)
        dealer_score = calculate_score(dealerhand)

        print(f"Your cards: {playerhand}, current score: {sum(playerhand)}")
        print(f"dealer's first card: {dealerhand[0]}")


        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_deal_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if player_deal_input == 'y':
                playerhand.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealerhand.append(deal_card())
        dealer_score = calculate_score(dealerhand)

    print(f"Your final hand: {playerhand}, final score: {sum(playerhand)}")
    print(f"dealer's final hand: {dealerhand}, final score: {sum(dealerhand)}")

    print(final_hand(player_score, dealer_score))

while input("Would you like to play a game of Blackjack? 'y' or 'n'? ").lower() == 'y':
    system("clear")
    print(BLACKJACK[0])
    play_game()
