#XR, C
# ord is the ascii number
# Check if letter convert it to number increase to number user told me convert back to letter print it.
# 4. tp turn it back you have to decript it so do the opposite of the incript (changeing number
# to a negative will let you decript)

userpick = input("Do you want to (E)encrypt or (D)decrypt a message: ").strip().upper()
message = input("Enter the message you would like for this: ")
shiftamount = int(input("How much would you like to shift by: "))

def cipher_shiftamount(message,shiftamount):
    result = ""
    for chr in message:
        if chr.isupper():

def caesar_shift(message,shiftamount):
    the_result = ""
    for char in message:
        if char.isupper():
            the_result += chr((ord(char) - ord("A") + shiftamount) % 26 + ord("A"))
        elif char.islower():
            the_result += chr((ord(char) - ord("a") + shiftamount) % 26 + ord("a"))
        else:
            the_result += char
    return the_result

if userpick == "E":
    the_result = caesar_shift(message, shiftamount)
    print(f"You encrypted message is: {the_result}")

elif userpick == "D":
    the_result = caesar_shift(message, -shiftamount)
    print(f"Your decrypted message is: {the_result}")
