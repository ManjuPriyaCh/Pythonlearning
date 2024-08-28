# Find factorial
# 5!=5*4*3*2*1>>
number = int(input("Enter number to get the factorial: "))
s = 1
# if number == 1:
#print(1)
# else:
for i in range(number, 0, -1):
    # print(i)
    s = s * i
print(f"factorial of {number} is  {s}")
