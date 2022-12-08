import pandas as pd
import numpy as np

df_dep = pd.read_csv('../Resources/departments.csv', sep=';', encoding='UTF-8')
print(df_dep.columns)

df_emp = pd.read_csv('../Resources/employees2.csv', sep=';', encoding='UTF-8')
print(df_emp.columns)

# 24. Identifique la diferencia en el how con el tipo de join: left, right y outer

# outer

df_outer = pd.merge(df_emp, df_dep, how='outer', on='MANAGER_ID')

print(df_outer.columns)
# This is usefully when we need to combine both df and get all the matches in either left or right join.

# When rows in both the dataframes do not match, the resulting dataframe
# will have NaN for every column of the dataframe that lacks a matching row.

# right and left:

df_ri_le = pd.merge(df_emp, df_dep, left_on='DEPARTMENT_ID', right_on='MANAGER_ID')
print(df_ri_le.columns)

# But, what if the column names are different in the two dataframes?
# Then, we have to explicitly mention both the column names.
#
# ‘left_on’ and ‘right_on’ are two arguments through which we can achieve this.
# ‘left_on’ is the name of the key in the left dataframe and ‘right_on’ in the right dataframe:

# load employees_43

df_emp = pd.read_csv('../Resources/employees_43.csv', sep='-', encoding='UTF-8')

# 25. obersevar la estructura
print(df_emp.columns)
print(df_emp.head(5))
for i in range(len(df_emp.columns)):
    print([df_emp.columns[i]])

# 26. Identifique para cada una de las series los valores nulos.

for i in range(len(df_emp.columns)):
    print(df_emp[df_emp[df_emp.columns[i]].isnull()][[df_emp.columns[i]]])

# 27. Elimine todas las filas que tienen valores nulos.

df_emp.dropna(inplace=True)

# 28. Homogenizar cada serie al tipo de dato que corresponda a la mayoria de sus valores (por ejmplo salary
# según los datos debe ser entero).

# start date as datetime
df_emp['Start Date'] = pd.to_datetime(df_emp['Start Date'])

# salary as int
df_emp['Salary'] = df_emp[df_emp.Salary.str.contains('^[0-9]+$', regex=True)]['Salary']
df_emp['Salary'] = df_emp['Salary'].fillna(0).astype(int)

# Bonus % as float
df_emp['Bonus %'] = df_emp['Bonus %'].str.replace(',', '.')
df_emp['Bonus %'] = df_emp['Bonus %'].fillna(0).astype(float)

# 29. Ordene el DataFrame alfabeticamente por apellido

df_emp.sort_values(by='First Name', inplace=True)

# 30. Asignar una nueva serie que corresponde a la llave, que debe iniciar en 100.

keys_df = pd.Series(np.arange(100, df_emp.shape[0] + 1))
df_emp['Keys'] = keys_df.apply(int)
print(df_emp['Keys'])

# 31. Crear un nuevo DataFrame con los valores únicos de la serie Team.

teams = df_emp['Team'].unique()
team_df = pd.DataFrame(data=teams)
team_df.rename(columns={0: 'Team'}, inplace=True)

# 32. Crearle al anterior DataFrame la llave primaria con un valor enumerado que inicie en 1.

team_key = pd.Series(np.arange(1, team_df.shape[0] + 1))
team_df['Codigo_Team'] = team_key

# 33. Crear una nueva serie con el nombre Codigo_Team en la DataFrame empleados, donde los valores
# numéricos correspondan a la llave del dataframe Team.

df_emp = pd.merge(df_emp, team_df, on='Team')
print(df_emp[df_emp['Team'] == 'Legal'][['Team', 'First Name', 'Codigo_Team']])

# 34. Eliminar la serie Team del DataFrame empleados que contenia los nombres de equipos.

df_emp.drop(['Team'], axis=1, inplace=True)
print(df_emp.columns)

# 35. Cantidad de empleados por equipo (team). Utilice la función groupby()

query = df_emp.groupby('Codigo_Team')
print(query[['First Name']].count())

# 36. Calcular el valor total de los salarios por equipo.

query = df_emp.groupby('Codigo_Team')
print(query[['Salary']].sum())

# 37. Cantidad de mujeres y hombres el dataframe.

query = df_emp.groupby('Gender')
print(query[['First Name']].count())

# 38. Empleados quienes hicieron login en el mes equivalente al mes actual.

print(df_emp[pd.DatetimeIndex(df_emp['Start Date']).month == 12][['Start Date', 'First Name', 'Last Login Time']])

# 39. Cantidad de empleados que hicieron login por año.

query = df_emp.groupby(pd.DatetimeIndex(df_emp['Start Date']).year)
print(query['First Name'].count())

# 40. Cantidad de empleados que no han hecho login en los ultimos quince años.

df_emp_aux = df_emp
df_emp_aux['Start Date'] = df_emp_aux[(pd.DatetimeIndex(df_emp['Start Date']).year < 2007)][['Start Date']]
query = df_emp_aux.groupby(pd.DatetimeIndex(df_emp_aux['Start Date']).year)
print(query['First Name'].count())