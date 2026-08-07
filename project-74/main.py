from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

cancer_data = load_breast_cancer()

x = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
y = cancer_data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

accuracy = model.score(x_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
