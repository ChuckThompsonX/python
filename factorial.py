# Factorial of a number provided by the user

def factorial(num):
    factorial = 1

    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial

try:
    # input from user
    num = int(input("Enter a number: "))
    print("The factorial of", num ,"is", factorial(num))
except ValueError:
    print("Enter a valid number")
