#XR, Password Strength Checker

length = False
uppercase = False
lowercase = False
number = False
symbol = False 
count = 0
strength = "Weak"

password = input("What is your password: ")

for letter in password:
    if len(password) >= 8:
        length = True

for letter in password:
    if letter .isupper():
        uppercase = True

for letter in password: 
    if letter .islower():
        lowercase = True

for letter in password:
    if letter .isnumeric():
        number = True

if letter in ".+?#$%!^&*()":
    symbol = True
print(f"Has a symbol: {symbol}")

if length == True:
    count = count + 1 
if uppercase == True:
    count = count + 1
if lowercase == True:
    count = count + 1 
if number == True:
    count = count + 1 
if symbol == True:
    count = count + 1 

if count == 5:
    strength = "Strong"
if count <= 4:
    strength == "Medium"
if count < 3:
    strength = "Weak"

print(f"You have a {strength} password.")
print(f"You have done {count}/5")
print(f"If you dont have a 5/5, you should check if you have a uppercase letter, lowercase letter, a number, and a symbol.")


 