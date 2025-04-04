'''
    Dictionaries
    - Unordered set of key:value pairs
'''

# Create a dictionary
empty = {}
chairs = {"kitchen": 4, "bedroom": 2}

# Add a key:value pair
chairs["garage"] = 0        # {'kitchen': 4, 'bedroom': 2, 'garage': 0}

# Overwrite value
chairs["kitchen"] = 2       # {'kitchen': 2, 'bedroom': 2, 'garage': 0}

# Iterate over key:value pairs
for key, value in chairs.items(): # "key" and "value" are placeholders
    print(key, value)

# Iterate only over the values
for value in chairs.values():
    print(value)