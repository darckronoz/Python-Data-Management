import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp

# 49. Ahora cargar en un nuevo DataFrame, equivalente al anterior con los datos del clima de la Ciudad de
# Bucaramanga.

df_bucaros = pd.read_csv('../Resources/bucaramanga.csv', sep=',', encoding='latin-1')
df_tunja = pd.read_csv('../Resources/tunja.csv', sep=',', encoding='latin-1')


print(df_bucaros.columns)

# 50. Mostrar las siguientes series del DataFrame: Departamento, Fecha, Hora, Temperatura, Velocidad del
# Viento, Precipitación, Humedad, Pronóstico.

print(df_bucaros[['Departamento', 'Fecha', 'Hora', 'Temperatura', 'Velocidad del Viento', 'Precipitación (mm/h)', 'Humedad', 'Pronóstico ']])

# 51. Renombrar las columnas Velocidad del Viento, Precipitación (mm/h) y Pronóstico por
# Velocidad_Viento, Precipitacion yPronostico respectivamente. Utilizando función rename

df_bucaros.rename(columns={'Velocidad del Viento': 'Velocidad_Viento', 'Precipitación (mm/h)': 'Precipitacion', 'Pronóstico ': 'Pronostico'}, inplace=True)
df_tunja.rename(columns={'Velocidad del Viento': 'Velocidad_Viento', 'Precipitación (mm/h)': 'Precipitacion', 'Pronóstico ': 'Pronostico'}, inplace=True)



# 52. Modificar el DataFrame de Bucaramanga y dejar solo las columnas: Departamento, Fecha, Hora, Temperatura,
# Velocidad_Viento,Precipitacion, Humedad, Pronostico.

df_bucaros.drop(['Cod_Div', 'Latitud', 'Longitud', 'Región', 'Dirección del Viento', 'Presión', 'Punto de Rocío',
               'Cobertura total nubosa', 'Probabilidad de Tormenta'], axis=1, inplace=True)
df_tunja.drop(['Cod_Div', 'Latitud', 'Longitud', 'Región', 'Dirección del Viento', 'Presión', 'Punto de Rocío',
               'Cobertura total nubosa', 'Probabilidad de Tormenta'], axis=1, inplace=True)


#53. Utilice los archivos de Barranquilla, Bogota y Cartagena; para crear el Dataframe consolidado de las cinco (5) ciudades. El
#Dataframe unido tendrá las series con columnas renombradas: Departamento, Fecha, Hora, Temperatura, Velocidad_Viento, Precipitacion,
#Humedad y Pronostico. Se debe resetear los Índices del dataframe resultado "df_unido"


df_bogota = pd.read_csv('../Resources/bogota.csv', sep=',', encoding='latin-1')
df_barranquilla = pd.read_csv('../Resources/barranquilla.csv', sep=',', encoding='latin-1')
df_cartagena = pd.read_csv('../Resources/cartagena.csv', sep=',', encoding='latin-1')

df_bogota.rename(columns={'Velocidad del Viento': 'Velocidad_Viento', 'Precipitación (mm/h)': 'Precipitacion', 'Pronóstico ': 'Pronostico'}, inplace=True)
df_barranquilla.rename(columns={'Velocidad del Viento': 'Velocidad_Viento', 'Precipitación (mm/h)': 'Precipitacion', 'Pronóstico ': 'Pronostico'}, inplace=True)
df_cartagena.rename(columns={'Velocidad del Viento': 'Velocidad_Viento', 'Precipitación (mm/h)': 'Precipitacion', 'Pronóstico ': 'Pronostico'}, inplace=True)

df_bogota.drop(['Cod_Div', 'Latitud', 'Longitud', 'Región', 'Dirección del Viento', 'Presión', 'Punto de Rocío',
               'Cobertura total nubosa', 'Probabilidad de Tormenta'], axis=1, inplace=True)
df_cartagena.drop(['Cod_Div', 'Latitud', 'Longitud', 'Región', 'Dirección del Viento', 'Presión', 'Punto de Rocío',
               'Cobertura total nubosa', 'Probabilidad de Tormenta'], axis=1, inplace=True)
df_barranquilla.drop(['Cod_Div', 'Latitud', 'Longitud', 'Región', 'Dirección del Viento', 'Presión', 'Punto de Rocío',
               'Cobertura total nubosa', 'Probabilidad de Tormenta'], axis=1, inplace=True)

df_unido = pd.concat([df_tunja, df_bucaros, df_barranquilla, df_bogota, df_cartagena], axis=0)
print(df_unido.columns)

df_unido = df_unido.reset_index(drop=True)
print(df_unido)

#54. Mostrar el promedio de la Velocidad_Viento de los cinco (5) departamentos.

query = df_unido.groupby('Departamento')
print(query['Velocidad_Viento'].mean())

#55. : Incluya en el Dataframe unido una nueva columna "Ciudad". Los valores de esta nueva columna dependerán de los valores de la
#serie "Departamento". Entonces, cuando la seie "Departamento" sea "ATLÁNTICO", la nueva serie "Ciudad" se le asignará el valor de "Barraquila".
#Correspondientemente para las otras "BOYACÁ" --> "Tunja", "BOGOTÁ. D. C." --> "Bogotá", "SANTANDER" --> "Bucaramanga" y "BOLÍVAR" -->
#"Cartagena".


city = [{'Departamento': 'BOYACÁ', 'Ciudad': 'Tunja'},
        {'Departamento': 'ATLÁNTICO', 'Ciudad': 'Barranquilla'},
        {'Departamento': 'BOGOTÁ. D. C.', 'Ciudad': 'Bogotá'},
        {'Departamento': 'BOLÍVAR', 'Ciudad': 'Cartagena'},
        {'Departamento': 'SANTANDER', 'Ciudad': 'Bucaramanga'}]

city_df = pd.DataFrame(city)
df_unido = pd.merge(df_unido, city_df, on='Departamento')

# 56. Verifique que la serie "Ciudad" corresponda con el valor de la serie Departamento. Borre la Serie "Departamento" del Dataframe
# unido. Función drop

query = df_unido.groupby('Departamento')
print(query['Temperatura'].mean())
query = df_unido.groupby('Ciudad')
print(query['Temperatura'].mean())

df_unido.drop(['Departamento'], axis=1, inplace=True)

# 57. Halle el promedio de Temperatura para cada una de las ciudades.

query = df_unido.groupby('Ciudad')['Temperatura'].mean().reset_index()
print(query)

# 58. Ordene la consulta anterior para que muestre las temperaturas de las ciudades en orden ascendente y
# descendente. Funciones mean y sort_values.

query.sort_values(by='Temperatura', ascending=True, inplace=True)
print('ascendente')
print(query)
query.sort_values(by='Temperatura', ascending=False, inplace=True)
print('descendente')
print(query)

# 59. Defina una nueva Columna o serie, "Rangos", que corresponda a un valor (Baja, Media y Alta) a partir de las siguientes
# categorías definidas de la serie "Temperatura":
# Temperatutras mayores a 4 grados y menores de 10 grados, será Rango "Baja".
# Temperatutras mayores o iguales a 10 grados y menor o igual a 16 grados, será Rango "Media".
# Temperaturas mayores a 16 grados, será Rango "Alta".
# Se puede realizar a partir de una función de usuario o también función lambda. y la función apply

ranges = np.arange(0, len(df_unido)+1)
ranges = pd.Series(str(ranges))
df_unido['Rangos'] = ranges
for i in range(len(df_unido)):
    if 4 < df_unido['Temperatura'][i] < 10:
        df_unido.at[i, 'Rango']='Baja'
    if 10 <= df_unido['Temperatura'][i] <= 16:
        df_unido.at[i, 'Rango']='Media'
    if df_unido['Temperatura'][i] > 16:
        df_unido.at[i, 'Rango']='Alta'

# 60. Agrupe ahora por rangos y realice el conteo

query = df_unido.groupby('Rango')['Temperatura'].count()
print(query)

# 61. Muestre la cantidad de temperaturas agrupadas por ciudad y rango

query = df_unido.groupby(['Rango', 'Ciudad'])['Temperatura'].count()
print(query)

# 62. Elabore gráfica que muestre el comportamiento de la temperatura en las cinco ciudades. Seguramente se debe consultar
# funcionalidades como, reset_index

pyp.plot(df_unido[df_unido['Ciudad'] == 'Tunja'][['Temperatura']].reset_index(drop=True))
pyp.plot(df_unido[df_unido['Ciudad'] == 'Cartagena'][['Temperatura']].reset_index(drop=True))
pyp.plot(df_unido[df_unido['Ciudad'] == 'Barranquilla'][['Temperatura']].reset_index(drop=True))
pyp.plot(df_unido[df_unido['Ciudad'] == 'Bogotá'][['Temperatura']].reset_index(drop=True))
pyp.plot(df_unido[df_unido['Ciudad'] == 'Bucaramanga'][['Temperatura']].reset_index(drop=True))
pyp.title('Cambio en Temp por ciudades')
pyp.xlabel('Cantidad Valores')
pyp.ylabel('Temperatura')
pyp.legend(['Tunja', 'Cartagena', 'Barranquilla', 'Bogotá', 'Bucaramanga'])
pyp.show()


