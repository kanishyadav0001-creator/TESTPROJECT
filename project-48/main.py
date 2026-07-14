#We Handle the Null values in data cleaning
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("country_vaccinations.csv")

print(df.head(10))

print(df.isnull().any())

subset = df.iloc[:100, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap='viridis')
plt.show()

print(df.head(10))

df=df.dropna(how="all")

df=df.bfill()

numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].interpolate()
df_dropped = df.dropna()
print(df_dropped) 