#first: verify the difference between append() and extend().

from mimetypes import init
from re import T


sample_list_one = ['ubuntu', 'debian', 'redhat', 'popOs', 'turupes', 'ccarros']
sample_list_two = ['naranja', 'fresa', 'aceite', 'amistad', 'puertas', 'python']

sample_list_one.extend(['hola', 'adios']) #extends the list adding the elements, if it is a string then takes the string as a list and adds all its chars.
sample_list_two.append(['hola', 'adios']) #adds the element at the final, if it's a list then it'll be a list in that position, not the list extended with the new list.

print(sample_list_one)
print(sample_list_two)

sample_list_two.insert(0, 'nuevo primero')
print(sample_list_two)
sample_list_one.sort(reverse=True)
print(sample_list_one)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# cual es la variante de index en la siguiente sentencia
print(fruits.index('banana', 4)) #the second parameter sets the start index.
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[1:4] = ["X"] #this takes the first but not the last one. in this case the: 1, 2, 3 and stops at the 4 without changing it.
print (letras)


