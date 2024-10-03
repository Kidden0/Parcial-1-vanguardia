import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

estadisticas = df.describe(include='all')
print("Parámetros estadísticos de todas las variables:\n", estadisticas)

# 1. Gráfica de la distribución de la edad
plt.figure(figsize=(10, 6))
sns.histplot(df['age'].dropna(), bins=30, kde=True)  
plt.title('Distribución de la Edad de los Pasajeros')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

# 2. Gráfica de tarifas pagadas por clase de pasajero
plt.figure(figsize=(10, 6))
sns.boxplot(x='pclass', y='fare', data=df)
plt.title('Tarifas Pagadas por Clase de Pasajero')
plt.xlabel('Clase de Pasajero')
plt.ylabel('Tarifa')
plt.grid()
plt.show()

# 3. Gráfica de la distribución del género
plt.figure(figsize=(10, 6))
sns.countplot(x='sex', data=df)
plt.title('Distribución de Género de los Pasajeros')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.grid()
plt.show()
