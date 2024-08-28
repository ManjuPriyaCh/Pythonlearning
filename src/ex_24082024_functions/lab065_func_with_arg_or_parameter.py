


# functions with argument, parameters
# parameter can be str,int,float,bool,
def greet():
    print("Hello, there!!")


def greet_by_name(pramod): # name -> variable name, argument | parameter
    print("Hello,", pramod)


def func_name(var_name):
    print(var_name)


#func_name()   # its wrong bcoz in function var_name is mandatory so we have to call any var_name while calling
func_name("manju")
greet()
#greet_by_name()
greet_by_name("Manju")
func_name("Priya")
greet_by_name(123)
greet_by_name(True)
greet_by_name(3.14)