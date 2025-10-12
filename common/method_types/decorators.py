'''
Decorators are a way to modify or enhance the behavior of functions or methods without 
directly altering their source code. They can wrap a function, allowing you to add 
functionality before, after, or even around the original function's execution.

Common Use Cases:
Logging: Recording function calls, arguments, and return values.
Timing/Performance Measurement: Calculating the execution time of functions.
Authentication/Authorization: Checking user permissions before executing a function.
Caching: Storing the results of expensive function calls to avoid re-computation.
Input Validation: Ensuring function arguments meet specific criteria.
'''

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Bob")