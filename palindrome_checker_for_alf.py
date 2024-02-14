# ========== PSEUDO CODE ==========
# - Printing the 'PALINDROME CHECKER FOR ALF' 
print("PALINDROME CHECKER FOR ALF")

# - Prompt the user to enter a word.
characters = input("Enter a Word:")


# - Check if the entered word is a palindrome using def function
def if_palindrome_or_not(text):
    reverse_char = text[::-1]
    if reverse_char == text:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")


# - Displaying the result if palindrome or not
if_palindrome_or_not(characters)

