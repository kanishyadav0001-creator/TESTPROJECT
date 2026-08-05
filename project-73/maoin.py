import numpy as np
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x, y)

p_pred = model.predict(x)
y_pred = model.predict(x)
score = model.score(x, y)
conf_m = classification_report(y, y_pred)

print('x:', x, sep='\n')
print('y:', y, sep='\n', end='\n\n')
print('intercept:', model.intercept_, sep='\n')
print('coef:', model.coef_, end='\n\n')
print('p_pred:', p_pred, sep='\n', end='\n\n')
print('y_pred:', y_pred, sep='\n', end='\n\n')  
