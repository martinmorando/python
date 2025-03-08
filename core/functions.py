def sum(x,y):
	return x + y
print(sum(1,2))


# Lambda functions (AKA anonymous functions)
sum_b = lambda x, y: x + y
print(sum_b(1,2)) 

numbers = range(100) 

# map(function, iterable)
# Advantage: memory efficient because it returns an iterator (instead of fully creating it in the memory)
# Example: multiply by 1.5 each element in numbers list
numbers_multiply = map(lambda x: x*1.5, numbers) 
print(list(numbers_multiply)) 

# filter(function, iterable)
# Example: filter numbers list: only saved even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# sorted(iterable, key)
# Example: order members list by second element of each tuple
members = [("A", 10), ("B", 1)]
sorted_members = sorted(members, key=lambda x: x[1])
print(list(sorted_members))

# reduce(function, iterable). Important: import needed
# Example: sum all elements in a list
from functools import reduce
another_list = [1, 2, 3]
z = reduce(lambda x, y: x + y, another_list)
print(z)