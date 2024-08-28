

# ✅ Understanding Decorators in Python

def add_before_ui_after_ui(custom_function_where_you_want_extra_func):    # defining decorator
    # two parts
    # wrapper & call
    def wrapper():                 # inner function
        print("Before the running UI TC")
        print("Start the Browser ")
        custom_function_where_you_want_extra_func()
        print("Ending the running UI TC")
        print("Quit the Browser!")

    return wrapper()


@add_before_ui_after_ui                            # adding decorator to the base func
def test_ui():                                     # base function
    print("I will Test the UI")