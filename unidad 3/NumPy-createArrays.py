import numpy as np

#numpy arange:
#return evenly spaced values withina given interval
#numpy.arange(start, stop, step, dtype=None, *, like=None)
 
print(np.arange(-20, 1, 0.5, dtype=float))#starts at -20 ends at 1 without
#generating the 1 and spacing values by 0.5 and with Data type float.

#numpy linspace
#creates and return a reference to an array where its elements are the sequence of n equidistants values.
#from start to finish.
#equidistant: values equaly distant from each other. (google it)
print(np.linspace(start=0, stop=5, num=5))

temperatures = np.linspace(13.6, 18.2, 20) #temperatures lineal Y axis with numbers between 13.6 and 18.2.
print(temperatures)


#array initialization

zeros = np.zeros(50) #array filled with 0.0 type float64
print(zeros.dtype)
print(zeros)

print('----')
ones = np.ones((4, 3)) #matrizxs filled with 1.0 type float64
print(ones.dtype)
print(ones)

print('----')

identity = np.identity(4) #matrizxs filled with 0.0 and pricipal diagonal with 1.0 type float64
print(identity.dtype)
print(identity)

print('----')

eye = np.eye(4, k=1) #matrizxs filled with 0.0 and a diagonal with 1.0 (with the k value you choose 
# the start of the diagonal) type float64
print(eye.dtype)
print(eye)

#in the eye you can change the start of the diagonal in the identity you cant.

