'''
    Operations
'''

import numpy as np 

a = np.array([1, 2, 3, 4, 5])

addition = a + 3            # [4 5 6 7 8]
subtraction = a - 3         # [-2 -1 0 1 2]
multiplication = a * 3      # [3 6 9 12 15]
division = a / 2            # [0.5 1. 1.5 2. 2.5]
squared = a ** 2            # [1 4 9 16 25]
squared_root = np.sqrt(a)   # [1. 1.41421356 1.73205081 2. 2.23606798]


b = np.array([6, 7, 8, 9, 10])

print(a + b)                # [7 9 11 13 15]
print(a - b)                # [-5 -5 -5 -5 -5]
print(a * b)                # [6 14 24 36 50]
print(a / b)                # [0.16666667 0.28571429 0.375 0.44444444 0.5]