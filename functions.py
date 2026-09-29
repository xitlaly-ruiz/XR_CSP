# XR, Function Notes
def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"What is your monthly {money}: "))
            return amount
        except:
            print("That isnt a number:(")
# Takes aways repeating code
# Makes code easy to read
# break down problems into smaller peices

# Write all your variables
income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
groceries = stupid_proof("groceries")
trasportation = stupid_proof("transportation")
saving = income *.1



income = float(input("What is your monthly income: "))
rent = float(input("What is your monthly rent: "))
utilities = float(input("What is your monthly utilities: "))
groceries = float(input("What is your monthly groceries: "))
trasportation = float(input("What is your monthly transportation: "))
saving = income * .1
# Write any functions you are using
def calc_percent(income, bill): 
    return round(bill/income *100)
# Outputs for the user
print(f"Your rent is ${rent:.2f} that is {calc_percent(income,rent)}% of your income")
print(f"Your rent is ${utilities:.2f} that is {calc_percent(income,utilities)}% of your income")
print(f"Your rent is ${groceries:.2f} that is {calc_percent(income,groceries)}% of your income")
print(f"Your rent is ${trasportation:.2f} that is {calc_percent(income,trasportation)}% of your income")
print(f"Your rent is ${saving:.2f} that is {calc_percent(income,saving)}% of your income")
print(f"You have ${income-rent-utilities-groceries-trasportation-saving:.2f} left to spend!")

# def = define(defines the function)
# calc_percent <= make function
# After your variable name put ()
# (income, bill) make peramiters (piece of ingo needed for variable to run)
# (income, bill): <= end line with collen
# Make indent in the next line when adding a collen
# make the function => return round(bill/income)
# return <= output to function call
# { function call => calc_percent(income,rent) <= arguments} parameter = argument
# argument = value of your parementer when you call your function