# ========== PSEUDO CODE ==========
# - Printing "VOWEL COUNTER FOR ALF"
print("VOWEL COUNTER FOR ALF")

# - Prompt the user to enter a word.
characters = input("Enter a word/s:")


# - Using def function
def count_vowels(text):
    count = 0 # - Count variable
    
    for i in text: # - Using 'for loop' function
        if (i in "aAeEiIoOuU"):
            count += 1
    return count

result = count_vowels(characters)


# - Displaying the result or counted vowels from the user's inputted character or string
print("The number of vowels in", characters, "is", result)


