
'''Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13'''

'''# logic
start with 0 and 1
Fn=Fn-1+Fn-2
'''

num = int(input("Enter number to get the fibonacci series :  "))
#print(num)
x,y = 0,1
if num == 0:
    print(f"Fibonacci Series for {num}:{num}")

elif num == 1:
    print(f"Fibonacci Series for {num}:{0,1}")
else:
     