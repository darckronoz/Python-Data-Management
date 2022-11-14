import pandas as pd

#Dataframe storage the data as an sorted data table in rows and columns.
#each column of the dataframe is a SERIE where the index match with the dataframe indexs.

#create a data frame from a dictionary
#the keys are the columns names, and the values are the characteristics.

#exmaple, dataframe with soccer team, adding high and weigth

dict_characteristics = {'apellido':['Ospina', 'Zapata', 'Falcao', 'Cuadrado', 'Rodriguez'],
'altura':[183.0,187.0,177.0,179.0,180.0],
'peso':[80.0,82.0,72.0,72.0,75.0]}

selcol = pd.DataFrame(dict_characteristics, index=[1,2,9,11,10])
selcol.index.name = 'numerix'
print(selcol)

#access to the registers by index

print(selcol[selcol.altura==187.0])
print(selcol[selcol.apellido=='Zapata'])

#to add a new player (with dataframe.loc)

num = 56

characteristics = ['Vargas', 169.0, 70.0]
selcol.loc[num] = characteristics

print(selcol)

#to add a new player (with dataframe.append)

selcoldos = pd.DataFrame({'apellido': 'sumama', 'altura': 169.5, 'peso': 89.5}, index=[8])

selcol = selcol.append(selcoldos)

print(selcol.keys())
print(selcol.dtypes)
print(selcol.values)

#delete column
#with drop
selcol.drop('peso', axis=1, inplace=True) #inplace = True to make the delete permanent
print(selcol)

#with del
#you can also use 

del selcol['altura']

print(selcol)

#delete rows

selcol23 = selcol.drop([8,56,2]) #array with the index of the row to be eliminated
print(selcol23)

print(selcol.columns) #to get the columns of the dataframe
print(selcol.index) #to get the indexs of the dataframes.

#sort a dataframe.
print('\n sort a dataframe \n')
newselcol = pd.DataFrame(dict_characteristics, index=[1, 2, 9, 11, 10])
print(newselcol)
print(newselcol.sort_index())
print(newselcol.sort_values(by=['altura'],ascending=False))#inplace=false by default.







