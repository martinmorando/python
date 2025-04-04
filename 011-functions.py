'''
    Functions
'''

# [BASIC FUNCTION]: with 2 parameters
def addition(x,y):
	return x + y

# Print the call to the function
print(addition(1,2))            # Output: 3



# [FUNCTION WITH A DEFAULT PARAMETER & 2 MULTIPLE RETURN VALUES]
def sumAndProduct(x, y=9):
    return x + y, x * y

print(sumAndProduct(2, 3))      # Output: (5, 6)
print(sumAndProduct(2))         # Output: (11, 18)

# Save the multiple returned values in variables
addition, product = sumAndProduct(5, 6)
print(addition)                 # Output: 11
print(product)                  # Output: 30



# [KEYWORD ARGUMENTS]
def colors(a, b):
    print("a:", a, "b:", b)
    return "KEEP GOING"

colors(1, 2)                    # Output: a: 1 b: 2
colors(2, 1)                    # Output: a: 2 b: 1

# Keyword arguments: arguments are passed using their names
colors(b=2, a=1)                # Output: a: 1 b: 2



# [SCOPE: GLOBAL VS LOCAL]
testVar = "global"              # Global variable
def checkScope():
    testVar = "local"           # Local variable, can't be used outside function
    print(testVar)

print(testVar)                  # Output: global
checkScope()                    # Output: local