

#change 
import pandas as pd

df_emp = pd.read_csv('/home/darckronoz/DEV/UPTC/Gestión_datos_python/Resources/employees.csv', error_bad_lines=False, sep=';', encoding='UTF-8')

print(df_emp.info())