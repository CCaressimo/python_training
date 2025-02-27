"""Reproduce and fix bugs"""
import random

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = random.randint(0, 5)
# print(dice_images[6]) Reproduce error
print(dice_images[dice_num])

# One line needed to be >= or <=
year = int(input("What year were you born in?\n"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Use a try catch to prevent ValueErrors
try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("Enter a numerical number.")
    age = int(input("How old are you?\n"))

# Fstring to input a variable
if age > 18:
    print(f"You can drive at age {age}")

# Use print statements
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
print(f"pages: {pages}")
print(f"words per page: {word_per_page}")
total_words = pages * word_per_page
print(total_words)
