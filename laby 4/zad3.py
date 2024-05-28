from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from typing import Any, cast
from NNGraph import NNGraph
import pandas as pd
import numpy as np

# Prepare datta
df = pd.read_csv('diabetes 1.csv')
df = df.dropna()
df = df.drop_duplicates()

# Scaling data
StandardScaler().fit_transform(df.drop('class', axis=1))

train_set, test_set, train_labels, test_labels = train_test_split(df.drop('class', axis=1), df['class'], test_size=0.3)

# Training the model
model1 = MLPClassifier(hidden_layer_sizes=(6, 3), max_iter=500, n_iter_no_change=500, learning_rate='adaptive',)
model1.fit(train_set, train_labels)

print('Results with hidden layer sizes (6, 3), activation function: relu')
model1.score(test_set, test_labels)
predictions = model1.predict(test_set)
print(f'Accuracy of the model: {accuracy_score(test_labels, predictions):.2f}')
# Confusion matrix
# [[TN, FP]
#  [FN, TP]]
matrix = confusion_matrix(test_labels, predictions)
print(matrix)



model2 = MLPClassifier(hidden_layer_sizes=(6, 6), max_iter=500, n_iter_no_change=500, learning_rate='adaptive',)
model2.fit(train_set, train_labels)

print('Results with hidden layer sizes (6, 6), activation function: relu')
model2.score(test_set, test_labels)
predictions = model2.predict(test_set)
print(f'Accuracy of the model: {accuracy_score(test_labels, predictions):.2f}')
# Confusion matrix
# [[TN, FP]
#  [FN, TP]]
matrix = confusion_matrix(test_labels, predictions)
print(matrix)



model3 = MLPClassifier(hidden_layer_sizes=(6, 3), max_iter=500, n_iter_no_change=500, learning_rate='adaptive', activation='tanh')
model3.fit(train_set, train_labels)

print('Results with hidden layer sizes (6, 3), activation function: tanh')
model3.score(test_set, test_labels)
predictions = model3.predict(test_set)
print(f'Accuracy of the model: {accuracy_score(test_labels, predictions):.2f}')
# Confusion matrix
# [[TN, FP]
#  [FN, TP]]
matrix = confusion_matrix(test_labels, predictions)
print(matrix)


model4 = MLPClassifier(hidden_layer_sizes=(6, 6), max_iter=500, n_iter_no_change=500, learning_rate='adaptive', activation='tanh')
model4.fit(train_set, train_labels)

print('Results with hidden layer sizes (6, 6), activation function: tanh')
model4.score(test_set, test_labels)
predictions = model4.predict(test_set)
print(f'Accuracy of the model: {accuracy_score(test_labels, predictions):.2f}')
# Confusion matrix
# [[TN, FP]
#  [FN, TP]]
matrix = confusion_matrix(test_labels, predictions)
print(matrix)

model5 = MLPClassifier(hidden_layer_sizes=(30, 15), max_iter=500, n_iter_no_change=500, learning_rate='adaptive', activation='relu')
model5.fit(train_set, train_labels)
print('Results with hidden layer sizes (30, 15), activation function: relu')
model5.score(test_set, test_labels)
predictions = model5.predict(test_set)
print(f'Accuracy of the model: {accuracy_score(test_labels, predictions):.2f}')
# Confusion matrix
# [[TN, FP]
#  [FN, TP]]
matrix = confusion_matrix(test_labels, predictions)
print(matrix)

NNGraph(model5, 'model-diabetes', ['0', '1'], list(df.columns[:-1])).draw_graph()

print("Wszystkie modele osiągnęły podobne rezultaty, z wyjątkiem modelu ze znacząco zwiększoną warstwą ukrytą (30, 15), który mimo tego osiągnął tylko nieco lepszy wynik.")
print("We wszystkich modelach więcej jest wskazań False Negative, które oznaczają zaklasyfikowanie osoby jako zdrowej, mimo że faktycznie jest chora.")
print("Błędy FN są gorsze niż FP, ponieważ osoba chora, która zostanie zaklasyfikowana jako zdrowa \n\
      może nie otrzymać odpowiedniej pomocy medycznej.")
print("Można również zauważyć tendencję do klasyfikowania osób jako zdrowych, co może wynikać z niewystarczającej ilości danych, \n\
      zbyt małej ilości neuronów w warstwie ukrytej lub za krótkiego treningu.")





# Plotting loss curves
plt.figure(figsize=(10, 5))
plt.plot(model1.loss_curve_)
plt.plot(model2.loss_curve_)
plt.plot(model3.loss_curve_)
plt.plot(model4.loss_curve_)
plt.plot(model5.loss_curve_)
plt.title('Loss curve')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['(6, 3) relu', '(6, 6) relu', '(6, 3) tanh', '(6, 6) tanh', '(30, 15) relu'])
plt.show()