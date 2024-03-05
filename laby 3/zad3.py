# Michał Pomirski 05.03.2024
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree, naive_bayes, neighbors
from sklearn.base import ClassifierMixin
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


def test_predictions(test_inputs: List[float], test_classes: List[float], clf: ClassifierMixin) -> None:
    print(f'Classifier: {str(clf)}')
    print(f'Good predictions: {(clf.predict(test_inputs) == test_classes).sum()}')
    print(f'Accuracy: {clf.score(test_inputs, test_classes)*100:.2f}%')
    print('Confusion matrix:')
    print(confusion_matrix(test_classes, clf.predict(test_inputs)))
    print('-----------------')


def main() -> None:
    df = pd.read_csv('iris.csv', na_values=["-", "nan"])
    (train_set, test_set) = train_test_split(df.values, test_size=0.7, random_state=293676)

    if DEBUG:
        debug_info(train_set, test_set)

    train_inputs = train_set[:, 0:4]
    train_classes = train_set[:, 4]
    test_inputs = test_set[:, 0:4]
    test_classes = test_set[:, 4]

    clf_tree = tree.DecisionTreeClassifier()
    clf_tree = clf_tree.fit(train_inputs, train_classes)

    clf_3knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    clf_3knn = clf_3knn.fit(train_inputs, train_classes)

    clf_5knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    clf_5knn = clf_5knn.fit(train_inputs, train_classes)

    clf_11knn = neighbors.KNeighborsClassifier(n_neighbors=11)
    clf_11knn = clf_11knn.fit(train_inputs, train_classes)

    clf_naive_bayes = naive_bayes.GaussianNB()
    clf_naive_bayes = clf_naive_bayes.fit(train_inputs, train_classes)


    test_predictions(test_inputs, test_classes, clf_tree)
    test_predictions(test_inputs, test_classes, clf_3knn)
    test_predictions(test_inputs, test_classes, clf_5knn)
    test_predictions(test_inputs, test_classes, clf_11knn)
    test_predictions(test_inputs, test_classes, clf_naive_bayes)

    print('The best classifier is KNN with 3 neighbors.')
    

if __name__ == '__main__':
    main()
