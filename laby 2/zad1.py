import pandas as pd
import os
print(os.path.curdir)
df = pd.read_csv("H:\\mpomirski\\4 semestr\\inteligencja obliczeniowa\\laby 2\\iris.csv")

print(df)
print(df.values)
print(df.values[:, 0])
print(df.values[5:11, :])
print(df.values[1, 4])