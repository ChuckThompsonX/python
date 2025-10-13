'''
Magic methods or dunder (double underscore) methods , are special methods in Python that 
have names starting and ending with two underscores, like __init__ or __str__. They are not
meant to be called directly. Instead, they allow you to customize how your objects behave with
Python's built-in functions, operators, and syntax.
'''

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Developer-focused output
        return f"Coordinates({self.x!r}, {self.y!r})"

    def __str__(self):
        # Human-readable output
        return f"Coordinates with components {self.x} and {self.y}"

    def __add__(self, other):
        # Defines behavior for the + operator
        if isinstance(other, Coordinates):
            return Coordinates(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        # Defines behavior for the == operator
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __len__(self):
        # Defines behavior for the len() function
        return 2


# Create Coordinates objects
c1 = Coordinates(2, 4)
c2 = Coordinates(3, 5)

# Example usage
print(c1)  # Calls __str__
print(repr(c1))  # Calls __repr__
print(c1 + c2)  # Calls __add__
print(len(c1))  # Calls __len__
print(c1 == Coordinates(2, 4))  # Calls __eq__
