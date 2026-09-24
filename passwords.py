#XR, Password Strength Checker

length = False
uppercase = False
lowercase = False
number = False
symbol = False 

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

if letter in "+?#$%!^&*()":
    symbol = True




 