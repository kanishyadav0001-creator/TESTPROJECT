import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('StudentsPerformance.csv')

print(data.isnull().sum())

data = data.dropna() 

print(data.describe())

categorical_features = data.select_dtypes(include=['object', 'category']).columns
for col in categorical_features:
    plt.figure()
    sns.countplot(x=col, data=data)
    plt.xticks(rotation=45)
    plt.show()

fig, axes = plt.subplots(1, 2, figsize=(14, 7))
data['race/ethnicity'].value_counts().plot.pie(ax=axes[0], autopct='%1.1f%%')
data['parental level of education'].value_counts().plot.pie(ax=axes[1], autopct='%1.1f%%')
plt.show()

print(pd.crosstab(data['race/ethnicity'], data['gender']))
plt.figure()
sns.countplot(x='race/ethnicity', hue='gender', data=data)
plt.show()

print(pd.crosstab(data['lunch'], data['gender']))
plt.figure()
sns.countplot(x='lunch', hue='gender', data=data)
plt.show()

numerical_features = data.select_dtypes(include=[np.number]).columns
for col in numerical_features:
    print(f"Skewness of {col}: {data[col].skew()}")
    plt.figure()
    sns.histplot(data[col], kde=True)
    plt.show()

plt.figure() 
sns.boxplot(x='gender', y='math score', data=data)
plt.show()

plt.figure()
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()
