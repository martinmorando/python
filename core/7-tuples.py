'''
    Tuples
    - inmutable: can't be changed, can't add or remove elements
    - think of fixed collections of items
'''

t = ("apple", "banana", "orange")

# Access 2nd item
firstItem = t[1]              # "banana"

# Number of elements
length = len(t)               # 3

# Find index of value
index = t.index("orange")     # 2

# Count number of occurences
count = t.count("banana")     # 1