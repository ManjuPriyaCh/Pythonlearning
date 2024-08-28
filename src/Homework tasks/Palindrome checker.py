# Create a program that checks whether a given string is a palindrome.
# A palindrome is a word or phrase that reads the same backward as forward
# (ignoring spaces, punctuation, and capitalization).
# Use an if-else statement to determine if the string is a palindrome.


Word = input("Enter Some String to check its palindrome or not : ")

if Word == Word[::-1]:
    print(f"Entered Word : {Word},is Palindrome")
else:
    print(f"Entered Word : {Word},is not a Palindrome")
