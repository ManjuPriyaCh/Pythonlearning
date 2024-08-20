
#Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

r = float(input("Enter radius of a circle "))
#Circle_Area=3.14*r*r
Circle_Area=3.14*pow(r,2)
print(f"Area of a circle with radius {r} is {Circle_Area:.2f}square.units")
