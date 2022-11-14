import pandas as pd

df = pd.DataFrame({'col 1': [1, 2, 3],
                    'col 2': [4, 5, 6],
                    'col 3': [7, 8, 9],
                    'Resume': [10, 11, 12]})

print(df)

df.set_axis(['X', 'Y', 'Z', 'Resume'], axis=1, inplace=True) #to replace/rename all the keys

print(df)

df.rename({'Z': 'sumama'}, axis=1, inplace=True) #to replace/rename a specific key

print(df.keys())

#you can also create a dataframe from an array and later asing columns like so

data = [['tom', 10], ['nick', 15], ['juli', 14]]

df2 = pd.DataFrame(data, columns=['Name', 'Age'], index=[5,45,8])

print(df2)