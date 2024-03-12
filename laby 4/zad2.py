from sklearn import datasets
from sklearn.model_selection import train_test_split, LearningCurveDisplay
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# Scaling data
scaler = StandardScaler()
scaler.fit_transform(iris.data)

# Splitting data
train_set, test_set, train_labels, test_labels = train_test_split(iris.data, iris.target, test_size=0.3)
print(f'Train set size: {len(train_set)}')
print(f'Test set size: {len(test_set)}')


# Training the first model (input, 1 hidden layer with 2 neurons, output)
model = MLPClassifier(hidden_layer_sizes=(2), max_iter=3000)
model.fit(train_set, train_labels)

# Testing the first model
predictions = model.predict(test_set)
model.score(test_set, test_labels)
print(f'Accuracy of the first model: {accuracy_score(test_labels, predictions)}')
plt.figure(figsize=(10, 5))
plt.plot(model.loss_curve_)
plt.title('Loss curve')
plt.xlabel('Epochs')
plt.ylabel('Loss')

# Training the second model (input, 1 hidden layers with 3 neurons, output)
model = MLPClassifier(hidden_layer_sizes=(3), max_iter=3000)
model.fit(train_set, train_labels)

# Testing the second model
predictions = model.predict(test_set)
print(f'Accuracy of the second model: {accuracy_score(test_labels, predictions)}')

plt.plot(model.loss_curve_)


# Training the third model (input, 2 hidden layers with 3 neurons, output)
model = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=3000)
model.fit(train_set, train_labels)

# Testing the third model
predictions = model.predict(test_set)
print(f'Accuracy of the third model: {accuracy_score(test_labels, predictions)}')
plt.plot(model.loss_curve_)
plt.legend(['1 hidden layer with 2 neurons', '1 hidden layer with 3 neurons', '2 hidden layers with 3 neurons'])
plt.show()




