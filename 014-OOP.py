'''
    OOP
    - "Dunder" methods: they have 2 underscores on either side 
'''

# PEP 8 Style: capitalize names of classes 
class Calculator:

    author = "Martin"   # This is a class variable

    # Constructor
    def __init__(self): # This is also a dunder method
        print("START")

    # String representation
    def __repr__(self):
        return "I'm a calculator"

    # Method
    def addition(self, n1, n2):
        return n1 + n2


# Initiate object
calculate = Calculator()

# Print attribute
print(calculate.author)                      # Output: Martin

# Call method
result = calculate.addition(3, 4)  
print(result)                                # Output: 7

# Print object
print(calculate)                             # Output: I'm a calculator



# [BUILT-IN FUNCTIONS]
# - hasttr()
print(hasattr(calculate, "author"))          # Output: True
print(hasattr(calculate, "year"))            # Output: False

# - getattr()
print(getattr(calculate, "author"))          # Output: Martin
print(getattr(calculate, "year", "default")) # Output: default