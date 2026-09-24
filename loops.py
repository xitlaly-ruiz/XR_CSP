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

sibilings = ["Cortez", "Galilea", "Nazareth", "Leticia", "Esperanza"] #<= surround by brackets
print(sibilings[2])
