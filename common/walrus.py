"""
Assignment expression operator allows you to assign a value to a variable within an expression. 
Syntax := resembles the eyes and tusks of a walrus.
"""

# Without walrus operator
inputs = []
while True:
    entry = input("Enter data (type 'quit' to stop): ")
    if entry == "quit":
        break
    inputs.append(entry)
print(inputs)

# With walrus operator
inputs = []
while (entry := input("Enter data (type 'quit' to stop): ")) != "quit":
    inputs.append(entry)
print(inputs)


def expensive_func(x):
    print(f"Calculating for {x}...")
    return x * x

data = [1, 2, 3]

# Without walrus operator
results = [expensive_func(item) for item in data if expensive_func(item) > 3]
print(results)

# With walrus operator
results = [y for item in data if (y := expensive_func(item)) > 3]
print(results)
