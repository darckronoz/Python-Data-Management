import pandas as pd

data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata',
'Mahindra', 'Maruti', 'Hyundai',
'Renault', 'Tata', 'Maruti'],
'Year': [2012, 2014, 2011, 2015, 2012,
2016, 2014, 2018, 2019],
'Kms Driven': [50000, 30000, 60000,
25000, 10000, 46000,
31000, 15000, 12000],
'City': ['Gurgaon', 'Delhi', 'Mumbai',
'Delhi', 'Mumbai', 'Delhi',
'Mumbai', 'Chennai', 'Ghaziabad'],
'Mileage': [28, 27, 25, 26, 28,
29, 24, 21, 24]})

print(data['City'][0])

ndata = data.to_numpy()
#print(ndata)

maruti = data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)]
maruti2 = data[(data.Brand == 'Maruti') & (data.Mileage > 25)][['Brand', 'Mileage']]
print(maruti)
print(maruti2)

print(data.loc[5:5])
#print(data.iloc[1:4])