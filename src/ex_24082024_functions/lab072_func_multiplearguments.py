def print_arguments(*args):
    # *args = multiple argument with no limit, -> list
    # print(args[0])
    for i in args:
        print(i)

# list = ["pramod", "amit", "lucky"]

print_arguments("pramod", "amit", "lucky")
print_arguments("amira", "lucky")
print_arguments("amira", 10)   # we can pass different data type params
print_arguments("amira", 10, True)
print_arguments("amiraa", 10, True, False)
print_arguments("amiraaa", 10, True, False, "PRAMOD")
print_arguments("lucky")
# print_arguments() -minimum 1 arguement is important


print("amit")
print("pramod", "amit")
print("pramod", "amit", True)
print("pramod", "amit", True, False)