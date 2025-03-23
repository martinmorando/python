'''
If the CSV file does not exist, it will be created.
If it exists, it will be overwritten.
'''

import csv
import os

# So that this script can be run from any dir
file_path = os.path.join(os.path.dirname(__file__), "../_data/write.csv")

data = [range(10)] # Iterable

# Write mode
# Newline="" ensures new lines are interpreted correctly
with open(file_path, mode="w", newline="") as file:

	writer = csv.writer(file)
	writer.writerows(data) # Needs an iterable