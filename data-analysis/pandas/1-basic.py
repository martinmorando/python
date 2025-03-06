import pandas

# Create a DataFrame
df = pandas.read_csv("data/guest-list.csv")

# Change column names
df.columns = ["id", "first_name", "last_name"]

# Print first 5 rows
print( df.head() )