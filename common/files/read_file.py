'''
Demonstrates reading from a file using different methods.
'''

with open("my_file.txt", "r") as f:
    data = f.read()
    print(data)

    f.seek(0)  # Reset file pointer to beginning
    first_line = f.readline()
    print(first_line)

    f.seek(0)
    lines = f.readlines()
    print(lines)
