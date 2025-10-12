'''
Instance Methods Example

Purpose: Operate on specific instances of a class. They are the most common type of method.
Decorator: No special decorator is needed.
First Argument: Implicitly takes self as its first argument, which refers to the instance of the 
class on which the method is called.
Access: Can access and modify both instance-specific attributes (using self.attribute_name) and 
class attributes (using ClassName.attribute_name or self.__class__.attribute_name).
Use Case: When a method needs to work with or modify the data unique to a particular object.
'''

class MyClass:
    def __init__(self, value):
        self.instance_value = value

    def instance_method(self):
        print(f"Instance value: {self.instance_value}")
        
im = MyClass(10)
print(im.instance_value)  # Accessing instance variable directly
