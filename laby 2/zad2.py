# Michał Pomirski 02.03.2024
import matplotlib.pyplot as plt
import numpy as np
from numpy import var
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
print(f'Wariancja 0: {var(pca_iris.transform(iris.data)[:,0])}')
print(f'Wariancja 1: {var(pca_iris.transform(iris.data)[:,1])}')
print(f'Wariancja 2: {var(pca_iris.transform(iris.data)[:,2])}')
'''
var0: 4.200053427994632
var1: 0.24105294294244256
var2: 0.07768810337596654
Strata informacji spowodowania usunięciem i ostatnich kolumn: sum_{k=n-1}^{n-i} var_k / sum_{k=0}^{n-1} var_k
'''
#Usunięcie ostatniej kolumny:
# n = 3, i = 1, n-i = n-1 = 2
print('Strata informacji spowodowana usunięciem ostatniej kolumny: ')
loss = sum([var(pca_iris.transform(iris.data)[:,i]) for i in range(1,1 + 1)]) / sum([var(pca_iris.transform(iris.data)[:,i]) for i in range(1 + 1)])
print(f'{loss*100:.2f}%')
print('Strata jest większa niż 5%, więc nie usuwamy ostatniej kolumny.')

#Wizualizacja:
fig = plt.figure(1, figsize=(8, 6))
plt.clf()

ax = fig.add_subplot(111, projection='3d', elev=48, azim=134)
ax.set_position([0, 0, 0.95, 1])
plt.cla()
X = pca_iris.transform(iris.data)

for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
    ax.text3D(
        X[iris.target == label, 0].mean(),
        X[iris.target == label, 1].mean() + 1.5,
        X[iris.target == label, 2].mean(), 
        name,
        horizontalalignment='center',
        bbox=dict(alpha=.5, edgecolor='w', facecolor='w'),
    )

y = np.choose(iris.target, [1, 2, 0]).astype(float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.nipy_spectral, edgecolor='k')
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])
plt.show()


