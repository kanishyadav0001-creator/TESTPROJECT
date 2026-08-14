import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('pokemon_data.csv')
print(df.head())

print(df.info())

print(df.describe())

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

df['capture_rate'] = lb.fit_transform(df['capture_rate'])
df['speed'] = lb.fit_transform(df['speed'])

print(df)

print(df.info())

df = df.drop(['attack','classfication','defense'], axis = 1)

print(df.shape)

y = df.pop('against_water')
X = df

print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)