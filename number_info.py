#XR, Number Information

for number in range (1,21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(f"{number} is even and can be divisible by 5")
        else:
            print(f"{number} is even and cannpt be divisible by 5")
    else:
        if number % 5 == 0:
            print(f"{number} is odd and can be divisble by 5")
        else:
            print(f"{number} is odd and cannot be divisible by 5")