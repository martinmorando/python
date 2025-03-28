'''
    2D arrays
    - They have 2 axes:
        - Axis 0: values that are in the same column ("same indexical position")
        - Axis 1: values that are in the same row ("share an array")
'''

import numpy as np 

# [DEFINE]
# Define a 2 dimensional-array
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# This WON'T WORK. Notice the []
# a = np.array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

# This also works
b = np.array([[1, 2, 3, 4, 5],   # First row
              [6, 7, 8, 9, 10]]) # Second row



# [SELECT ELEMENT]
# - [ROW, COLUMN]
# - Example: 2nd row (index 1), 4th column (index 3)
print(b[1, 3])                   # Output: 9