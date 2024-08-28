

def sum_of_three_user_inputs(num1,num2,num3):
    return num1+num2+num3

num1 = int(input("Enter num1 value: "))
num2 = int(input("Enter num2 value: "))
num3 = int(input("Enter num3 value: "))

result = sum_of_three_user_inputs(num1,num2,num3)
print("Sum is",result)
result = sum_of_three_user_inputs(10,10,10) # if enter number in() it will automatically show num1,..)
print("Sum is",result)




# Create a program to sum of three number from the user input

numb1 = int(input("Enter the the numb 1 ")) # 100
numb2 = int(input("Enter the the numb 2 ")) # 200
numb3 = int(input("Enter the the numb 3 ")) # 300


def sum_of_three_number(n1, n2, n3):
    return n1 + n2 + n3

result = sum_of_three_number(numb1,numb2,numb3)    # need to pass variable name in ()
print(result)
result = sum_of_three_number(100, 200, 300)
print(result)