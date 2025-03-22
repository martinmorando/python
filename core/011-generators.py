'''
    Generators
    - Special type of iterable that allows one to iterate in a memory-efficient way
'''

# Import required built-in library
import itertools

# Create a list of tuples
fruits = [("apple", 10), ("banana", 6), ("orange", 25)]

# Create a generator object from the list "fruits"
fruits_iterator = iter(fruits)

# Retrive next value from the generator object
print( next(fruits_iterator) )  # ('apple', 10)
print( next(fruits_iterator) )  # ('banana', 6)
print( next(fruits_iterator) )  # ('orange', 25)

# This is wrong because there are no more values in the generator object
# print( next(fruits_iterator) )  # Raises StopIteration