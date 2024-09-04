'''Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, printdetails,
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions.'''


class Employee:
    def __init__(self, name, age, phone, address, employee_id):
      self.name = name
      self.age = age
      self.phone = phone
      self.address = address
      self.employee_id = employee_id

    def employee_func(self):

        print(f"Employee name is  {self.name}")
        print(f"Employee age is  {self.age}")
        print(f"Employee Phone is  {self.phone}")
        print(f"Employee Address is  {self.address}")
        print(f"Employee Id is  {self.employee_id}")

    def employee_func_walk(self):
         print("Employee Walk")
    def employee_func_talk(self):
        print("Employee Talk")

#------------------------------------------------------------------

name = input("Enter Employee1 name \n")
age = int(input("Enter Age \n"))
phone = int(input("Enter Phone number \n"))
address = input("Enter Address number \n")
employee_id = input("Enter Employee Id  \n")

obj_E1 = Employee(name ,age ,phone ,address ,employee_id)
print("-------------Employee1 Details---------")
obj_E1.employee_func()
print("-----------------")
obj_E1.employee_func_walk()
print("--------------------")
obj_E1.employee_func_talk()

print("-------------E2-----------------------")
name = input("Enter Employee 2 name \n")
age = int(input("Enter Age \n"))
phone = int(input("Enter Phone number \n"))
address = input("Enter Address number \n")
employee_id = input("Enter Employee Id  \n")
obj_E2 = Employee(name ,age ,phone ,address ,employee_id)
print("-------------Employee 2 Details---------")
obj_E2.employee_func()
print("-----------------")
obj_E2.employee_func_walk()
print("--------------------")
obj_E2.employee_func_talk()
