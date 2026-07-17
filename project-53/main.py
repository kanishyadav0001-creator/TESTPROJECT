import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('penguins.csv')

print(df.isnull().sum())
print("\n")

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title("Visualizing Missing Values")
plt.show()

num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_cols = df.select_dtypes(exclude=np.number).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

print(df.isnull().sum())
print("\n")

sns.pairplot(df)
plt.suptitle("Pair Plot of Numerical Features", y=1.02)
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='terrain', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

num_data = df.select_dtypes(include=np.number)
num_data.plot(kind='box', subplots=True, layout=(2, 3), figsize=(15, 10))
plt.suptitle("Boxplots for Numerical Features")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sex', palette='spring')
plt.title("Count Plot of Gender/Sex")
plt.show()



