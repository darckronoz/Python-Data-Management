import pandas as pd

#import the data from google drive csv file.
url="https://drive.google.com/uc?export=download&id=1TJrHAQo-wrZe0zmbXGYehhDf1-58-kmK"
data = pd.read_csv(url)


#exercise 1.
#1. Look for null values use info() function
#2. change the nulls for 0
data.fillna ('0', inplace=True)

data.info()
#3. reload the dataset

datanew = pd.read_csv(url)
#4. delete the null rows
datanew.dropna(inplace=True)
datanew.info()

#5. observe the data type of each serie

print(datanew.dtypes)

#the majority of data is object cuz it was created from a csv file.

#6. select the employees from team Finance.

print(datanew[datanew.Team == 'Finance'][['First Name', 'Team']])

#7. reload the dataset and create a new dataframe with:
#First Name, Gender and salary. and show the 100 index


datal = pd.read_csv(url)
newDataFrame = datal[['First Name', 'Gender', 'Salary']]
print(newDataFrame.loc(100))

#8. sort by salary, ascending and descending

salarySortedAs = newDataFrame.sort_values(by=['Salary'], ascending=True)
salarySortedDes = newDataFrame.sort_values(by=['Salary'], ascending=False)

print(salarySortedDes)

#9 show employees with salary from 49000 to 50000.
#show name and salary

salaryQuery = newDataFrame[(newDataFrame.Salary > 49000) & (newDataFrame.Salary < 50000)][['First Name', 'Salary']]
print(salaryQuery)

#10. change the name of the serie First Name for Nombre

newDataFrame.rename({'First Name': 'Nombre'}, axis=1, inplace=True)
print(newDataFrame.keys())

#11. Count the rows of item 9

newDataFrame.loc(9)

