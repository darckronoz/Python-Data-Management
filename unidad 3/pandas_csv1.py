import pandas as pd

#problems with the csv path.******
#for importing this file I must use the double quote "" cuz it was genereting an error with single quote
#also i hah to change the \ with /.
#******
df_emp = pd.read_csv("D:/dev/university/Python-Data-Management/datas/employees.csv", sep=';')
print(df_emp.info())
print("Head")
print(df_emp.head(5))
print("Tail")
print(df_emp.tail(5))
print("Shape")
print(df_emp.shape)
print("Len")
print(print(len(df_emp)))
print("Axes")
print(df_emp.axes)
print("size")
print(df_emp.size)
print("Columns")
print(df_emp.columns)
print("Columns.tolist")
print(df_emp.columns.tolist())
