'''
Simple python program that computes the amount of time a function takes to execute.
'''
import time
from functools import wraps

# We pass in the sample_func by way of the time_function decorator
def time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Start time '{start_time}'...")
        
        # Call the actual function
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"End time '{end_time}'...")
        
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds")
        
        return result
    return wrapper

@time_func
def sample_func(n):
    print(f"Calculating the sum of numbers up to {n}...")
    total = 0
    for i in range(n):
        total += i
    print(f"End calculation...")
    return total

# Example usage
result = sample_func(10000000)
print(f"Result: {result}")
# Output will show the time taken to execute sample_func
