# XR, Number Guessing Game
import random

answer = random.randint(1, 100)
guesses = 0

while guesses < 6:
	guess = int(input("Guess a number from 1 to 100: "))
	guesses = guesses + 1

	if guess == answer:
		print(f"Correct you got it in {guesses} tries!")
		break
	elif guess < answer:
		print("Guess higher")
	else:
		print("Guess lower")

if guess != answer:
	print(f"Your out of tries. The answer was {answer}")






