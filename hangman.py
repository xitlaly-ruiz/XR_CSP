#XR, Hangman

import random

# The player gets 6 wrong guesses before losing the game
MAX_WRONG_GUESSES = 6

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


def load_words():
    with open("words.txt", "r") as file:
        lines = file.read().splitlines()

    words = []
    for word in lines:
        cleaned_word = word.strip().lower()
        if cleaned_word != "":
            words.append(cleaned_word)
    return words


def load_stats():
    try:
        with open("stats.txt", "r") as file:
            lines = file.readlines()

        wins = int(lines[0].split("=")[1].strip())
        losses = int(lines[1].split("=")[1].strip())
    except (FileNotFoundError, IndexError, ValueError):
        wins = 0
        losses = 0

    return wins, losses


def save_stats(wins, losses):
    with open("stats.txt", "w") as file:
        file.write(f"wins = {wins}\n")
        file.write(f"losses = {losses}\n")


def show_word(secret_word, guessed_letters):
    result = ""
    for letter in secret_word:
        if letter in guessed_letters:
            result += letter.upper() + " "
        else:
            result += "_ "
    return result.strip()


def main():
    print("getting the word list from words txt")
    words = load_words()
    if not words:
        print("there are no words in words txt")
        return

    wins, losses = load_stats()
    print(f"getting the stats from stats txt you have {wins} wins and {losses} losses")

    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    print("lets play hangman")

    while True:
        # Show the drawing that matches the number of wrong guesses
        print(hangman_art[wrong_guesses])
        current_display = show_word(secret_word, guessed_letters)
        print("word", current_display)

        if guessed_letters:
            guessed_list = " ".join(letter.upper() for letter in guessed_letters)
            print("letters you guessed", guessed_list)
        else:
            print("letters you guessed none yet")

        remaining = MAX_WRONG_GUESSES - wrong_guesses
        print(f"wrong guesses left {remaining}")

        if "_" not in current_display:
            print(f"you got it the word was {secret_word.upper()}")
            wins += 1
            save_stats(wins, losses)
            print(f"your total score is {wins} wins and {losses} losses")
            break

        if wrong_guesses == MAX_WRONG_GUESSES:
            print(f"game over the word was {secret_word.upper()}")
            losses += 1
            save_stats(wins, losses)
            print(f"your total score is {wins} wins and {losses} losses")
            break

        guess = input("guess a letter ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("type just one letter")
            continue

        if guess in guessed_letters:
            print("you already guessed that one try a different letter")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"nice {guess.upper()} is in the word")
        else:
            wrong_guesses += 1
            print(f"oops {guess.upper()} is not in the word")


if __name__ == "__main__":
    main()
