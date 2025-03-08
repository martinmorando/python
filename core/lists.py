empty = []
strings = ["A", "B", "C"]
numbers = [1, 2, 3]
mixed = ["A", 1, 0.99, True]

# Access first item
first_item = strings[0]

# Add item
strings.append("D")

# Remove item (first match only)
strings.remove("D") 

# Modify list
strings[0] = "AA"
print(strings)

# Add lists
mixed_2 = strings + numbers
mixed_3 = strings + numbers + [2] # Add list that contains one item
print(mixed_2)

# Zip
print(list(zip(numbers, strings)))