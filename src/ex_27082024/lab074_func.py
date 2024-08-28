
# different functions with multiple args
#Note : only one multiple arg can pass at atime
def make_pizza(*toppings, base):
    print(toppings, base)


def make_pizza_2(*base,topping):
    print(base, topping)


make_pizza("mushroom", "tomato", "cheese", base="thin crust")
make_pizza_2("crust","thin crust",topping="cheese")