'''
    List comprehensions
'''

# Create a list of integers from [0, 5)
numbers_list = [x for x in range(5)]
print(numbers_list)                     # [0, 1, 2, 3, 4]


# Create a list of even integers from [0, 9)
a = [n for n in range(9) if n % 2 == 0]
print(a)                                # [0, 2, 4, 6, 8]


# Calculate y_values for a linear function (y = m * x + b)
# where m = 3 and b = 5, for x in {0, 1, 2, 3}.
y_values = [3*x + 5 for x in range(4)]
print(y_values)                         # [5, 8, 11, 14]