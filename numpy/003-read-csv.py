'''
    Read CSV
'''

import numpy as np 
 
# Import os module for operating system functionality (file path)
import os
# Construct the file path to the CSV file, allowing the script to be run from any directory
file_path = os.path.join(os.path.dirname(__file__), "../_data/write.csv")


# Create an array from a CSV (treats values as float by default)
arrA = np.genfromtxt(file_path, delimiter=",")
print(arrA)


# Create an array from a CSV, explicitly treating values as integers
arrB = np.genfromtxt(file_path, delimiter=",", dtype=int)
print(arrB)