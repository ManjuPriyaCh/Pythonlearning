
# how can we use function within other function eg

# def and call
# user defined functions

def greet_to_all_of_you():
    print("Hello, Everyone")

#.lower() - string
def greet():
    print("Yes")
    greet_to_all_of_you()

greet_to_all_of_you()     # Hello, everyone will display bcoz we have call greet_to_all_of_you