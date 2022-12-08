import pandas as pd
import numpy as np

df_emp = pd.read_csv('../Resources/employees2.csv', sep=';', encoding='UTF-8')
print(df_emp.columns)
#
# 4. Mostsrar los empleados que son del departamento 50 y tienen un salario igual o superior a 4000. Proyectar
# nombre, apellido, salario y departamento

print(df_emp.query('DEPARTMENT_ID == 50 and SALARY >= 4000')[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']])

# 5. Cuál es el cargo (Job_Id) de empleados que tengan nombre Alexander. Mostrar nombre, apellido y codigo de trabajo.

print(df_emp.query("FIRST_NAME == 'Alexander'")[['JOB_ID', 'FIRST_NAME', 'LAST_NAME']])

# 6. Seleccionar los empleados cuyo salario es igual al mínimo salario de la compañia.

minsalary = min(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == minsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 7. Seleccionar los empleados cuyo salario es mayor al salario promedio de la compañia.

meansalary = np.mean(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY > meansalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 8. Listar el empleado con el salario mas alto de la compañia

maxsalary = max(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == maxsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 9. Consultar la cantidad de empleados que pertenecen a cada departamento.

group_bydep1 = df_emp.groupby('DEPARTMENT_ID')
print(group_bydep1[['FIRST_NAME']].count())

# 10. Determinar para cada departamento cual es el minímo salario.

group_bydep2 = df_emp.groupby('DEPARTMENT_ID')
print(group_bydep2[['SALARY']].min())

# 11. Determinar para cada departamento cual es el máximo salario.

group_bydep3 = df_emp.groupby('DEPARTMENT_ID')
print(group_bydep2[['SALARY']].max())

# 12. Cuales son los 5 cargos más comunes. Probar con la función value_counts()

print(df_emp['JOB_ID'].value_counts().rank(method='max').head(5))

#  13. Cuales son los 5 departamentos con más empleados (más comunes)

print(df_emp[['DEPARTMENT_ID']].value_counts().rank(method='max').head(5))

# 14. Lista de empleados que el apellido contenga las letras "man". Posiblemente es necesario utilizar funciones como: contains,
# lower y upper

print(df_emp[df_emp.LAST_NAME.str.contains('[manMAN]', regex=True)]['LAST_NAME'])

# 15. Mostrar los empleados, donde el apellido contenga una letra H o la letra k.

print(df_emp[df_emp.LAST_NAME.str.contains('[hkHK]', regex=True)]['LAST_NAME'])

# 16. Mostrar los empleados, donde el apellido contenga una letra h, enseguida 2 caracteres cualquiera y luego la letra o.

print(df_emp[df_emp.LAST_NAME.str.contains("h..o", regex=True)]['LAST_NAME'])

# 17. Mostrar los empleados donde el apellido finalilice con la letra g

print(df_emp[df_emp.LAST_NAME.str.contains("g$", regex=True)]['LAST_NAME'])

# 18. Nombre del empleado con mayor salario de la organización

maxsalary = max(list(df_emp['SALARY']))
print(df_emp[df_emp.SALARY == maxsalary][['FIRST_NAME', 'LAST_NAME', 'SALARY']])

# 19. Ordene los salarios de los empleados de forma descendente. Utilice función sort_values

print(df_emp[['FIRST_NAME', 'LAST_NAME', 'SALARY']].sort_values(by=['SALARY'], ascending=False))

# 20. Empleados cuyo salario es mayor o igual a 13500 y menor o igual a 17000. Mostrar las columnas FIRST_NAME, LAST_NAME,
# JOB_ID, SALARY.

print(df_emp.query('SALARY >= 13500 and SALARY <= 17000')[['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'SALARY']])

# 21. . Empleados que pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas
# DEPARTMENT_ID,FIRST_NAME. Utilice la función isin

print(df_emp[df_emp.DEPARTMENT_ID.isin([10, 20, 40, 70])][['FIRST_NAME', 'DEPARTMENT_ID']])

# 22. Empleados que NO pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas
# DEPARTMENT_ID,FIRST_NAME. Utilice la negación ~

print(df_emp[~df_emp.DEPARTMENT_ID.isin([10, 20, 40, 70])][['FIRST_NAME', 'DEPARTMENT_ID']])

# 23. Identifique la razón por la que aparecen en el DataFrame resultado (df_unido) MANAGER_ID_x y
# MANAGER_ID_y, y el por qué no tienen la misma información. Explíquelo desde el punto de vista
# Modelo Relacional

df_dep = pd.read_csv('../Resources/departments.csv', sep=';', encoding='UTF-8')
print(df_dep.columns)

df_unido = pd.merge(df_emp, df_dep, on='DEPARTMENT_ID')

print(df_unido.columns)

print(df_emp['MANAGER_ID'].head(5))
print(df_dep['MANAGER_ID'].head(5))
print(df_unido['MANAGER_ID_x'].head(5))
print(df_unido['MANAGER_ID_y'].head(5))

#manager ID x es el jefe que corresponde a cada empleado y managerID_y es el jefe de cada departamento.



