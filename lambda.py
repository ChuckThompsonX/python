from pprint import pprint

def test_lambda():
    add = lambda x, y: x * y
    val = add(14, 11)
    print(val)
    
def hello(name: str) -> str:
    return f"Hi {name}!"

if __name__ == '__main__':
    test_lambda()
    data = hello("Chuck")
    print(data)

'''
lambda keyword is used to create anonymous functions, which can take 
any number of arguments but can only have one expression. 
They are often used for short, simple operations that can be defined inline.

The -> syntax is used for return type annotations, not arrow functions.
It is used to specify the expected return type of a function. 
'''
