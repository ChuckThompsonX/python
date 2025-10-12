'''
Demonstration of Instance, Class, and Static Methods in Python.
Methods within a class can be categorized into three main types 
based on how they interact with the class and its instances.
'''

class Employee:
    company = "MyCompany"  # Class variable
    department = "IT"  # Class variable
  
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    # Instance method
    def print_employee_info(self):
        print(f"The co is {self.company}.")
        print(f"Name is {self.name}.")
        print(f"Salary is ${self.salary}.")

    # Class Method
    @classmethod
    def change_dept(cls, dept):
        cls.department = dept
    
    # Static Method
    @staticmethod
    def print_dept():
        print(f"Department is {Employee.department}.")

# Example usage
e = Employee("Tom Jones", 100000)
print(Employee.company)
e.print_employee_info()
Employee.print_dept()
e.change_dept("Accounting")
print(Employee.department)
