def count_letters(text):
# Remove spaces from the text

text_without_spaces = text.replace(" ", "")

# Count the number of characters

letter_count = len(text_without_spaces)

return letter_count



# Example usage

text = "Hello, World! How are you?"

result = count_letters(text)


print(result) # Output: 21
