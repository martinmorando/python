'''
    Files
'''

# Read all content from a file
with open("_data/lorem-ipsum.txt") as file_object:
    content = file_object.read()

# Print it
print(content)



# Read content line by line, and print them. Same result as previous example
with open("_data/lorem-ipsum.txt") as file_object:
    for line in file_object.readlines():
        print(line)



# Read only the first 3 lines, and print the 3rd one
with open("_data/lorem-ipsum.txt") as file_object:
    first_line = file_object.readline()
    second_line = file_object.readline()
    third_line = file_object.readline()
    print(third_line)