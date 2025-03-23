import pandas
import os

# So that this script can be run from any dir
file_path = os.path.join(os.path.dirname(__file__), "../_data/guest-list.csv")

# Create a DataFrame
df = pandas.read_csv(file_path)

# Change column names
df.columns = ["id", "first_name", "last_name"]

# Print first 5 rows
print( df.head() )