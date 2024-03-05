# Michał Pomirski 05.03.2024
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix
from typing import List
DEBUG = False

def debug_info(train_set: List[float], test_set: List[float]):
    train_inputs = train_set[:, 0:4]
    train_classes = train_set[:, 4]
    test_inputs = test_set[:, 0:4]
    test_classes = test_set[:, 4]
    print('Test set:')
    print(f'{test_set}', end='\n\n')
    print('Test set shape:')
    print(f'{test_set.shape}', end='\n\n')
    print('Train set:')
    print(f'{train_set}', end='\n\n')
    print('Train set shape:')
    print(f'{train_set.shape}', end='\n\n')

    print('Train inputs:')
    print(f'{train_inputs}', end='\n\n')
    print('Train classes:')
    print(f'{train_classes}', end='\n\n')
    print('Test inputs:')
    print(f'{test_inputs}', end='\n\n')
    print('Test classes:')
    print(f'{test_classes}', end='\n\n')


def test_predictions(test_inputs: List[float], test_classes: List[float], clf: tree.DecisionTreeClassifier) -> None:
    print(clf.score(test_inputs, test_classes))
    good_predictions = clf.predict(test_inputs) == test_classes
    print(f'Good predictions: {good_predictions.sum()}')
    print(f'Accuracy: {good_predictions.sum() / len(test_inputs)}')
    print('Confusion matrix:')
    print(confusion_matrix(test_classes, clf.predict(test_inputs)))


def main() -> None:
    df = pd.read_csv('iris.csv', na_values=["-", "nan"])
    (train_set, test_set) = train_test_split(df.values, test_size=0.7, random_state=293676)

    if DEBUG:
        debug_info(train_set, test_set)

    train_inputs = train_set[:, 0:4]
    train_classes = train_set[:, 4]
    test_inputs = test_set[:, 0:4]
    test_classes = test_set[:, 4]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_inputs, train_classes)
    tree.plot_tree(clf)

    test_predictions(test_inputs, test_classes, clf)
    print('Było blisko, ale drzewko jest lepsze :(')

if __name__ == '__main__':
    main()
