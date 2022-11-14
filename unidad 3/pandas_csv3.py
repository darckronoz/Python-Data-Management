import pandas as pd
import os

# Check current working directory.
retval = os.getcwd()
print(retval)

path = "D:\\dev\\university\\Python-Data-Management\\"

# Now change the directory
os.chdir(path)

# Check current working directory.
retval = os.getcwd()
print(retval)

data = pd.read_csv('employees.csv', sep=';')

#dont understand what this explication was... edit: the file was on the wrong directory...
#it works fine

#generate csv from dataframe

#import from json file

import json 
with open('_personFile.json','r') as j:
    data = json.load(j)

dataframe = pd.DataFrame(data)

dataframe.to_csv('filepersonas.csv', index=False)
