# Classifying Iris Species

from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("Keys of Iris_dataset: \n{}".format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193]+"\n...")

print("Target names: {}".format(iris_dataset['target_names']))
print("Feature names: {}".format(iris_dataset['feature_names']))

print("Type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))

print("First five columns of data:\n{}".format(iris_dataset["data"][:5]))

print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))

# 0 - setosa 1 - versicolor 2 - virginica
print("Target:\n{}".format(iris_dataset["target"])) 

# random shuffle then assign [ 75% train | 25% test ]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"],iris_dataset["target"], random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

# pair plot to show all possiple pairs of features
import pandas as pd
import matplotlib.pyplot as plt
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
grr = pd.plotting.scatter_matrix(iris_dataframe, c = y_train, figsize=(15,15), marker = 'o', hist_kwds={'bins':20}, s = 60, alpha = .8)
#plt.show()

# K-nearest Neighbor
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)


# Prediction
import numpy as np
X_new = np.array([[5,2.9,1,0.2]])
print("X_new shape: {}".format(X_new.shape))

prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(iris_dataset["target_names"][prediction]))

y_pred = knn.predict(X_test)
print("Test set predictions:\n{}".format(y_pred))
print("Test set score: {:.2f}".format(np.mean(y_pred==y_test)))
print("Test set score: {:.2f}".format(knn.score(X_test,y_test)))

# we can trust it 97% of the time

