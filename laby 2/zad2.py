import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="FlowerType")
print(X.head())

pca_iris = PCA(n_components=3).fit(iris.data)
print(pca_iris)
print()
print(pca_iris.explained_variance_ratio_)
print()
print(pca_iris.components_)
print()
print(pca_iris.transform(iris.data))


