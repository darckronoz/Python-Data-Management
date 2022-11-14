import pandas as pd

#import from json file

import json 
with open('_personFile.json','r') as j:
    data = json.load(j)

dataframe = pd.DataFrame(data)

print(dataframe.head(1))

tags = dataframe['tags']

list_tags_1 = dataframe.loc[1:1,['tags']]
list = list_tags_1.to_numpy()
print(list)
print(list[0][0][0])
