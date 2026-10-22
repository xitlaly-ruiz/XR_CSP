#XR fixed ticket code
age = int(input("Enter your age: "))
if age < 0:
  print("invalid age!")
matinne = input("Is this a matinee (yes/no): ").strip().lower()

if age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes":
    price = price - 3
    if price < 0:
      price = 0
print(f"Ticket price: ${price.2f}")
