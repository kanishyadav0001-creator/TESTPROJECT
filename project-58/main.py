import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Bestsellers with categories (1).csv')

print(data.isnull().sum())

data = data.dropna()

for col in data.select_dtypes(include=['object']).columns:
    print(data[col].value_counts())

min_rating = data['User Rating'].min()
max_rating = data['User Rating'].max()
mid_rating = (min_rating + max_rating) / 2
data['Rating_Class'] = pd.cut(data['User Rating'], bins=[min_rating - 0.1, mid_rating, max_rating], labels=['good', 'excellent'])

numerical_features = data.select_dtypes(include=[np.number]).columns
for col in numerical_features:
    print(f"{col} Skewness: {data[col].skew()}")

print(pd.crosstab(data['Genre'], data['Rating_Class']))

print(data[['User Rating', 'Price']].corr())
