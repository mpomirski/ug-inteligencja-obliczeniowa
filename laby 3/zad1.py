# Michał Pomirski 05.03.2024
import pandas as pd
from sklearn.model_selection import train_test_split
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

def classify_iris(sepal_l: float, sepal_w: float, petal_l: float, petal_w: float) -> str:
    if petal_w < 1:
        return("Setosa")
    elif petal_l >= 4.9:
        return("Virginica")
    else:
        return("Versicolor")
    
def test_predictions(test_inputs: List[float], test_classes: List[float]) -> None:
    good_predictions = 0
    for i in range(len(test_inputs)):
        if classify_iris(test_inputs[i][0], test_inputs[i][1], test_inputs[i][2], test_inputs[i][3]) == test_classes[i]:
            good_predictions += 1
    print(f'Good predictions: {good_predictions}')
    print(f'Accuracy: {good_predictions / len(test_inputs)}')


def main() -> None:
    df = pd.read_csv('iris.csv', na_values=["-", "nan"])
    (train_set, test_set) = train_test_split(df.values, test_size=0.7, random_state=293676)

    if DEBUG:
        debug_info(train_set, test_set)

    train_inputs = train_set[:, 0:4]
    train_classes = train_set[:, 4]
    test_inputs = test_set[:, 0:4]
    test_classes = test_set[:, 4]

    # print(pd.DataFrame(train_set, columns=['sepal_l', 'sepal_w', 'petal_l', 'petal_w', 'name']).sort_values(by='name'))

    test_predictions(test_inputs, test_classes)


if __name__ == '__main__':
    main()
