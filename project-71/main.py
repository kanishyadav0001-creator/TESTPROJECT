import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

df = pd.read_csv('xydataset (1).csv'), header=None, names=['X', 'y']

X = df['X'].values
y = df['y'].values

m = 0
c = 0
lr = 0.0001
epochs = 1000
n = float(len(X))

for i in range(epochs):
    y_pred = m * X + c
    dm = (-2 / n) * sum(X * (y - y_pred))
    dc = (-2 / n) * sum(y - y_pred)
    m = m - lr * dm
    c = c - lr * dc

y_final_pred = m * X + c

plt.scatter(X, y, color='blue')
plt.plot(X, y_final_pred, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Gradient Descent Linear Regression')
plt.show()

print(f"Slope (m): {m}")
print(f"Intercept (c): {c}")
