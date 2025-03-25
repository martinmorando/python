'''
    Tuples
    - Built-in data structure; more efficient in memory and time compared to lists.
    - Immutable: can't be changed, can't add or remove elements.
    - Think of them as fixed collections of items.
    - Can hold objects of different data types.
'''

# Define a tuple of 3 items
t = ("apple", "banana", "orange")

# Define a tuple of 1 item. Notice the comma
t2 = ("apple",)

# Access 2nd item
firstItem = t[1]              # "banana"

# Number of elements
length = len(t)               # 3

# Find index of value
index = t.index("orange")     # 2

# Count number of occurences
count = t.count("banana")     # 1

# Min & Max: returns the maximum value. All items must be of the same type
# - Numerical values: highest value
# - String values: sorts alphabetically (closer to "Z", higher)
print(min(t))   # apple
print(max(t))   # orange