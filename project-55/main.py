import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv('Bestsellers with categories.csv')
print(data.head(5))
print(data.info())
print(data.isnull().sum())

print("* User Rating *")

var_rating = np.var(data['User Rating'])
print("Variance of User Rating -", var_rating)

std_rating = np.std(data['User Rating'])
print("Standard Deviation of User Rating -", std_rating)

print("* Price *")

var_price = np.var(data['Price'])
print("Variance of Price -", var_price)

std_price = np.std(data['Price'])
print("Standard Deviation of Price -", var_price)

print("* Histogram *")

plt.hist(data['User Rating'])
plt.hist(data['User Rating'], color='purple', edgecolor='black', bins=np.arange(1,7,0.5))
plt.show()



