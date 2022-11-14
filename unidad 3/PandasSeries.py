import pandas as pd

#data structures with pandas

#series. 
#a serie is an unidimensional array with and index for each array position.

seleccionColombia = pd.Series(
['Ospina', 'Zapata', 'Falcao', 'Cuadrado', 'Rodriguez'],
index=[1, 2, 9, 11, 10]) #the index can be disordered.
print(type(seleccionColombia))

#series with dictionaries
#series can be defined from dictionaries.

dict_selcol = {1:'Ospina', 2: 'Zapata', 9: 'Falcao', 11: 'Cuadrado', 10: 'Rodriguez'}

ser_selcol = pd.Series(dict_selcol)
print(ser_selcol)

print(ser_selcol.index)
print(ser_selcol.values)

print(ser_selcol[9])

print(ser_selcol[ser_selcol>='O'])

ser_selcol.index.name = 'Num_Cam' #you can name the index with this sentence
ser_selcol.name = 'Jugador' 
print(ser_selcol)
