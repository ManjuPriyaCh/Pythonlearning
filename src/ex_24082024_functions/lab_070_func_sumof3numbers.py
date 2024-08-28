def sum_of_three_number(a=5, b=10, c=15):
    return a + b + c


# result = sum_of_three_number(10, 20, 30)  # consider as a=10,b=20,c=30
# result = sum_of_three_number(10, 20)     # consider as a, b and c as default value 15
# result = sum_of_three_number(10)      # consider only a =10 and b abd c as default value
# result = sum_of_three_number()        # a,b,c are default values
result = sum_of_three_number(a=78, c=67)       # b will be default value
print(result)