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
a = [7, 7, 7, 7, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(np.bincount(a).argmax())
#argmax()
#is a numpy method that returns the index of the first maximum value in an array
#combining this two methods we can find the number that appears most often in the array.

#hsatck, vstack, dstack
#hstack
#return an array stacking 2 or more arrays in this case horizontaly (column wise)
x = np.array((1, 2, 3))
y = np.array((4, 5, 6))
print("hstack")
print(np.hstack((x, y)))
x.shape = (3,1)
y.shape = (3,1)
print(np.hstack((x, y)))

#vstack
#return an array stacking 2 or more arrays in this case vertically (row wise)
x = np.array((1, 2, 3))
y = np.array((4, 5, 6))
print("vstack")
print(np.vstack((x, y)))
x.shape = (3,1)
y.shape = (3,1)
print(np.vstack((x, y)))

#dstack
#return an array stacking 2 or more arrays in this case depth wise (along third axis)
x = np.array((1, 2, 3))
y = np.array((4, 5, 6))
print("dstack")
print(np.dstack((x, y)))
x.shape = (3,1)
y.shape = (3,1)
print(np.dstack((x, y)))


#tolist
#return the array as an a.ndim-levels deep nested list of python scalars
#Return a copy of the array data as a (nested) Python list.
#  Data items are converted to the nearest compatible builtin Python type, via the item function.
print("tolist")
x = np.float32([1, 2, 3])
x_list = list(x)
print(x, x_list, type(x_list[0])) #in this case the type is still de float32 from numpy.
x_tolist = x.tolist()
print(x, x_tolist, type(x_tolist[0])) #and here the type is the basic float from python.

#comparison.all
#this is the form you compare 2 arrays, but is no the best to compare 2 arrays
#np.array_equal([arrays]) always produce the best result
print("comparison.all")
x = np.array([1])
y = np.array([])
print((x==y).all(), '.all')
print(np.array_equal(x,y), 'array_equal')

#flipud (flip upside down)
#Reverse the order of elements along axis 0 (up/down).
print('flipud')
x = np.diag([1.0, 2, 3])
print('original \n ', x)
print( 'flipped \n ', np.flipud(x))

#isin
#Calculates element in test_elements, broadcasting over element only.
#Returns a boolean array of the same shape as element that is True
#where an element of element is in test_elements and False otherwise.
print('isin')

x = np.array(range(10))
y = np.array([5, 6, 7, 8])

print(np.isin(x, y))

#flatten
#Return a copy of the array collapsed into one dimension.
#order:
# C to flat and order in the principal row order, default value.
# F to flat and order in the principal column order.
# K to flat and order in the order the elements were storaged.
# A to flat and order with the natural index.

x = np.arange(16)
x.shape = (4, 4)
print(x, 'original')
print(x.flatten(order='C'), 'flatten order: C')
print(x.flatten(order='F'), 'flatten order: F')
print(x.flatten(order='K'), 'flatten order: K')
print(x.flatten(order='A'), 'flatten order: A')

#unique
#Find the unique elements of an array.
#with the parameters you can also get the index of each element and the count.
x = np.array([1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 1, 1, 1, 1])
arrx, indexs, counts = np.unique(x, return_counts=True, return_index=True)
print('unique')
print(x, 'original')
print(arrx, 'array')
print(counts, 'counts')
print(indexs, 'indexs')

#asarray
#Convert the input to an array.
print('asarray')
x = [1, 2, 3]
y = np.asarray(x)
print(x, type(x), 'tipo original')
print(y, type(y), 'tipo asarray')


#where
#Return elements chosen from x or y depending on condition.
x = np.arange(10)
print(x, 'original')
print(np.where(x < 5, x, x*0), 'where with a condition')