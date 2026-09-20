import pandas as pd

file_name = "data.csv"

df = pd.read_csv(file_name)

print("Original Dataset:")
print(df)

print("\nDataset Dimensions:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

filtered_df = df[df["Age"] > 18]

print("\nFiltered Data (Age > 18):")
print(filtered_df)

filtered_df.to_csv("filtered_data.csv", index=False)

print("\nFiltered data saved as 'filtered_data.csv'")