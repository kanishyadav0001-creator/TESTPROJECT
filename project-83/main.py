import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon_data.csv')
print(df.head())

print(df.info())

print(df.describe)

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

df['capture_rate'] = lb.fit_transform(df['capture_rate'])
df['speed'] = lb.fit_transform(df['speed'])

print(df)

df = df.drop(['attack', 'defense','classfication'], axis = 1)

print(df.shape)

y = df.pop('against_water')
X = df

print(X.shape)
print(y.shape)



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

print(X_train)

import keras
from keras.models import Sequential 
from keras.layers import Dense
#from keras.layers import LeakyRelu, PRelu, Elu
#from keras.layers import Dropaut

classifier = Sequential()

classifier.add(Dense(unit = 6, kernel_intializer = 'he_unifrom',activation='relu'))


classifier.add(Dense(unit = 1, kernel_intializer = 'glorot_uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'Adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set

model_history=classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# list all data in history

classifier.summary()

#total params are total number of weights and biases

"""### **5. Model Evaluation**"""

# Predict the Test set results

Y_pred = classifier.predict(X_test)

Y_pred

Y_pred = (Y_pred > 0.5)

Y_pred

# Confusion Matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, Y_pred)

print(cm)

# Calculate the Accuracy

from sklearn.metrics import accuracy_score

score=accuracy_score(Y_pred,y_test)

print(score)

