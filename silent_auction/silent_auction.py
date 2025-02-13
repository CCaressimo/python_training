"""Simulate a silent auction with dictionaries"""
from os import system

silent_auction = {}
AUCTION = True

while AUCTION:
    bidder = input("What is your name?\n")
    bid_price = input("What is your bid?\n")
    finish_auction = input("Are there any other bidders? 'yes' or 'no'?\n").lower()

    if finish_auction == "no":
        silent_auction[bidder] = bid_price
        system("clear")
        highest_bidder = max(silent_auction, key=silent_auction.get)
        print(f"The highest bidder is:\n{highest_bidder} for {silent_auction[highest_bidder]}!!")
        AUCTION = False
    else:
        silent_auction[bidder] = bid_price
        system("clear")
