#XR, Nesting
count = 2 

while count <= 20:
    print(count)
    count += 2


    for number in range(2,22,2):
        print(number)

for number in range(1,21):
    if number % 15 ==0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

siblings = ["Nazareth", "Galilea", "Leticia", "Esperanza"]
count = 1
if len(siblings) > 0:
    while count <= len(siblings):
        print(f"{count}. {siblings[count]}")
        count += 1
else:
    print("There are no siblings")