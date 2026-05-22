import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# loading dataset
dataset = pd.read_csv("iris.csv")

# input data
X = dataset.iloc[:, [0,1,2,3]].values

# output data
y = dataset.iloc[:, -1].values

# splitting dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# creating model
classifier = KNeighborsClassifier(
    n_neighbors=5,
    metric='minkowski',
    p=2
)

# training model
classifier.fit(X_train, y_train)

# prediction
y_pred = classifier.predict(X_test)

# results
print("My first AI classification project")

print("\nPredictions:")
print(y_pred)

print("\nActual Values:")
print(y_test)

# confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# accuracy
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))