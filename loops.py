def loops():
    
    # for loop iterates over a sequence (such as a list, tuple, string, or range) or other iterable objects
    
    # iterating through a list
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)

    # iterating through a range
    for i in range(5): # generates numbers from 0 to 4
        print(i)

    # iterating through a string
    my_string = "Hello"
    for char in my_string:
        print(char)
        
    # using continue
    for i in range(10):
        if i % 2 == 0:
            continue # skip even numbers
        print(i)

    # using pass
    for i in range(5):
        if i == 2:
            pass # do nothing when i is 2
        else:
            print(i)

    # loop thru dictionary
    my_dict = {"a": 1, "b": 2, "c": 3}

    # iterate through keys
    for key in my_dict:
        print(key)

    # iterate through values
    for value in my_dict.values():
        print(value)

    # iterate through key-value pairs
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

    # while loop executes a block of code as long as a condition is true
        
    # simple while loop
    count = 0
    while count < 5:
        print(count)
        count += 1

    # while loop with a break statement
    num = 0
    while True:
        print(num)
        num += 1
        if num >= 5:
            break    
        
if __name__ == '__main__':
    loops()
