import numpy as np

weight_matrix = np.matrix([[-0.46122, 0.97314, -0.39203], 
                           [0.78548, 2.10584, -0.57847]])

biases_matrix = np.matrix([[0.80109], 
                           [0.43529]])

weights_hidden = np.matrix([[-0.81546],
                            [1.03775]])

biases_hidden = np.matrix([[-0.2368]])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_pass(age, weight, height):
    inputs = np.matrix([age, weight, height])
    layer_1 = sigmoid(np.dot(weight_matrix, inputs.T) + biases_matrix)
    layer_2 = np.dot(weights_hidden.T, layer_1) + biases_hidden

    return layer_2

def predict(age, weight, height):
    prediction = forward_pass(age, weight, height)
    return np.round(prediction, ).tolist()[0][0]


data = [
    [23, 75, 176, True],
    [25, 67, 180, True],
    [28, 120, 175, False],
    [22, 65, 165, True],
    [46, 70, 187, True],
    [50, 68, 180, False],
    [48, 97, 178, False]
]
inputs = np.array(data)[:, :-1]
labels = np.array(data)[:, -1]
for input, label in zip(inputs, labels):
    value = predict(*input)
    print(f'Prediction: {value}, Actual: {label}', '✓' if value == label else '✗')