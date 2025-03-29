'''
    1D arrays
'''

# [IMPORT LIBRARY]
import numpy as np



# [CREATE 1D ARRAY]
# - Create an array from a list of integers
a_list = [1, 2, 3, 4, 5, 6]          # Python list
a = np.array(a_list)                 # Numpy array: [1 2 3 4 5 6]

# - Create an array
b = np.array([1, 2, 3, 4, 5])



# [OPERATIONS WITH SCALARS]
addition = b + 3            # [4 5 6 7 8]
subtraction = b - 3         # [-2 -1 0 1 2]
multiplication = b * 3      # [3 6 9 12 15]
division = b / 2            # [0.5 1. 1.5 2. 2.5]
squared = b ** 2            # [1 4 9 16 25]
squared_root = np.sqrt(b)   # [1. 1.41421356 1.73205081 2. 2.23606798]



# [OPERATIONS BETWEEN ARRAYS]
c = np.array([6, 7, 8, 9, 10])
print(b + c)                # [7 9 11 13 15]
print(b - c)                # [-5 -5 -5 -5 -5]
# - Elementwise product
print(b * c)                # [6 14 24 36 50] = [1*6 + 2*7 + 3*8 + 4*9 + 5*10]
# - Matrix product (2 alternatives, same result)
print(b @ c)                # 130
print(b.dot(c))             # 130


# [SELECT AN ITEM]: returns 1 item
# - Select 4th item
print(c[3])                 # 9
# - Select last item
print(c[-1])                # 10



# [SELECT SEVERAL ITEMS]: returns an array
# - Including a[1] but excluding a[3]
print(c[1:3])               # [7 8]

# - Last 2 elements
print(c[-2:])               # [9 10]