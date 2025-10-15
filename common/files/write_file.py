'''
Demonstrates writing to a file using different methods.
'''

with open("new_file.txt", "w") as f:
    f.write("This is the 1st line.\n")
    f.write("This is the 2nd line.\n")

lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("log.txt", "a") as f:
    f.writelines(lines)
