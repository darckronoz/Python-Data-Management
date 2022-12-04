import pandas as pd

df_emp = pd.read_csv('../Resources/employees1.csv', error_bad_lines=False, sep=';', encoding='UTF-8')

# exercise 1 - COMMISSION PCT to numeric and reformat - ',' for '.'
df_emp['COMMISSION_PCT'] = df_emp['COMMISSION_PCT'].str.replace(',', '.')
df_emp['COMMISSION_PCT'] = pd.to_numeric(df_emp['COMMISSION_PCT'])
df_emp['COMMISSION_PCT'] = df_emp['COMMISSION_PCT'].fillna(0)

print(df_emp['COMMISSION_PCT'])

# 2. Crear una nueva serie en el DataFrame empleados que calcule el salario por la comisión
newSalary = df_emp['COMMISSION_PCT'] * df_emp['SALARY']
df_emp['NEW_SALARY'] = newSalary

print(df_emp[(df_emp.NEW_SALARY > 0)][['NEW_SALARY', 'FIRST_NAME']])


# 3. Genere un nuevo DataFrame que muestre apellido, salario, fecha de contratación y comisión para los
# empleados que hayan sido contratados en el segundo semestre del 2018 y que la comisión sea superior al
# 25%.
df_emp['HIRE_DATE'] = pd.to_datetime(df_emp['HIRE_DATE'])

query = df_emp[(df_emp.COMMISSION_PCT > 0.25) & (pd.DatetimeIndex(df_emp.HIRE_DATE).year == 2018) & (pd.DatetimeIndex(df_emp.HIRE_DATE).month >= 6)][
    ['FIRST_NAME', 'LAST_NAME', 'SALARY', 'HIRE_DATE', 'COMMISSION_PCT']]
print(query)
