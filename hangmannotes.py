# create a list of ten words cat,dog,bird

# create another file holds win/loss count
# use split(",") on the content of the words txt document to create your list of words
# Pull win and loose totals from the other txt file and save then as 2 seperate variables

#Build the hangman game

# Save and correct word as a variable random.choice(name of the list)
# num of wrong guesses
# What letters have been guessed


#Function to display the hangman (Needs number of wrong guesses)
""" _____
    |    |
    |    O
    |   /|\\
    |   /\\
    |________
    """
# Function to show the letter and spaces (The correct word, letters that have been guessed)
#Loop over the correct word
    #variable for dispaly word (starts as an empty sting)
    #check if letter has been guessed
        #Then add the letter to the display word
    #if they havent guessed the letter
        #add the underscore to the display word
# return the finished display letter word (outside of the loop)


# Main game loop(while true)
    # call function to show hangman
    # print functino call to show display word
    # create variable and ask user to guess a letter
    # add the letter to list of guessed letter
    # check if not letter in word:
        #increase incorrect guesses
    # check if display word is same as the word
        # tell user they won
        #increas win total
        #ask if they want to play again
            #reset random word, reset wrong guess count
    #check to see if they lost (if they have 6 wrong guesses)
        #tell them they lost
        #tell them what the word was
        #increase lost count
        #ask if they want to play again
        