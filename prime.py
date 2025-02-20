# Check if a number is prime or not
import math

def is_prime(num):
    if num <= 1:
        # can not be negative, 0 or 1
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        # check factors
        if num % i == 0:
            return False
    return True

try:
    num = int(input("Enter a number: "))
    print(f"{num} is " + ("" if is_prime(num) else "not ") + "prime")
except ValueError:
    print("Enter a valid number")
