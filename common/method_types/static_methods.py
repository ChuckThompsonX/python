'''
Static Methods Example

Purpose: Utility functions that are logically related to the class but do not depend on the state 
of the class or any specific instance. They are essentially regular functions placed within a class 
for organizational purposes.
Decorator: Defined using the @staticmethod decorator.
First Argument: Does not implicitly take self or cls. It takes only the arguments explicitly passed to it.
Access: Cannot directly access class attributes or instance attributes unless they are explicitly passed as arguments.
Use Case: For helper functions or calculations that are conceptually part of the class but don't require access 
to instance or class state.
'''

class MyClass:
  
    @staticmethod
    def static_method(a, b):
        return a + b
      
result = MyClass.static_method(5, 7)
print(result)  # Outputs: 12