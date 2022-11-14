import pandas as pd

dict_characteristics = {'apellido':['Ospina', 'Zapata', 'Falcao', 'Cuadrado', 'Rodriguez'],
'altura':[183.0,187.0,177.0,179.0,180.0],
'peso':[80.0,82.0,72.0,72.0,75.0]}

selcol = pd.DataFrame(dict_characteristics, index=[1,2,9,11,10])

#Exercise 0: more ways to add rows to a data frame

#to add a new player (with dataframe.loc)

num = 56

characteristics = ['Vargas', 169.0, 70.0]
selcol.loc[num] = characteristics

print(selcol)

#to add a new player (with dataframe.append)

selcoldos = pd.DataFrame({'apellido': 'sumama', 'altura': 169.5, 'peso': 89.5}, index=[8])

selcol = selcol.append(selcoldos) #use ignore index and the new dataframe'll generate new index

print(selcol)