'''
Class Methods Example

Purpose: Operate on the class itself, not a specific instance. They are often used for factory methods 
or methods that need to access or modify class-level data.
Decorator: Defined using the @classmethod decorator.
First Argument: Implicitly takes cls as its first argument, which refers to the class object itself.
Access: Can access and modify class attributes (using cls.attribute_name), but generally cannot directly 
access instance attributes without an instance.
Use Case: When a method needs to work with class-level data or create instances of the class in a 
specific way (e.g., alternative constructors).
'''

class MyClass:
    class_value = "Class Data"

    @classmethod
    def class_method(cls):
        print(f"Class value: {cls.class_value}")
        
cm = MyClass()
cm.class_method()  # Calling class method via instance