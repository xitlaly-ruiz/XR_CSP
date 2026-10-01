#XR, C
# ord is the ascii number
# Check if letter convert it to number increase to number user told me convert back to letter print it.
# 4. tp turn it back you have to decript it so do the opposite of the incript (changeing number
# to a negative will let you decript)

userpick = input("Which one would you like to do , encrypt or decript: ")
message = input("Enter the message you would like for this: ")
shiftamount = int(input("How much would you like to shift by: "))

def cipher_shiftamount(message,shiftamount):
    result = ""
    for chr in message:
        if chr.isupper():
           # resut += (char((ord)(chr) - ))