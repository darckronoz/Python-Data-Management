import pandas as pd

#1. file punto1.txt

#2. HDF5
from pandas import HDFStore
#create HDF5 from dataframe

#import from json file

import json 
with open('_personFile.json','r') as j:
    data = json.load(j)

dataframe = pd.DataFrame(data)

#hdf = HDFStore('hdf_file.h5')

#store data in hdf5 file

#hdf.put('key1', dataframe, format='table', data_columns=True)

#3. html

#read html from web **install package lxml with pip.

table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')
print(f'Total tables: {len(table_MN)}')
#this imports all the tables from the site, there are 31 tables and thats a lot

table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota',
 match='United States presidential election results for Minnesota')

 #with match parameter we can select just the table we want.
 #html5lib installed with pip
 #beautifulsoup4 installed with pip


dataframefromhtml = table_MN[0]
print(dataframefromhtml.head())

#in order to do any query we need to replace the percentage values.
dataframefromhtml[['Republican', 'Democratic', 'Third party']].replace({'%': ''}, regex=True)
print(dataframefromhtml.head())

#4. pdf from dataframe
#using the df from the last exercise (dataframefromhtml)

#plot table with matplotlib and then generate the pdf

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=dataframefromhtml.values,colLabels=dataframefromhtml.columns,loc='center')

#https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
pp = PdfPages("minesota.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()


#5. create excel from df
#the same as the last exercise 

dataframefromhtml.to_excel('minesota.xlsx')

