#XR, Password Strength Checker

length = False
uppercase = False
lowercase = False
number = False
symbol = False
count = 0
strength = "Weak"

password = input("What is your password: ")

if len(password) >= 8:
    length = True

for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if letter in ".+?#$%!^&*()":
        symbol = True

if length:
    count += 1
if uppercase:
    count += 1
if lowercase:
    count += 1
if number:
    count += 1
if symbol:
    count += 1

if count == 5:
    strength = "Strong"
elif count >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print(f"At least 8 characters: {length}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"You have a {strength} password.")
print(f"You have done {count}/5")
if strength != "Strong":
    print("Missing:")
    if not length:
        print("At least 8 characters")
    if not uppercase:
        print("An uppercase letter")
    if not lowercase:
        print("A lowercase letter")
    if not number:
        print("A number")
    if not symbol:
        print("A symbol")

 