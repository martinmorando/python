'''
If the file does not exist, it creates the file and appends data.
If the file exists, it appends data.
'''

import csv

file_path = "data/write.csv"

data = [range(10)] # Iterable

# Append mode
# Newline="" ensures new lines are interpreted correctly
with open(file_path, mode="a", newline="") as file:

	writer = csv.writer(file)
	writer.writerows(data) # Needs an iterable