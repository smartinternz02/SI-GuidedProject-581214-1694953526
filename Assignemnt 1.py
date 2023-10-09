import pandas as pd
import numpy as np

data = np.random.rand(4, 4)
df = pd.DataFrame(data, columns=['RV1', 'RV2', 'RV3', 'RV4'])

# Task 2: Rename the column names
df.columns =['Random value 1', 'Random value 2', 'Random value 3', 'Random value 4']

# Task 3: Descriptive statistics
descriptive_stats = df.describe()

# Task 4: Check for null values and data types
null_values = df.isnull().sum()
data_types = df.dtypes

# Task 5: Display 'Random value 2' & 'Random value 3' columns using location and index
value_2_location = df.loc[:, 'Random value 2']
value_2_index = df.iloc[:, 1]

value_3_location = df.loc[:, 'Random value 3']
value_3_index = df.iloc[:, 2]

print("Task 1: DataFrame")
print(df)
print("\nTask 2: Renamed Columns")
print(df.columns)
print("\nTask 3: Descriptive Statistics")
print(descriptive_stats)
print("\nTask 4: Null Values")
print(null_values)
print("\nData Types")
print(data_types)
print("\nTask 5: 'Random value 2' & 'Random value 3' Columns")
print("Using Location:")
print("Random value 2:")
print(value_2_location)
print("\nRandom value 3:")
print(value_3_location)
print("\nUsing Index Location:")
print("Random value 2:")
print(value_2_index)
print("\nRandom value 3:")
print(value_3_index)