class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
         return f" {self .name} {self.age}"



p1 = Person("John",16)   # object creation

print(p1)
print(f"Employee details is ---- {p1}")
print(f"Employee Name is ---- {p1.name}")
print(f"Employee Age is ---- {p1.age}")

