import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('penguins Data.csv')
df = df.dropna()

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.hist(df['Culmen Length (mm)'], bins=[30, 40, 50, 60, 70], rwidth=0.9, color='blue')
plt.title('Culmen Length')
plt.xlabel('mm')

plt.subplot(2, 2, 2)
plt.hist(df['Culmen Depth (mm)'], bins=[10, 14, 18, 22], rwidth=0.9, color='green')
plt.title('Culmen Depth')
plt.xlabel('mm')

plt.subplot(2, 2, 3)
plt.hist(df['Flipper Length (mm)'], bins=[170, 190, 210, 230], rwidth=0.9, color='red')
plt.title('Flipper Length')
plt.xlabel('mm')

plt.subplot(2, 2, 4)
plt.hist(df['Body Mass (g)'], bins=[2000, 3500, 5000, 6500], rwidth=0.9, color='orange')
plt.title('Body Mass')
plt.xlabel('grams')

plt.tight_layout()
plt.show()