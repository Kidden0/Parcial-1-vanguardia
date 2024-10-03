import pandas as pd
from sklearn.datasets import fetch_openml

dataset = fetch_openml(name="titanic", version=1)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

df.to_csv('titanic.csv', index=False)

print("El archivo CSV ha sido guardado.")

print("Descripción de la base de datos:")
print(df.describe(include='all'))  

variable_types = df.dtypes
print("\nTipos de variables:")
print(variable_types)
