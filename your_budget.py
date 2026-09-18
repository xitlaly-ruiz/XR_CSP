#XR, Your Budget

while True: 
    try:
        income = float(input("what is your monthly income?: "))
        break
    except:
        print("This is not what i asked for")

while True: 
    try:
        rent = float(input("what is your monthly rent/mortgage?: "))
        break
    except:
        print("This is not what i asked for")

while True: 
    try:
        utilities= float(input("what is your monthly utilities?: "))
        break
    except:
        print("This is not what i asked for")

while True: 
    try:
        groceries= float(input("what is your monthly groceries?: "))
        break
    except:
        print("This is not what i asked for")

while True: 
    try:
        transportation = float(input("what is your monthly transportion?: "))
        break
    except:
        print("This is not what i asked for")

print(f"Your rent is ${rent:.2f} and that is {int(rent/income*100)}% of your income.")
print(f"Your utilities is ${utilities:.2f} and that is {int(utilities/income*100)}% of your income.")
print(f"Your groceries is ${groceries:.2f} and that is {int(groceries/income*100)}% of your income.")
print(f"Your transportation is ${transportation:.2f} and that is {int(transportation/income*100)}% of your income.")

savings = income/10
leftover = income-(rent+utilities+groceries+transportation+savings)
print(f"You should save ${savings:.2f} a month, that is 10% of your income.")
print(f"You have ${leftover:.2f} of spending money each month!")
    

    
