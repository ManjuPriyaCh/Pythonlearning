# User Defined
# 1. The can't return -> non return
# 2.They can return something
# They have parameters
# They don't parameters / arguments


# 1. The can't return -> non return
# # No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello World")


result = greet()
print(result)                 # Result type is None means no return


# 2. # No Return Type and with Argument
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Manju")
result = greet_by_name("Priya")
print(result)        # Result type is None means no return




# # 3. No Return Type and with Default Argument
def say_hello_default_arg(name="pramod"):     # default name is pramod
    print("Hello", name.upper())   # to print the text in upper case
    print("Hello", name.lower())    # to print the text in lower case


say_hello_default_arg("Tanvish")
say_hello_default_arg()           # if we don't pass anything while calling then it consider the default name
say_hello_default_arg(name="Sai")  # positional argument

print(say_hello_default_arg("sandy"))    # none type



def multiple_args(name1="Arha", name2="SAI", name3="Amira"):   # defining argument with default values
    print("Multiple Arguments", name1, name2, name3)

multiple_args() # all deafult values will print
multiple_args(name1="Ram", name2="Manju", name3="Sree")  # these values will print
multiple_args(name1="SANDYY")  # except name1 remaining default values will print


# 4. Argument + return Type
def sum_of_two_number(num1, num2):
    return num1 + num2


def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2



# result = sum_of_two_number(10, 34)
result = sum_of_two_number(num1=34, num2=34)
#print(result) #34+34=68 will display
result = sum_of_two_number_with_default()
print(result)  # recent result will print 100+200=300