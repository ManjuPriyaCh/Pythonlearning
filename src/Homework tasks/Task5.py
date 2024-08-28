# - Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))

if num1 > num2:
    print(f"{num1} is greater than 5{num2}")
elif num1 < num2:
    print(f"{num1} is Less than {num2}")
else:
    print(f"{num1} and {num2} are equal")

# print(num1 > num2)
# print(num1 < num2)
# print(num1 == num2)
