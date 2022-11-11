import numpy as np

#exercise 2, identify and use: 
#bincount() & bincount().argmax()
#hsatck, vstack, dstack
#tolist
#comparison.all
#flipud
#isin
#flatten
#unique
#asarray
#where

#bincount()
#is a numpy method used to obtain the frequency of each element provided inside a numpy array.
a = np.arange(9) 
print(np.bincount(a).argmax())