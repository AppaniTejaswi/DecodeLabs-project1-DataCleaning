import pandas as pd

df = pd.read_csv("Dataset_for_Data_Analytics.csv")

print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())