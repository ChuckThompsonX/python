'''
*args and **kwargs are special syntaxes that allow functions to accept a variable number
of arguments. They provide flexibility when defining functions where the exact number 
of inputs might not be known beforehand.
'''

def my_func(*args):
    for arg in args:
        print(arg)

my_func(1, 2, "test", True)


def my_other_func(**kwargs):
    for key in kwargs.keys():
        print(f"{key} -> {kwargs[key]}")
    #for key, value in kwargs.items():
    #    print(f"{key}: {value}")

my_other_func(name="Alice", age=30, city="New York")


def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(sum(*numbers))  # Unpacks the list into positional arguments


def hello(greeting, name):
    print(f"{greeting}, {name}!")

details = {"greeting": "Hi", "name": "Alice"}
print(hello(**details))  # Unpacks the dictionary into keyword arguments
