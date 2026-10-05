import random

guess = 0

# with open("","r") as file:
#   words = file.read().split(",")

with open ("list.txt", "r") as file:
    words = file.read().split(",")
answer = random.choice(words)
""" _____
    |    |
    |    O
    |   /|\\
    |   /\\
    |________
    """
for answer in range (1,answer+1):
    letter = input("Welcome to Hangman, you have 6 attempts to guess the right letter: ")
"""_____
   |    |
   |    o
   |   /|\\
   |   /\\
   |________"""
