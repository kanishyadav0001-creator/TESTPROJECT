import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('penguins.csv')
df = df.dropna()

plt.figure(figsize=(8, 5))
plt.scatter(df['Culmen Length (mm)'], df['Body Mass (g)'], color='blue')
plt.title('Culmen Length vs Body Mass')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['Culmen Depth (mm)'], df['Body Mass (g)'], color='green')
plt.title('Culmen Depth vs Body Mass')
plt.xlabel('Culmen Depth (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

sns.pairplot(df)
plt.show()

df_sorted = df.sort_values(by='Culmen Length (mm)')

plt.figure(figsize=(8, 5))
plt.fill_between(df_sorted['Culmen Length (mm)'], df_sorted['Body Mass (g)'], color='purple', alpha=0.4)
plt.title('Culmen Length vs Body Mass (Area Graph)')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()