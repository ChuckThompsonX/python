def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
      
print(fib(10))  # Output: 55

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
