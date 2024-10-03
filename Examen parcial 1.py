import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paso 1: Cargar e Inspeccionar los Datos
df_flights = pd.read_csv('flights.csv')
print(df_flights.head())
print(df_flights.info())

# Paso 2: Limpieza de Datos
valores_faltantes = df_flights.isnull().sum()
print(valores_faltantes[valores_faltantes > 0])
df_flights['DepDelay'].fillna(0, inplace=True)
df_flights['ArrDelay'].fillna(0, inplace=True)

## 2.2. Identificar y Eliminar Atípicos
Q1_dep = df_flights['DepDelay'].quantile(0.25)
Q3_dep = df_flights['DepDelay'].quantile(0.75)
IQR_dep = Q3_dep - Q1_dep
condicion_atipicos_dep = (df_flights['DepDelay'] < (Q1_dep - 1.5 * IQR_dep)) | (df_flights['DepDelay'] > (Q3_dep + 1.5 * IQR_dep))
df_flights = df_flights[~condicion_atipicos_dep]

Q1_arr = df_flights['ArrDelay'].quantile(0.25)
Q3_arr = df_flights['ArrDelay'].quantile(0.75)
IQR_arr = Q3_arr - Q1_arr
condicion_atipicos_arr = (df_flights['ArrDelay'] < (Q1_arr - 1.5 * IQR_arr)) | (df_flights['ArrDelay'] > (Q3_arr + 1.5 * IQR_arr))
df_flights = df_flights[~condicion_atipicos_arr]

# Paso 3: Explorar los Datos Limpiados
estadisticas_resumen = df_flights.describe()
print(estadisticas_resumen)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df_flights['DepDelay'], bins=30, kde=True, color='blue')
plt.title('Distribución de Retrasos de Salida')
plt.xlabel('Retraso de Salida (minutos)')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
sns.histplot(df_flights['ArrDelay'], bins=30, kde=True, color='red')
plt.title('Distribución de Retrasos de Llegada')
plt.xlabel('Retraso de Llegada (minutos)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Paso 4: Preguntas de Análisis
retraso_promedio_dep = df_flights['DepDelay'].mean()
retraso_promedio_arr = df_flights['ArrDelay'].mean()
print(f'Retraso Promedio de Salida: {retraso_promedio_dep:.2f} minutos')
print(f'Retraso Promedio de Llegada: {retraso_promedio_arr:.2f} minutos')

retraso_aerolineas = df_flights.groupby('Carrier')['ArrDelay'].mean().sort_values()
print(retraso_aerolineas)

plt.figure(figsize=(10, 5))
retraso_aerolineas.plot(kind='bar', color='orange')
plt.title('Retraso Promedio de Llegada por Aerolínea')
plt.ylabel('Retraso Promedio de Llegada (minutos)')
plt.xlabel('Aerolínea')
plt.show()

retraso_dias = df_flights.groupby('DayOfWeek')['ArrDelay'].mean().sort_values()
print(retraso_dias)

plt.figure(figsize=(10, 5))
retraso_dias.plot(kind='bar', color='green')
plt.title('Retraso Promedio de Llegada por Día de la Semana')
plt.ylabel('Retraso Promedio de Llegada (minutos)')
plt.xlabel('Día de la Semana')
plt.xticks(ticks=range(7), labels=['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'], rotation=45)
plt.show()

retraso_aeropuertos = df_flights.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False)
print(retraso_aeropuertos.head(10))

plt.figure(figsize=(8, 6))
sns.scatterplot(x='DepDelay', y='ArrDelay', data=df_flights)
plt.title('Retraso de Salida vs Retraso de Llegada')
plt.xlabel('Retraso de Salida (minutos)')
plt.ylabel('Retraso de Llegada (minutos)')
plt.axhline(0, color='red', linestyle='--', label='Llegada a Tiempo')
plt.axvline(0, color='blue', linestyle='--', label='Salida a Tiempo')
plt.legend()
plt.show()

llegadas_tardias = df_flights[df_flights['ArrDelay'] > 15]
ruta_llegadas_tardias = llegadas_tardias.groupby(['OriginAirportName', 'DestAirportName']).size().reset_index(name='Llegadas Tardías')
ruta_llegadas_tardias = ruta_llegadas_tardias.sort_values(by='Llegadas Tardías', ascending=False)
print(ruta_llegadas_tardias.head(10))

ruta_retraso_arr = df_flights.groupby(['OriginAirportName', 'DestAirportName'])['ArrDelay'].mean().reset_index()
ruta_retraso_arr = ruta_retraso_arr.sort_values(by='ArrDelay', ascending=False)
print(ruta_retraso_arr.head(10))
