# XR, Number Guessing Game
# XR, Number Guessing Game
import random

answer = random.randint(1, 100)
guesses = 0

while guesses < 6:
	guess = int(input("Guess a number 1-100: "))
	guesses += 1

	if guess == answer:
		print(f"Good job! You got it in {guesses} tries.")
		break
	elif guess < answer:
		print("Guess higher")
	else:
		print("Guess lower")
else:
	print(f"You ran out of tries. The answer was {answer}.")
