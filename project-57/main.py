import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Bestsellers with categories (1).csv') 
print(data.head(5))

print("Null values per column:")
print(data.isnull().sum())


data = data.dropna() 

price_p10 = np.quantile(data['Price'], 0.10)

price_q1 = np.quantile(data['Price'], 0.25)
price_q2 = np.quantile(data['Price'], 0.50)
price_q3 = np.quantile(data['Price'], 0.75)
iqr_price = price_q3 - price_q1


rating_q1 = np.quantile(data['User Rating'], 0.25)
rating_q2 = np.quantile(data['User Rating'], 0.50)
rating_q3 = np.quantile(data['User Rating'], 0.75)
iqr_rating = rating_q3 - rating_q1

print("#92;nUser Rating Quartiles:")
print(f"Q1: {rating_q1} | Q2 (Median): {rating_q2} | Q3: {rating_q3}")
print("Inter-Quartile Range (IQR) for User Rating:", iqr_rating)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=data['Price'])
plt.title('Price Distribution')

plt.subplot(1, 2, 2)
sns.boxplot(y=data['User Rating'])
plt.title('User Rating Distribution')

plt.tight_layout()
plt.show()
