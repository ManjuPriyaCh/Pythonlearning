


def outer_function():
    var1 = 30  # local int variable

    def inner_function():
        print(var1)

    def inner_function2():
        print(var1+1)

    inner_function()
    inner_function2()



outer_function()    # to get inner function we need to call outer function first