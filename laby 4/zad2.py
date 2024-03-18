from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from typing import Any, cast
from NNGraph import NNGraph

SHOW = False
GLOBAL_MAX_ITER = 100
iris: Any = cast(Any, datasets.load_iris())

# Scaling data
scaler = StandardScaler()
scaler.fit_transform(iris.data)

# Splitting data
train_set, test_set, train_labels, test_labels = train_test_split(iris.data, iris.target, test_size=0.3)
print(f'Train set size: {len(train_set)}')
print(f'Test set size: {len(test_set)}')


# Training the first model (input, 1 hidden layer with 2 neurons, output)
model1 = MLPClassifier(hidden_layer_sizes=(2), max_iter=GLOBAL_MAX_ITER, n_iter_no_change=GLOBAL_MAX_ITER, learning_rate='adaptive')
model1.fit(train_set, train_labels)
graph1 = NNGraph(model1, 'model1', iris.target_names, iris.feature_names)
graph1.draw_graph()


# Testing the first model
predictions = model1.predict(test_set)
model1.score(test_set, test_labels)
print(f'Accuracy of the first model: {accuracy_score(test_labels, predictions):.2f}')


# Training the second model (input, 1 hidden layers with 3 neurons, output)
model2 = MLPClassifier(hidden_layer_sizes=(3), max_iter=GLOBAL_MAX_ITER, n_iter_no_change=GLOBAL_MAX_ITER, learning_rate='adaptive')
model2.fit(train_set, train_labels)

graph2 = NNGraph(model2, 'model2', iris.target_names, iris.feature_names)
graph2.draw_graph()

# Testing the second model
predictions2 = model2.predict(test_set)
print(f'Accuracy of the second model: {accuracy_score(test_labels, predictions2):.2f}')


# Training the third model (input, 2 hidden layers with 3 neurons, output)
model3 = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=GLOBAL_MAX_ITER, n_iter_no_change=GLOBAL_MAX_ITER, learning_rate='adaptive')
model3.fit(train_set, train_labels)

graph3 = NNGraph(model3, 'model3', iris.target_names, iris.feature_names)
graph3.draw_graph()

# Testing the third model
predictions3 = model3.predict(test_set)
print(f'Accuracy of the third model: {accuracy_score(test_labels, predictions3):.2f}')



if (SHOW):
    plt.figure(figsize=(10, 5))
    plt.plot(model1.loss_curve_)
    plt.plot(model2.loss_curve_)
    plt.plot(model3.loss_curve_)
    plt.title('Loss curve')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend(['1 hidden layer with 2 neurons', '1 hidden layer with 3 neurons', '2 hidden layers with 3 neurons'])
    plt.show()




