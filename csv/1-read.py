'''
Read all data from a CSV file.
If the file does not exist, it will throw out an error.
'''

import csv
import os

# So that this script can be run from any dir
file_path = os.path.join(os.path.dirname(__file__), "../_data/guest-list.csv")

# Read mode
# Newline="" ensures new lines are interpreted correctly
with open(file_path, mode="r", newline="") as file:

	reader = csv.reader(file)

	next(reader) # Skip the first line 

	for row in reader:
		id = row[0]
		name = row[1]
		print(name)