'''
    Basics
'''

# Import NumPy
import numpy as np

# Import os module for operating system functionality (file path)
import os
# Construct the file path to the CSV file, allowing the script to be run from any directory
file_path = os.path.join(os.path.dirname(__file__), "../_data/write.csv")


# [CREATE]
# Create an array from a list of integers
a = [1, 2, 3, 4, 5, 6]
arrA = np.array(a)
print(arrA)


# Create an array from a CSV (treats values as float by default)
arrB = np.genfromtxt(file_path, delimiter=",")
print(arrB)


# Create an array from a CSV, explicitly treating values as integers
arrC = np.genfromtxt(file_path, delimiter=",", dtype=int)
print(arrC)