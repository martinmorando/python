'''
    Basic data types
'''

# [DECLARE AND INITIATE VARIABLES]
# - Integer
count = 1

# - Float
price = 3.99

# - String
name = "Clark Kent"

# - Boolean
keepsGoing = True



# [CHECK THE TYPE OF A VARIABLE]
print(type(count))          # Ouput: <class 'int'>
print(type(price))          # Ouput: <class 'float'>
print(type(name))           # Ouput: <class 'str'>
print(type(keepsGoing))     # Ouput: <class 'bool'>



# [DYNAMICALLY TYPED]: the type of a variable is determine at runtime,
# not at compile time. Meaning, the type of a variable can be changed 
# during the execution of the program.
keepsGoing = "F*ck yes"
print(type(keepsGoing))     # Ouput: <class 'str'>