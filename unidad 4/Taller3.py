import pandas as pd
import numpy as np

df_emp = pd.read_csv('../Resources/employees2.csv', sep=';', encoding='UTF-8')
print(df_emp.columns)
# 1. Mostsrar los empleados que son del departamento 50 y tienen un salario igual o superior a 4000. Proyectar
# nombre, apellido, salario y departamento

print(df_emp.query('DEPARTMENT_ID == 50 and SALARY >= 4000')[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']])

# 2. Cuál es el cargo (Job_Id) de empleados que tengan nombre Alexander. Mostrar nombre, apellido y codigo de trabajo.

print(df_emp.query("FIRST_NAME == 'Alexander'")[['JOB_ID', 'FIRST_NAME', 'LAST_NAME']])

# 3. Seleccionar los empleados cuyo salario es igual al mínimo salario de la compañia.

minsalary = min(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == minsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 4. Seleccionar los empleados cuyo salario es mayor al salario promedio de la compañia.

meansalary = np.mean(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY > meansalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 5. Listar el empleado con el salario mas alto de la compañia

maxsalary = max(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == maxsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 6. Consultar la cantidad de empleados que pertenecen a cada departamento.

group_bydep1 = df_emp.groupby('DEPARTMENT_ID')
print(group_bydep1[['FIRST_NAME']].count())

# 7. Determinar para cada departamento cual es el minímo salario.

group_bydep2 = df_emp.groupby('DEPARTMENT_ID')
print(group_bydep2[['SALARY']].min())

# 8. Determinar para cada departamento cual es el máximo salario.

group_bydep3 = df_emp.groupby('DEPARTMENT_ID')
print(group_bydep2[['SALARY']].max())

# 9. Cuales son los 5 cargos más comunes. Probar con la función value_counts()

print(df_emp['JOB_ID'].value_counts().rank(method='max').head(5))

#  10. Cuales son los 5 departamentos con más empleados (más comunes)

print(df_emp[['DEPARTMENT_ID']].value_counts().rank(method='max').head(5))

# 11. Lista de empleados que el apellido contenga las letras "man". Posiblemente es necesario utilizar funciones como: contains,
# lower y upper

print(df_emp[df_emp.LAST_NAME.str.contains('[manMAN]', regex=True)]['LAST_NAME'])

# 12. Mostrar los empleados, donde el apellido contenga una letra H o la letra k.

print(df_emp[df_emp.LAST_NAME.str.contains('[hkHK]', regex=True)]['LAST_NAME'])

# 13. Mostrar los empleados, donde el apellido contenga una letra h, enseguida 2 caracteres cualquiera y luego la letra o.

print(df_emp[df_emp.LAST_NAME.str.contains("h..o", regex=True)]['LAST_NAME'])

# 14. Mostrar los empleados donde el apellido finalilice con la letra g

print(df_emp[df_emp.LAST_NAME.str.contains("g$", regex=True)]['LAST_NAME'])

# 15. Nombre del empleado con mayor salario de la organización

maxsalary = max(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == maxsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 16. Ordene los salarios de los empleados de forma descendente. Utilice función sort_values

print(df_emp[['FIRST_NAME', 'LAST_NAME', 'SALARY']].sort_values(by=['SALARY'], ascending=False))

# 17. Empleados cuyo salario es mayor o igual a 13500 y menor o igual a 17000. Mostrar las columnas FIRST_NAME, LAST_NAME,
# JOB_ID, SALARY.

print(df_emp.query('SALARY >= 13500 and SALARY <= 17000')[['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'SALARY']])

# 18. . Empleados que pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas
# DEPARTMENT_ID,FIRST_NAME. Utilice la función isin

print(df_emp[df_emp.DEPARTMENT_ID.isin([10, 20, 40, 70])][['FIRST_NAME', 'DEPARTMENT_ID']])

# 19. Empleados que NO pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas
# DEPARTMENT_ID,FIRST_NAME. Utilice la negación ~

print(df_emp[~df_emp.DEPARTMENT_ID.isin([10, 20, 40, 70])][['FIRST_NAME', 'DEPARTMENT_ID']])
