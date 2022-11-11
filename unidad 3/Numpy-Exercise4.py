import numpy as np

#reverse a 1D numpy array without using numpy specific functions

a = np.arange(1,7)
x = a.size-1
b = a.copy()
print('Arreglo inicial', a)
for i in range(6):
    a[i] = b[x]
    x -= 1

print('Salida', a)
