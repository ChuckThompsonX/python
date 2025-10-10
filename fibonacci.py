# basic example of recursion
# Fibonacci sequence
# series of numbers where each number is the sum of the two preceding ones
# typically starting with 0 and 1

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
      
print(fib(10))  # Output: 55
