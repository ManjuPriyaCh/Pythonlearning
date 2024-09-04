
# simple class with an objective
class Employee:
    def __init__(self,name,age):
      self.name = name
      self.age = age


Object_E1 = Employee("Manju",30)
print(Object_E1.name)
print(Object_E1.age)
print("Employee name is " + Object_E1.name)
#print("Employee age is " + Object_E1.age) # we cannot concatenate string and int, so it won't work for interger type
print(f"Employee name is ---> {Object_E1.name}")
print(f"Employee age is ---> {Object_E1.age}")


