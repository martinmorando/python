'''
    Lists
'''
# Create lists
empty = []
strings = ["A", "B", "C"]
numbers = [1, 2, 3]
mixed = ["A", 1, 0.99, True]

# Create a list with integers from 0 to 99
# list() is necessary because range() returns a range object
usingRange = list(range(100)) # [0, 1, 2, 3,..., 98, 99]

# Access first item of "strings" list
first_item = strings[0]

# Add item to "strings" list
strings.append("D")           # ["A", "B", "C", "D"]

# Remove item (first match only)
strings.remove("B")           # ["A", "C", "D"]

# Remove last item
strings.pop()                 # ["A", "C"]

# Modify 1st item from "strings" list
strings[0] = "AA"             # ["AA", "C"]

# Add lists
mixed_2 = strings + numbers   # ["AA", "C", 1, 2, 3]

# Add a list that contains one item
mixed_3 = strings + [4]       # ["AA", "C", 4]
# This is wrong: mixed_4 = strings + 4

# Zip
list(zip(numbers, strings))