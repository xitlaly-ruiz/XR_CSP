#XR, Reading and Writing to Files
# with open = key word to open your/a file
# File path= how you get the file
#
#           File path    what we do with this file 
with open("practice.txt", "r+") as file: #< name of file in code (lets you read and write)
    content = file.read()
    #               ^ gives what is written on the file
    content = "Chapter 1:\n" + content + " And Christopher Robin was sitting on his doorstep putting on"
    "his big boots"
    file.write(content)

with open("practice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day")

# r = read
# w = write <= replaces the content
# a = append <= add content to the end
# \n <= starts a new line
