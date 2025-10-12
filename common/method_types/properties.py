"""
The @property decorator in Python is a built-in decorator that allows you to define methods 
in a class that can be accessed like attributes, providing a "Pythonic" way to manage 
attribute access. It simplifies the implementation of getters, setters, and deleters for 
class attributes without the need for explicitly calling methods.
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Radius deleted!")
        del self._radius

    def area(self):
        if hasattr(self, '_radius'):        
            import math
            return math.pi * (self._radius ** 2)
        else:
            raise AttributeError("Radius is not defined")

# Example usage
c = Circle(5)
print(c.radius)  # Accessing the radius property
print(c.area())  # Calculating area
del c.radius  # Calls the deleter
print(c.area())  # This will raise an error since radius is deleted
