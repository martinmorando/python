'''
Read all data from a CSV file.
If the file does not exist, it will throw out an error.
'''

import csv

file_path = "data/guest-list.csv"

# Read mode
# Newline="" ensures new lines are interpreted correctly
with open(file_path, mode="r", newline="") as file:

	reader = csv.reader(file)

	next(reader) # Skip the first line 

	for row in reader:
		id = row[0]
		name = row[1]
		print(name)