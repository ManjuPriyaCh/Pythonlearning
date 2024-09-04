


# simple class with multiple objective
class Employee:
    def __init__(self, name, age, address):   # __init__ is a default constructor which can we called automatically while creating an object instance
      self.name = name
      self.age = age
      self.address = address


Object_E1 = Employee("Manju", 30, "Hyd")
print(Object_E1.name)
print(Object_E1.age)
print(Object_E1.address)
print("Employee name is " + Object_E1.name)
print("Employee address is " + Object_E1.address)
print(f"Employee name is ---> {Object_E1.name}")
print(f"Employee age is ---> {Object_E1.age}")
print(f"Employee address is ---> {Object_E1.address}")

print("-----------------------------------------------")

Object_E2 = Employee("Tanu",20,"Chennai")
print(Object_E2.name)
print(Object_E2.age)
print(Object_E2.address)
print("Employee name is " + Object_E2.name)
print("Employee address is " + Object_E2.address)
print(f"Employee name is ---> {Object_E2.name}")
print(f"Employee age is ---> {Object_E2.age}")
print(f"Employee address is ---> {Object_E2.address}")


