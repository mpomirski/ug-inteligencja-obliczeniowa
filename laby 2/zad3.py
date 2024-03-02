# Michał Pomirski 02.03.2024
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import pandas as pd

iris = datasets.load_iris()
# Original dataset
print('Original dataset:')
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="FlowerType")
sepal_length = iris.data[:,0]
sepal_width = iris.data[:,1]
_, (ax1, ax2, ax3), = plt.subplots(1, 3, figsize=(15, 5))
scatter = ax1.scatter(sepal_length, sepal_width, c=iris.target)
ax1.set_xlabel('Sepal length (cm)')
ax1.set_ylabel('Sepal width (cm)')
ax1.set_title('Original dataset')
_ = ax1.legend(scatter.legend_elements()[0], iris.target_names)
print(f'min sepal length: {np.min(sepal_length)}, max sepal length: {np.max(sepal_length)}')
print(f'min sepal width: {np.min(sepal_width)}, max sepal width: {np.max(sepal_width)}')
print(f'mean sepal length: {np.mean(sepal_length):.2f}, mean sepal width: {np.mean(sepal_width):.2f}')
print(f'std sepal length: {np.std(sepal_length):.2f}, std sepal width: {np.std(sepal_width):.2f}')


# min-max 
print('Min-max Normalised dataset:')
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
sepal_length = X_scaled[:,0]
sepal_width = X_scaled[:,1]
scatter = ax2.scatter(sepal_length, sepal_width, c=iris.target)
ax2.set_xlabel('Sepal length (cm)')
ax2.set_ylabel('Sepal width (cm)')
ax2.set_title('Min-max Normalised dataset')
_ = ax2.legend(scatter.legend_elements()[0], iris.target_names)
print(f'min sepal length: {np.min(sepal_length)}, max sepal length: {np.max(sepal_length)}')
print(f'min sepal width: {np.min(sepal_width)}, max sepal width: {np.max(sepal_width)}')
print(f'mean sepal length: {np.mean(sepal_length):.2f}, mean sepal width: {np.mean(sepal_width):.2f}')
print(f'std sepal length: {np.std(sepal_length):.2f}, std sepal width: {np.std(sepal_width):.2f}')

# z-score
print('Z-score Normalised dataset:')
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
sepal_length = X_scaled[:,0]
sepal_width = X_scaled[:,1]
scatter = ax3.scatter(sepal_length, sepal_width, c=iris.target)
ax3.set_xlabel('Sepal length (cm)')
ax3.set_ylabel('Sepal width (cm)')
ax3.set_title('Z-score Scaled Dataset')
_ = ax3.legend(scatter.legend_elements()[0], iris.target_names)
print(f'min sepal length: {np.min(sepal_length)}, max sepal length: {np.max(sepal_length)}')
print(f'min sepal width: {np.min(sepal_width)}, max sepal width: {np.max(sepal_width)}')
print(f'mean sepal length: {np.mean(sepal_length):.2f}, mean sepal width: {np.mean(sepal_width):.2f}')
print(f'std sepal length: {np.std(sepal_length):.2f}, std sepal width: {np.std(sepal_width):.2f}')

plt.show()