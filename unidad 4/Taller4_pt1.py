import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp

df_tunja = pd.read_csv('../Resources/tunja.csv', sep=',', encoding='latin-1')

print(df_tunja.columns)

# 42. Mostrar las siguientes series del DataFrame: Departamento, Fecha, Hora, Temperatura, Velocidad del
# Viento, Precipitación, Humedad y Pronóstico.

print(df_tunja[['Departamento', 'Fecha', 'Hora', 'Temperatura', 'Velocidad del Viento', 'Precipitación (mm/h)', 'Humedad', 'Pronóstico ']])

# 43. Renombrar las columnas Velocidad del Viento, Precipitación (mm/h) y Pronóstico por
# Velocidad_Viento, Precipitacion yPronostico respectivamente. Utilizando función rename

df_tunja.rename(columns={'Velocidad del Viento': 'Velocidad_Viento', 'Precipitación (mm/h)': 'Precipitacion', 'Pronóstico ': 'Pronostico'}, inplace=True)

# 44. Modificar el DataFrame de Tunja y dejar solo las columnas: Departamento, Fecha, Hora, Temperatura,
# Velocidad_Viento,Precipitacion, Humedad, Pronostico.

df_tunja.drop(['Cod_Div', 'Latitud', 'Longitud', 'Región', 'Dirección del Viento', 'Presión', 'Punto de Rocío',
               'Cobertura total nubosa', 'Probabilidad de Tormenta'], axis=1, inplace=True)

# 45. Hallar el promedio, máxima y mínima temperatura. mean, max y min

print('Mean Temperature')
print(np.mean(df_tunja['Temperatura']))
print('Max Temperature')
print(np.max(df_tunja['Temperatura']))
print('Min Temperature')
print(np.min(df_tunja['Temperatura']))

# 46. Agrupar por la serie de fecha del DataFrame. Utilice función groupby(). Ahora muestre el promedio de
# esa función de grupo.

df_tunja['Fecha'] = pd.DatetimeIndex(df_tunja['Fecha'])
query = df_tunja.groupby('Fecha')
print(query['Fecha'].mean())

# 47. Utilizando la función de grupo calcular la Cantidad de registros, valores mínimos y máximos

print(query['Temperatura'].count())
print(query['Temperatura'].max())
print(query['Temperatura'].min())


# 48. Agregar el titulo y nombres a los ejes a la gráfica.

pyp.plot(df_tunja['Temperatura'], color='purple')
pyp.title('temperaturas')
pyp.xlabel('time')
pyp.ylabel('temperature')
pyp.show()

