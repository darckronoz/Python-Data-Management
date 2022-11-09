import numpy as np

#get into elements of an array

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[1, 0])
print('----')
print(a[1][0])
print('----')
print(a[1:,0])
print('----')
print(a[:, 0:2])

#filter with a[condition] you get an array with the elements from (a) that matches the condition

print(a[(a%2 ==0) & (a > 2)])