import random

hangman_art = [
"""
_______
|     |
|
|
|
|
_________""",

"""
_______
|     |
|     O
|
|
|
_________""",
"""
_______
|     |
|     O
|     |
|
|
_________""",
"""
_______
|     |
|     O
|    /|
|
|
_________""",
"""
_______
|     |
|     O
|    /|\\
|
|
_________""",
"""
_______
|     |
|     O
|    /|\\
|    /
|
_________""",
"""
_______
|     |
|     O
|    /|\\
|    / \\
|
_________""",
]

with open("list.txt", "r") as file:
    words = file.read().split(",")

with open("wins_loses.txt", "r") as file:
    score_lines = file.readlines()
    wins = int(score_lines[0].split("=")[1])
    losses = int(score_lines[1].split("=")[1])

answer = random.choice(words).strip().lower()
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
won = False

print("Hello welcome to hangman! You have 6 attempts to guess the word")

while wrong_guesses < max_wrong_guesses:
    print(hangman_art[wrong_guesses])
    shown_word = ""
    for letter in answer:
        if letter in guessed_letters:
            shown_word = shown_word + letter + " "
        else:
            shown_word = shown_word + "_ "

    print(f"\nWord: {shown_word}")
    print(f"Attempts remaining: {max_wrong_guesses - wrong_guesses}")

    if "_" not in shown_word:
        print("You win!")
        wins = wins + 1
        won = True
        break

    guess = input("Guess a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess not in answer:
        wrong_guesses = wrong_guesses + 1
        print("That letter is not in the word.")

if not won:
    print(hangman_art[wrong_guesses])
    print(f"\nYou lose! The word was: {answer}")
    losses = losses + 1

print(f"Score: {wins} wins, {losses} losses")
with open("wins_loses.txt", "w") as file:
    file.write(f"win = {wins}\n")
    file.write(f"loss = {losses}\n")
