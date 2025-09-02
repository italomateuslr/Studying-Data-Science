# %%

import os
print(os.getcwd())

# os.chdir("Users\italo\Desktop\Projects\Machine Learning")

# %%

import pandas as pd

df_data = pd.read_excel("data/dados_frutas.xlsx")

df_data["Arredondada"]

# %%

from sklearn import tree

arvore = tree.DecisionTreeClassifier()

# %%

y = df_data["Fruta"]

caracteristicas = ["Arredondada","Suculenta","Vermelha","Doce"]
X = df_data[caracteristicas]

# %%

arvore.fit(X, y)