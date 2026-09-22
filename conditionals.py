# XR, Conditionals Notes
#Boolean => True or False
# conditional
# every conditional starts with if. Evertime line of code ends in collen, next line has to be indented
# indented lines only happen when condition above is True. End of conditional=else
# Else is aslong as the conditons above are false this will happen, == <= equal to. ! <= not equal to
# Logical operators = and (both conditions must be true), or(at least one must be true), not(checks if false)
# nesting is when you put one of something indside of another conditional.

time = 1416
day = "Tuesday"
if time < 1200 and time > 500: #<= Boolean statement
    print("Good morning!")
    if day != "Saturday" or day != "Sunday":
        print("Are you ready for school?")
elif time < 1700: 
    print("Good Afternoon!")
    if day != "Saturday" and day != "Sunday":
        print("How has school been?")
elif time < 2000:
    print("Good Evening!")
else:
    print("Good Night!")

print("Code is done")
