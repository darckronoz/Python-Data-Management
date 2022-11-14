import pandas as pd
import numpy as nepe

#the null values are none or NaN
#with the method fillna you can change the nulls for something #inplace=False by default
#with the method dropna you can delete the nulls rows #inplace=False by default

df = pd.DataFrame({'col1':[1,2,3,nepe.nan],
'col2':[nepe.nan,555,666,444],
'col3':['abc','def','ghi',None]})

print(df.fillna('0', inplace=True))
print(df)


