import pandas as pd

#import excel files

dataframe_excel = pd.read_excel('employees.xlsx', sheet_name='employees')

print(dataframe_excel.head())

#generate excel file from dataframe (the dataframe from the json file xd)

#import from json file

import json 
with open('_personFile.json','r') as j:
    data = json.load(j)

dataframe = pd.DataFrame(data)

file_name = 'filepersonas.xlsx'

dataframe.to_excel(file_name)
print('completed, succesfully imported into excel file')