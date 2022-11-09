#numpy anotations.
#numpy se especializa en calculo numerico y analisis de datos en gran volumen
#incorpora arrays 
#procesar vectores o matrices es mucho mas rapido con numpy
import numpy as np

a = np.array([1, 2, 3, 4, 5]) #create numpy array
#print(a)

#print(a.shape) #prints a tuple with the dimensions of the array

#print(a.ndim) #prints the number of dimensions

#print(a.size) #prints the number of elements

#you can do math operations with numpy arrays 
x = np.array([[1, 2, 3],[ 1, 1, 1]], dtype=np.int32)
y = np.array([[1, 0, 5], [6, 8, 1]])

#print(x)
#print(y)
#print('-----------')
#print(x + y)
#print('-----------')
#print(x*y)
#print('-----------')
#print(x**y)

#you can cast an array like so

z = x.astype(np.float64) #x as float
#print(z)

c = np.array([1.1, 2.3, 4.4, -3.1, -4.9, -0.6])
#print(c)

#cast c to int

cint = c.astype(np.int32)

#print(cint)

#string list to float numpy array

equis = ['1.1', '-2.54', '-2.44', '2.99', '0.99']
tmp = np.array(equis)

#print(tmp)

tmp_float = tmp.astype(np.float64)

#print(tmp_float)

tmp_int = tmp_float.astype(np.int32)

#print(tmp_int)

#attributes of a numpy array

#shape, ndim, size already explained
#dtype obtains the type of the elements.

print('----------------------')

#Arrays and diferent dimensions.

#print(list(range(1, 13)))
arreglo=np.array(range(1, 13))
#print(arreglo)
arreglo.shape=(3,4) #change the shape from list to a matriz. the dimensions must match the 
#number of elements (12 elements from the list, dimensions must be (1,12), (4,3), (6,2) etc)...
matriz=arreglo
#print(matriz)


matriz2=matriz.reshape(3,4) #reshape obtains the reshaped object
#shape change the attribute
matriz2


#print(np.ravel(matriz2)) #flatened object with all the elements
#print("----------")
np.ravel(matriz2,order='F')
#the order parameter: 
# C to flat and order in the principal row order, default value.
# F to flat and order in the principal column order.
# K to flat and order in the order the elements were storaged.
# A to flat and order with the natural index.

#print(list(range(1, 25)))
cubo = np.array(range(1, 25))
print(cubo.size)


cubo.shape = (2, 2, 6) #three dim array: 2 number of arrays(matriz), 2 rows, 6 columns.
print(cubo)
print(cubo.shape)
print(cubo.ndim)



