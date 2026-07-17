import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Bestsellers with categories.csv')
print(data.head(5))
print(data.dtypes)
print(data.isnull().sum())


print("\n* User Rating *")

mean_rating = data['User Rating'].mean()
print("Mean Rating of Bestsellers - ", mean_rating)

median_rating = data['User Rating'].median()
print("Median value of Rating -", median_rating)

mode_rating = data['User Rating'].mode()[0]
print("Mode value of Rating -", mode_rating)

print("\n* Reviews *")

mean_reviews = data['Reviews'].mean()
print("Mean Reviews of Bestsellers - ", mean_reviews)

median_reviews = data['Reviews'].median()
print("Median value of Reviews -", median_reviews)

mode_reviews = data['Reviews'].mode()[0]
print("Mode value of Reviews -", mode_reviews)

print("\n* Price *")


mean_Price = data['Price'].mean()
print("Mean Price of Bestsellers - ", mean_Price)

median_Price = data['Price'].median()
print("Median value of Price -", median_Price)

mode_Price = data['Price'].mode()[0]
print("Mode value of Price -", mode_Price)

print("\nThanks")
