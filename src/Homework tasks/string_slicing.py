

# String slicing

text = "Hello, World"

#slice = text[start:end:step]  # start from 0 and end=end-1, default step is 1

slice1 = text[0:5] #Hello>> start with 0 and end with 4
print(slice1)
slice2 = text[5:]   #  , World >>Start with 5 and ends with upto last word
print(slice2)
slice3 = text[:5]  # Hello >>start with 0 and at end 4
print(slice3)

slice4 = text[::2]  # Hlo ol>> 2 steps will move means 0,3,6,9,.. will display
print(slice4)
slice5 = text[::-1]  # to reverse the entire word
print(slice5)