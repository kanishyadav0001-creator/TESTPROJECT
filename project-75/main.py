from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

X = iris.data
Y = iris.target

logreg = LogisticRegression(max_iter=10000)
logreg.fit(X, Y)

y_predicted = logreg.predict(X)

accuracy = logreg.score(X, Y)
print(f"Accuracy: {accuracy * 100:.2f}%")
