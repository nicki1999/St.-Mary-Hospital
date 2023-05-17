import pandas as pd
from tabulate import tabulate

# Example DataFrame with 9 rows and 12 columns
data = [[f"Row {i}", f"Col {j}"] for i in range(1, 10) for j in range(1, 13)]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Get column names
headers = ["Column {}".format(i) for i in range(1, 13)]

# Convert DataFrame to a list of lists
data = df.values.tolist()

# Creating a table
table = tabulate(data, headers=headers, tablefmt="grid")

# Displaying the table
print(table)
