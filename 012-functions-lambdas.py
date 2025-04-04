'''
    Lambdas
    - AKA "anonymous functions" because they don't have a name.
    - As they can have only 1 expression and 0 statements, they are
      used for simple operations.
'''

# Simple lambda
sum_b = lambda x, y: x + y
print(sum_b(1,2))



# [USAGE WITH OTHER FUNCTIONS]
# - A) Map(function, iterable1, iterable2, ...)
# Apply a function to EVERY item in an iterable
# Advantage: memory efficient because it returns an iterator (instead of fully creating it in the memory)
# Example: multiply by 1.5 each element in numbers list
numbers = range(100) 
numbers_multiply = map(lambda x: x*1.5, numbers)
print(list(numbers_multiply)) 


# - B) Filter(function, iterable)
# Example: filter numbers list (only save even numbers)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))


# - C) Sorted(iterable, key)
# Example: order members list (by second element of each tuple)
members = [("A", 10), ("B", 1)]
sorted_members = sorted(members, key=lambda x: x[1])
print(list(sorted_members))


# - D) Reduce(function, iterable). Important: import required
# Example: sum all elements in a list
from functools import reduce
another_list = [1, 2, 3]
z = reduce(lambda x, y: x + y, another_list)
print(z)