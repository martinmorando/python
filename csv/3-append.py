'''
If the file does not exist, it creates the file and appends data.
If the file exists, it appends data.
'''

import csv
import os

# So that this script can be run from any dir
file_path = os.path.join(os.path.dirname(__file__), "../_data/write.csv")

data = [range(10)] # Iterable

# Append mode
# Newline="" ensures new lines are interpreted correctly
with open(file_path, mode="a", newline="") as file:

	writer = csv.writer(file)
	writer.writerows(data) # Needs an iterable