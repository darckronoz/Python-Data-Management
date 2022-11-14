import pandas as pd

#import the data from google drive csv file.
url="https://drive.google.com/uc?export=download&id=1TJrHAQo-wrZe0zmbXGYehhDf1-58-kmK"
data = pd.read_csv(url)


#exercise 1.
#Look for null values use info() function
#change the nulls for 0
data.fillna ('0', inplace=True)

data.info()
#reload the dataset

datanew = pd.read_csv(url)
#delete the null rows
datanew.dropna(inplace=True)
datanew.info()

#observe the data type of each serie

print(datanew.dtypes)

#the majority of data is object cuz it was created from a csv file.

#print(datanew[datanew.Team == 'Finance'][['First Name', 'Team']])

