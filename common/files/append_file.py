'''
Demonstrates appending content to a file.
'''

# Append new content to file
with open("my_file.txt", "a") as f:
    f.write("This is an appended line.\n")
    f.write("Another appended line.\n")

# Read and print the entire content of the file
with open("my_file.txt", "r") as f:
    data = f.read()
    print(data)
