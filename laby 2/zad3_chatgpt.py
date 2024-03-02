'''
Prompt:
In python, create scatter plots with the data from the iris sklearn dataset for two variables:
sepal length and sepal width. 
The iris classes should be coloured differently and they should be denoted in the legends of the plots. 
Create three plots: with the original data, with the data normalized with min-max, with the data normalized by z-score.
What can you say about the min, max, mean and stdev of these datasets?
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load iris dataset
iris = load_iris()
X = iris.data[:, :2]  # using only sepal length and sepal width
y = iris.target

# Scatter plot function
def plot_scatter(X, y, title):
    plt.figure()
    for i in range(len(np.unique(y))):
        plt.scatter(X[y == i, 0], X[y == i, 1], label=iris.target_names[i])
    plt.title(title)
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.legend()
    plt.show()

# Original Data Scatter Plot
plot_scatter(X, y, 'Original Data Scatter Plot')

# Normalizing data with Min-Max scaler
min_max_scaler = MinMaxScaler()
X_min_max = min_max_scaler.fit_transform(X)

# Scatter Plot with Min-Max normalization
plot_scatter(X_min_max, y, 'Min-Max Normalized Scatter Plot')

# Normalizing data with Z-score (StandardScaler)
z_score_scaler = StandardScaler()
X_z_score = z_score_scaler.fit_transform(X)

# Scatter Plot with Z-score normalization
plot_scatter(X_z_score, y, 'Z-score Normalized Scatter Plot')

# Calculate statistics
def calculate_statistics(data):
    min_val = np.min(data)
    max_val = np.max(data)
    mean_val = np.mean(data)
    std_dev = np.std(data)
    return min_val, max_val, mean_val, std_dev

# Statistics for original data
min_max_orig = calculate_statistics(X)
print("Original Data:")
print("Min:", min_max_orig[0])
print("Max:", min_max_orig[1])
print("Mean:", min_max_orig[2])
print("Standard Deviation:", min_max_orig[3])

# Statistics for Min-Max normalized data
min_max_scaled = calculate_statistics(X_min_max)
print("\nMin-Max Normalized Data:")
print("Min:", min_max_scaled[0])
print("Max:", min_max_scaled[1])
print("Mean:", min_max_scaled[2])
print("Standard Deviation:", min_max_scaled[3])

# Statistics for Z-score normalized data
z_score_scaled = calculate_statistics(X_z_score)
print("\nZ-score Normalized Data:")
print("Min:", z_score_scaled[0])
print("Max:", z_score_scaled[1])
print("Mean:", z_score_scaled[2])
print("Standard Deviation:", z_score_scaled[3])
