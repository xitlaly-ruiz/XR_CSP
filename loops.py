#XR, Loops Notes
import random
# everthing indented is apart of while loop. Last line of while loop has to increase iterator

count = 1 # 1: list start point

while count <= 10: # 2: stop point (boolean statement)
    print(count)
    count += 1  # 3: increase the iterator (keeping track of the number of 
                # times youve done the thing. iteratoin what your doing it to) 

ducks = 1 #start
goose = random.randint(1,11)

while True: 
    if ducks == goose: 
        break # ends loop/ stop point
    print("Duck. . . .")
    ducks += 1 #ducks = ducks + 1 (increase iterator place)
print("GOOSE!!!!")

# continue sends you to the begining of the loop

# Complex Data Type = holds other data in it
# every item seperated by commas
# must be valid data type
# bracktes

sibilings = ["Galilea", "Nazareth", "Leticia", "Esperanza"] #<= surround by brackets
print(sibilings[2])
#adding to a list
sibilings.append("Yaneli") # <= adds the item to the end of the list

sibilings.insert(3, "Xitlaly")

print(sibilings)
#remove from a list
sibilings.pop(3) # <= if no number given pop removes the last item
print(sibilings)

#print each item in a list
for sibling in sibilings:
    print(sibilings)

# For loops
for num in range(1,25): #range builds a list for you (start, stop, counting by)
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#for temp in temperature, keyword to start loop is => for
#temp, variable for current iteration
#in, keyword for loop
#temperature, list were looking at


