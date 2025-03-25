'''
    OOP
    - "Dunder" methods: they have 2 underscores on either side 
'''

# PEP 8 Style: capitalize names of classes 
class Calculator:

    # Constructor
    def __init__(self): # This is also a dunder method
        print("START")

    # Method
    def addition(self, n1, n2):
        return n1 + n2


calculate = Calculator()
result = calculate.addition(3, 4)  
print(result)                # Output: 7