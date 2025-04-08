# Factorial of a number provided by the user
import sys

def factorial(num):
    factorial = 1

    if num < 0:
        print("Does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial *= i
    return factorial

try:
    # input from user
    num = int(input("Enter a number: "))
except ValueError:
    print("Value entered was not a valid number")
    sys.exit(1)
    
print("The factorial of", num ,"is", factorial(num))
