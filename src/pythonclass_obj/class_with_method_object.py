class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
         #return f" {self .name} {self.age}"
         print(f"Employee Name is ---- {self.name}")
         print(f"Employee Age is ---- {self.age}")



p1 = Person("John",16)   # object1 creation
p1.__str__()  # calling the methods/function of the class

print("------------------------------")

p2 = Person("Smith",45)   # object2 creation
p2.__str__()  # calling the method


