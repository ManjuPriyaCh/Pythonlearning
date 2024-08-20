#Task 2
'''Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}'''

# To Take 2 inputs from the user
num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))

# To know the type of user input
print(type(num1))
print(type(num2))

# To perform Max,power, sub,mul,sum and div
print("Maximum is ",max(num1,num2))
print(f"Maxi of {num1,num2} is {max(num1,num2)}")

print("Power is ",pow(num1,num2))
print(f"Power of {num1,num2} is {pow(num1,num2)}")

print("Subtraction is ",(num1-num2))
print(f"Subtraction of {num1,num2} is {(num1-num2)}")

print("Multiplication is ",(num1*num2))
print(f"Multiplication of {num1,num2} is {(num1*num2)}")

print("Sum is ",(num1+num2))
print(f"Sum of {num1,num2} is {(num1+num2)}")

print("Division is ",(num1/num2))
print(f"Division of {num1,num2} is {(num1/num2)}")




