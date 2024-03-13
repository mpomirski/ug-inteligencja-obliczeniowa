from matplotlib.pylab import f
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from typing import Any, cast, List
from graphviz import Digraph
import math

SHOW = True

def calculate_stroke_weight(weight: float) -> float:
    return math.log(abs(weight) + 1)+0.25
    

def draw_dot(model: MLPClassifier, name: str, labels: List[str]) -> Digraph:
    dot = Digraph(comment='The Round Table')
    dot.node('00', 'Sepal Length', group='inputs')
    dot.node('01', 'Sepal Width', group='inputs')
    dot.node('02', 'Petal Length', group='inputs')
    dot.node('03', 'Petal Width', group='inputs')
    dot.attr(rankdir='LR', size='16!,10!', nodesep='2', ranksep='2', splines='false')

    for layer_no, layer in enumerate(model.coefs_):
        for i, neuron in enumerate(layer.T):
            if layer_no == len(model.coefs_) - 1:
                dot.node(f'{str(layer_no+1) + str(i)}', f'{labels[i]}')
            else:
                dot.node(f'{str(layer_no+1) + str(i)}', f'Neuron {layer_no+1}{i}')
            for j, weight in enumerate(neuron):
                stroke_weight = calculate_stroke_weight(weight)
                dot.edge(f'{str(layer_no) + str(j)}', f'{str(layer_no + 1) + str(i)}', xlabel=f'{weight:.2f}', fontsize='10', fontcolor='blue', penwidth=str(stroke_weight))

    return dot

iris: Any = cast(Any, datasets.load_iris())

# Scaling data
scaler = StandardScaler()
scaler.fit_transform(iris.data)

# Splitting data
train_set, test_set, train_labels, test_labels = train_test_split(iris.data, iris.target, test_size=0.3)
print(f'Train set size: {len(train_set)}')
print(f'Test set size: {len(test_set)}')


# Training the first model (input, 1 hidden layer with 2 neurons, output)
model1 = MLPClassifier(hidden_layer_sizes=(2), max_iter=3000, early_stopping=True, n_iter_no_change=100)
fitted = model1.fit(train_set, train_labels)
print('Labels:')
print(iris.target_names)
print("Weights:")
print(*model1.coefs_, sep='\n\n')
print("Biases:")
print(*model1.intercepts_, sep='\n\n')
print(fitted.coefs_)
graph = draw_dot(model1, 'model1', iris.target_names)
graph.render('model1', format='png', cleanup=True,)


# Testing the first model
predictions = model1.predict(test_set)
model1.score(test_set, test_labels)
print(f'Accuracy of the first model: {accuracy_score(test_labels, predictions)}')


# Training the second model (input, 1 hidden layers with 3 neurons, output)
model2 = MLPClassifier(hidden_layer_sizes=(3), max_iter=3000)
model2.fit(train_set, train_labels)

graph = draw_dot(model2, 'model2', iris.target_names)
graph.render('model2', format='png', cleanup=True,)

# Testing the second model
predictions2 = model2.predict(test_set)
print(f'Accuracy of the second model: {accuracy_score(test_labels, predictions2)}')





# Training the third model (input, 2 hidden layers with 3 neurons, output)
model3 = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=3000)
model3.fit(train_set, train_labels)

graph = draw_dot(model3, 'model3', iris.target_names)
graph.render('model3', format='png', cleanup=True,)

# Testing the third model
predictions3 = model3.predict(test_set)
print(f'Accuracy of the third model: {accuracy_score(test_labels, predictions3)}')



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




