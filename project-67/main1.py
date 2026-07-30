import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

matches = pd.read_csv("Matches.csv")
deliveries = pd.read_csv("Deliveries.csv")

print("--- Processing Dataset 1: Matches ---")

print("Null values count in Matches:")
print(matches.isnull().sum())

plt.figure(figsize=(10, 5))
sns.heatmap(matches.isnull(), cmap="spring", cbar=False)
plt.title("Null Values Heatmap - Matches")
plt.show()

matches.dropna(inplace=True)  

print("\nColumns in Matches:", matches.columns)


print("\n--- Processing Dataset 2: Deliveries ---")

print("Null values count in Deliveries:")
print(deliveries.isnull().sum())

plt.figure(figsize=(10, 5))
sns.heatmap(deliveries.isnull(), cmap="spring", cbar=False)
plt.title("Null Values Heatmap - Deliveries")
plt.show()

deliveries.dropna(inplace=True)

print("\nColumns in Deliveries:", deliveries.columns)


print("\n--- Checking for Common Link & Merging ---")

common_columns = set(matches.columns).intersection(set(deliveries.columns))
print("Identified common column names:", common_columns)

if 'id' in matches.columns and 'match_id' in deliveries.columns:
    merged_data = pd.merge(deliveries, matches, left_on='match_id', right_on='id')
    print("Merged successfully using 'match_id' and 'id' keys!")
    print(merged_data.head())

elif len(common_columns) > 0:
    link_col = list(common_columns)[0]
    merged_data = pd.merge(deliveries, matches, on=link_col)
    print(f"Merged successfully on exact column name: {link_col}")
    print(merged_data.head())

else:
    print("No common link found between columns. Merging ignored.")
